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

from page import main_page

class MainHandler(webapp2.RequestHandler):


    def get(self):
        p= main_page()

        if self.request.GET:
            var1 = self.request.GET["firstname"]
            var2 = self.request.GET["lastname"]
            var3 = ','
            var4 = self.request.GET["select"]
            var5 = self.request.GET["address"]

            # if 'topping1' in self.request.GET:
            #     print 'IS THERE!!!'
            # else:
            #     print 'IS NOT THERE'
            #
            # if self.request.GET["topping1"]:
            #     var3 += self.request.GET["topping1"]
            #
            # if self.request.GET["topping2"]:
            #     var3 += self.request.GET["topping2"]
            #
            # if self.request.GET["topping3"]:
            #     var3 += self.request.GET["topping3"]
            #
            # if self.request.GET["topping4"]:
            #     var3 += self.request.GET["topping4"]

            var3 += ' ' + self.request.get("topping1", default_value = ' ')
            var3 += ' ' + self.request.get("topping2", default_value = ' ')
            var3 += ' ' + self.request.get("topping3", default_value = ' ')
            var3 += ' ' + self.request.get("topping4", default_value = ' ')

            self.response.write(p.content_page(var1, var2, var3, var4, var5))
        else:
            self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
