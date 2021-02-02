import warnings
warnings.filterwarnings("ignore")

import unittest
import json
import requests
from requests.exceptions import Timeout
import pandas as pd
from multiprocessing import Pool
from unittest.mock import patch

RESULT_FIELDS = ['energy', 'lat', 'lon']
CONCERNED_FIELDS = ['date', 'energy', 'lat', 'lat-dir', 'lon', 'lon-dir']


class DataNotFoundError(Exception):
    pass


class NASAApi:
    """
    A simple wrapper for NASA API

    Attributes:
    ----------
    root_url:str
        variable to hold base url

    Methods:
    --------
    _get_url(**kwargs):
        takes input params and return url
    fetch_records(kwargs):
        takes input parms and returns records for stars
    """

    def __init__(self):
        self.root_url = 'https://ssd-api.jpl.nasa.gov/fireball.api?'

    def _get_url(self, **kwargs):
        """
        :param kwargs: keyword args
        :return: url(str)
        """
        suffix=''
        for k, v in kwargs.items():
            suffix += str(k.replace('_', '-'))+'='+str(v)+'&'
        return (self.root_url+suffix).rstrip('&')

    def fetch_records(self, **kwargs):
        """
        :param kwargs: keyword args
        :return: dict
        """
        url = self._get_url(**kwargs)
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


class BrightestStarPredictor(NASAApi):
    """
    Simple class to get the Brightest star based in energy radiated

    Attributes:
    ----------
    buffer: int
        buffer to be considered when calculating the stars in range of co-ords
    filters: dict
        keyword args for query params to filter data from NASA Api

    Methods:
    --------
    _get_dataframe(data):
        takes the data and generates dataframe
    _update_latlon_signs(row):
        takes dataframe row and updates lat, lon columns
    prepare_dataframe(df):
        updates dataframe and does some manipulation
    _filter_dataframe(df):
        filters dataframe rows based on buffer
    fireball(coords):
        takes lat/lon and returns brightest star
    """

    def __init__(self, buffer=15, **filters):
        self.buffer = buffer
        self.filters = filters
        super().__init__()

    @staticmethod
    def _get_dataframe(data):
        """
        :param data: json
        :return: pandas dataframe
        """
        cols = data.get('fields')
        content = data.get('data')
        df = pd.DataFrame(data=content, columns=cols)
        return df

    @staticmethod
    def _update_latlon_signs(row):
        """
        :param row: dataframe series
        :return: series
        """
        row['lat'] = row['lat'] * (-1) ** (row['lat-dir'] == 'S')
        row['lon'] = row['lon'] * (-1) ** (row['lon-dir'] == 'W')
        return row

    @staticmethod
    def prepare_dataframe(df):
        """
        :param df: pandas dataframe
        :return: pandas dataframe
        """
        df_updated = df[CONCERNED_FIELDS]
        # Checked the dtypes of the dataframe and found columns we are interested in are of object type
        # obviously we need to change the type to float to perform operation
        df_updated[RESULT_FIELDS] = df_updated[RESULT_FIELDS].astype('float')
        df_updated = df_updated.apply(BrightestStarPredictor._update_latlon_signs, axis=1)
        return df_updated

    def _filter_dataframe(self, df, coords):
        """
        :param df: pandas dataframe
        :param coords: tuple of lat/lon
        :return: pandas dataframe
        """
        df = df.loc[(df['lat'] >= coords[0] - self.buffer) & (df['lat'] <= coords[0] + self.buffer) &
                        (df['lon'] >= coords[1] - self.buffer) & (df['lon'] <= coords[1] + self.buffer)]
        return df

    def fireball(self, coords):
        """
        :param coords: tuple of lat/lon
        :return:
        """
        params = self.filters
        try:
            json_resp = self.fetch_records(**params)
        except Exception:
            raise
        if not json_resp:
            raise DataNotFoundError
        new_df = self.prepare_dataframe(self._get_dataframe(json_resp))
        df = self._filter_dataframe(new_df, coords)
        df = df[RESULT_FIELDS].head(1)
        return df.iloc[0][RESULT_FIELDS[0]], df.iloc[0][RESULT_FIELDS[1]], df.iloc[0][RESULT_FIELDS[2]]


class TestNasaApi(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = NASAApi()
        self.expected_url = 'https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2017-01-01&req-alt=true&energy-min=0.3&sort=-energy'

    def test_get_url(self):
        resp = self.obj._get_url(date_min="2017-01-01", req_alt="true", energy_min="0.3", sort="-energy")
        self.assertIsInstance(resp, str)
        self.assertEqual(self.expected_url, resp)

    def test_fetch_records(self):
        resp = self.obj.fetch_records(date_min="2017-01-01", req_alt="true", energy_min="0.3", sort="-energy")
        self.assertIsInstance(resp, dict)


class TestFireBall(unittest.TestCase):

    def setUp(self) -> None:
        warnings.filterwarnings("ignore")
        self.obj = BrightestStarPredictor(date_min="2017-01-01", req_alt="true", energy_min="0.3", sort="-energy")
        self.data = '{"signature":{"source":"NASA/JPL Fireball Data API","version":"1.0"},' \
                                                  '"count":"5","fields":["date","energy","impact-e","lat","lat-dir","lon","lon-dir","alt","vel"],' \
                                                  '"data":[["2018-12-18 23:48:20","13000","173","56.9","N","172.4","E","25.6","32.0"],' \
                                                  '["2020-12-22 23:23:33","489.8","9.5","31.9","N","96.2","E","35.5","13.6"],' \
                                                  '["2017-12-15 13:14:37","311.4","6.4","60.2","N","170.0","E","20.0","31.4"],' \
                                                  '["2019-06-22 21:25:48","294.7","6","14.9","N","66.2","W","25.0","14.9"],' \
                                                  '["2019-02-18 10:00:43","195.8","4.2","15.5","S","25.3","E","26","20.8"]]}\n'
        self.inputs = [(42.354558, -71.054254), (28.574389, -77.312638), (37.793700, -122.403906)]

    def test_fireball(self):
        pool = Pool(processes=3)
        results = pool.map(self.obj.fireball, self.inputs)
        brightest_star = sorted(results, key=lambda x: x[0])[-1]
        self.assertIsInstance(results, list)
        print("Brightest star, with Brightness and lat/lon", brightest_star)
        pool.close()

    @patch('driver.requests')
    def test_fireball_exception(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            self.obj.fireball((42.354558, -71.054254))

    @patch('driver.NASAApi.fetch_records')
    def test_fireball_DataNotFound_exception(self, mock_nasaapi):
        mock_nasaapi.return_value = None
        with self.assertRaises(DataNotFoundError):
            self.obj.fireball((42.354558, -71.054254))

    def test_get_dataframe(self):
        data = json.loads(self.data)
        resp = self.obj._get_dataframe(data)
        self.assertIsInstance(resp, pd.DataFrame)

    def test_prepare_dataframe(self):
        data = json.loads(self.data)
        df = self.obj._get_dataframe(data)
        new_df = self.obj.prepare_dataframe(df)
        self.assertIsInstance(new_df, pd.DataFrame)

    def test_filter_dataframe(self):
        data = json.loads(self.data)
        df = self.obj._get_dataframe(data)
        new_df = self.obj.prepare_dataframe(df)
        final_df = self.obj._filter_dataframe(new_df, (42.354558, -71.054254))
        self.assertIsInstance(final_df, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

