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
        self.response.write('Hello world!')

class PageBuilder(object):
    def __init__(self):

        self.open = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{self.title}</title>
            <link href="css/style.css" rel="stylesheet" type="text/css">
        </head>
        <body>
        <div class="wrap">

        '''

        self.nav= '''
       <nav>
            <ul>
                <li><a href="?an=">WALE</a></li>
                <li><a href="?an=">WOLF</a></li>
                <li><a href="?an=">LION</a></li>
            </ul>
       </nav>
        '''

        self.close = '''
        </div>
        </body>
        </html>
        '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
