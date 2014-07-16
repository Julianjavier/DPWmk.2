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

class constructor(object):
    def __init__(self):
        self.__name = ""    ##
        self.__str = 0      ##
        self.__def = 0      ##
        self.__agl = 0      ## These will hold values for the character sheet
        self.__int = 0      ##
        self.__con = 0      ##
        self.__totla = 0    ##

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
