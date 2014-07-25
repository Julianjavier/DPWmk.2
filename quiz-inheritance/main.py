#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('QUIZ IT IS')


class car(object):
    def __init__(self):

        self.tires = ""
        self._gastank = 0

    def mpg(self):
        mile = self._gastank / 10
        return mile

    def price(self):
        self.price = 0
        return self.price


class lambo(car):
    def __init__(self):
        car.__init__(self)

        self.tires = "14'inch"
        self._gastank = 100

        self.heated_seat = "YES"
        self.airbags = "YES"

        self.price = 350000


class fordF150(car):
    def __init__(self):
        car.__init__(self)

        self.tires = "10'inch"
        self._gastank = 150

        self.heated_seat = "YES"
        self.airbags = "YES"

        self.price = 25000







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
