# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()


#
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
#
# Enjoy your interview!
#
# ===== Preface =====
#
# This question is very difficult in C and C++, where there is
# insufficient library support to answer it in an hour. If you
# prefer to program in one of those languages, please ask us to
# provide you with a question designed for those languages instead!
#
#
# ===== Intro =====
#
# Here at Delphix, we admire NASA’s engineering mission. But beyond
# that, we can use data from NASA to learn about how space interacts
# with Earth. Solving global warming is unfortunately outside the scope
# of an interview question, so your goal is somewhat simpler: use
# NASA’s public HTTP APIs to create a function which determines which
# of three locations has seen the brightest shooting stars since 2017.
# This can be handy if you're trying to find a good spot to do some night sky
# watching. :-)
#
# You should implement this in whatever language you're most
# comfortable with -- just make sure your code is commented,
# has error handling, and is modularized if possible.
#
# Finally, please help us by keeping this question and your
# answer secret so that every candidate has a fair chance in
# future Delphix interviews. Thank you!
#
#
# ===== Steps =====
#
# 1.  Choose the language you want to code in from the menu
#     labeled "Plain Text" in the top right corner of the
#     screen. You will see a "Run" button appear on the top
#     left -- clicking this will send your code to a Linux
#     server and compile / run it. Output will appear on the
#     right side of the screen.
#
#     For information about what libraries are available for
#     your chosen language, see:
#
#       https://coderpad.io/languages
#
# 2.  Pull up the documentation for the API you'll be using:
#
#       https://ssd-api.jpl.nasa.gov/doc/fireball.html
#
# 3.  Implement a function fireball() whose function signature
#     looks like this (can differ slightly depending on the
#     language you chose):
#
#       Object fireball(double latitude, double longitude)
#
#     When there is enough data to do so, the function should
#     return the brightness and location for the brightest shooting
#     star seen since 2017 at the given location.
#
#     The human eye can see a lot of the night sky, so give your latitude
#     and longitude a buffer of +/- 15. For example, if you are looking
#     for shooting stars at the Delphix SF Office
#          37.7937007 N,  122.4039064 W
#     You would look for shooting stars within these coordinates:
#          (22.7937007   <--> 52.7937007 N,
#          107.4039064 <--> 137.4039064 W)
#
#     *Note* that Latitude and Longitude can be written in a few different
#     formats. We suggest either using Signed Degrees, or Degrees plus
#     Compass Direction:
#
#     Signed Degrees:
#      - Latitudes range from -90 to 90.
#      - Longitudes range from -180 to 180.
#
#     Degrees plus Compass Direction:
#     Latitudes range from 0 to 90.
#     Longitudes range from 0 to 180.
#     Use N, S, E or W as either the first or last character, which
#     represents a compass direction North, South, East or West.
#
#     The brightness should be determined using the energy from each
#     shooting star (a higher ‘energy’ meaning a brighter star).
#
#     You can use the https://ssd-api.jpl.nasa.gov/doc/fireball.html API
#     to get the information you will need to compute this.
#
# 4.  With your fireball() function, determine which of three
#     locations had the brightest shooting star since
#     2017. Print out the location and brightness for that star.
#
#     Use these Delphix Office Locations to figure out which Office
#     saw the brightest star since 2017 (2017-01-01 -> 2020-01-01)
#
#
#     Boston -        latitude: 42.354558N, longitude:  71.054254W
#     NCR -           latitude: 28.574389N, longitude:  77.312638E
#     San Francisco - latitude: 37.793700N, longitude: 122.403906W
#
#
# 5.  Add any tests for your code to the main() method of
#     your program so that we can easily run them.
#
# 6.  Don’t forget to implement error handling. Depending on the language
#     you are using, feel free to adjust the function signature to do it in an
#     idiomatic way (e.g Exceptions in Java)
#
#
#
# ====== FAQs =====
#
# Q:  How do I submit my code when I am done?
# A:  Once you are happy with your code, email your interviewer
#     telling them that you have finished the assignment. They will handle
#     getting the code to our graders.
#
# Q:  Won't we be able to see a wider longitude range the higher our latitude
#     (with an extreme of either the North or South Pole)?
# A:  That is correct. But to help simplify this problem you can just assume
#     that we can only see the +/- 15 degrees regardless of your location.
#
# Q:  How do I know if my solution is correct?
# A:  Make sure you've read the prompt carefully and you're
#     convinced your program does what you think it should
#     in the common case. If your program does what the prompt
#     dictates, you will get full credit. We do not use an
#     auto-grader, so we do not have any values for you to
#     check correctness against.
#
# Q:  What is Delphix looking for in a solution?
# A:  After submitting your code, we'll have a pair of engineers
#     evaluate it and determine next steps in the interview process.
#     We are looking for correct, easy-to-read, robust code.
#     Specifically, ensure your code is idiomatic and laid out
#     logically. Ensure it is correct. Ensure it handles all edge
#     cases and error cases elegantly.
#
# Q:  How should my output be formatted?
# A:  Your output should include a location and the energy of the
#     star in whatever format you find easiest. There are no other
#     strict formatting constraints (we just inspect the output for
#     correctness).
#
# Q:  If I need a clarification, who should I ask?
# A:  Send all questions to the email address that sent you
#     this document, and an engineer at Delphix will get
#     back to you ASAP (we're pretty quick during normal
#     business hours).
#
# Q:  How long should this question take me?
# A:  Approximately 1 hour, but it could take more or less
#     depending on your experience with web APIs and the
#     language you choose.
#
# Q:  When is this due?
# A:  We will begin grading your answer 24 hours after it is
#     sent to you, so that is the deadline.
#
# Q:  How do I turn in my solution?
# A:  Anything you've typed into this document will be saved.
#     Email us when you are done with your solution. We will
#     respond confirming we've received the solution within
#     24 hours.
#
# Q:  Can I use any external resources to help me?
# A:  Absolutely! Feel free to use any online resources you
#     like, but please don't collaborate with anyone else.
#
# Q:  Can I use my favorite library in my program?
# A:  Unfortunately, there is no way to load external
#     libraries into CoderPad, so you must stick to what
#     they provide out of the box for your language (although
#     they do support for many popular general-use libraries):
#
#       https://coderpad.io/languages
#
#     If you really want to use something that's not
#     available, email the person who sent you this link
#     and we will work with you to find a solution.
#
# Q: Can I code this up in a different IDE?
# A: Of course! However, we do not have your environment
#     to run your code in. We ask that you submit your final
#     code via CoderPad (and make sure it can run). This gives
#     our graders the ability to run your code rather than guessing.
#
# Q:  Why does my program terminate unexpectedly in
#     CoderPad, and why can't I read from stdin or pass
#     arguments on the command line?
# A:  CoderPad places a limit on the runtime and amount of
#     output your code can use, but you should be able to
#     make your code fit within those limits. You can hard
#     code any arguments or inputs to the program in your
#     main() method or in your tests.
#
# Q:  I'm a Vim/Emacs fan -- is there any way to use those
#     keybindings? What about changing the tab width? Font
#     size?
# A:  Yes! Hit the button at the bottom of the screen that
#     looks like a keyboard.
#
#
#
"""
Approach:

1) Create a function to have co-ordinates of location as input
2) Hit NASA api with required filters(date, energy-min etc) and get the json back
3) create a dataframe (easy to visualise, and think) from the json
4) Prepare dataframe as per our need (signed degrees etc)
5) filter dataframe as per our rules of (+/- 15 for lat/long) and get the rows that fall into the given filter
6) Run 3 parallel instances of your function (for eg. using multiprocessing, threading. etc), get the results
6) Return the one with highest enery radiated.
"""

import warnings

warnings.filterwarnings("ignore")

import requests
import pandas as pd
from multiprocessing import Pool


class DataNotFoundError(Exception):
    pass


class NASAApi:

    def __init__(self):
        self.root_url = 'https://ssd-api.jpl.nasa.gov/fireball.api?'

    def _get_url(self, **kwargs):
        suffix = ''
        for k, v in kwargs.items():
            suffix += str(k.replace('_', '-')) + '=' + str(v) + '&'
        return (self.root_url + suffix).rstrip('&')

    def fetch_records(self, **kwargs):
        url = self._get_url(**kwargs)
        r = requests.get(url)
        r.raise_for_status()
        return r.json()


class BrightestStarPredictor(NASAApi):

    def __init__(self, buffer=15, **filters):
        self.buffer = buffer
        self.filters = filters
        super().__init__()

    @staticmethod
    def _get_dataframe(data):
        cols = data.get('fields')
        content = data.get('data')
        return pd.DataFrame(content,
                            columns=cols)

    @staticmethod
    def _update_latlon_signs(row):
        row['lat'] = row['lat'] * (-1) ** (row['lat-dir'] == 'S')
        row['lon'] = row['lon'] * (-1) ** (row['lon-dir'] == 'W')
        return row

    @staticmethod
    def prepare_dataframe(df):
        df_updated = df[['date', 'energy', 'lat', 'lat-dir', 'lon', 'lon-dir']]
        df_updated[['energy', 'lat', 'lon']] = df_updated[['energy', 'lat', 'lon']].astype('float')
        df_updated = df_updated.apply(BrightestStarPredictor._update_latlon_signs, axis=1)
        return df_updated

    def _adjust_buffer(self, coords):
        return

    def _filter_dataframe(self, df, coords):
        df = df.loc[(df['lat'] >= coords[0] - self.buffer) & (df['lat'] <= coords[0] + self.buffer) &
                    (df['lon'] >= coords[1] - self.buffer) & (df['lon'] <= coords[1] + self.buffer)]
        return df

    def fireball(self, coords):
        params = self.filters
        try:
            json_resp = self.fetch_records(**params)
        except Exception:
            raise
        if not json_resp:
            raise DataNotFoundError
        df = self.prepare_dataframe(self._get_dataframe(json_resp))
        df = self._filter_dataframe(df, coords)
        return df.head(1).iloc[0]['lat'], df.head(1).iloc[0]['lon'], df.head(1).iloc[0]['energy']


if __name__ == '__main__':
    obj = BrightestStarPredictor(date_min="2017-01-01", req_alt="true", energy_min="0.3", sort="-energy")
    pool = Pool(processes=3)
    inputs = [(42.354558, -71.054254), (28.574389, -77.312638), (37.793700, -122.403906)]
    results = pool.map(obj.fireball, inputs)
    print(sorted(results, key=lambda x: x[2])[-1])

# TODO - 1: DocStrings, comments
#        2: Revisit Exception Handling
#        3: Code Review
#        4: Unit tests
# :O -- Will do it tomorrow





