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

from page import main_page
import webapp2

class MainHandler(webapp2.RequestHandler):

    def get(self):
        p= main_page
        if self.request.GET:
            fn = self.request["firstname"]
            ls = self.request["lastname"]
            cn1 = self.request["content1"]
            cn2 = self.request["content2"]
            self.response.write()

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
