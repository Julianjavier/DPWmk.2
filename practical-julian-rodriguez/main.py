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
import json
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')



class MusicModel(object):
    def __init__(self):

        mdo = MusicObject()

        self.full_url="http://rebeccacarroll.com/api/music/music.json"
        req=urllib2.Request(self.full_url)
        opener=urllib2.build_opener()
        data=opener.open(req)
        jsondoc=json.load(data)

        track= jsondoc['songs']['track']

class MusicObject(object):
    def __init__(self):
        self.file=''
        self.title=''
        self.artist=''
        self.length=''
        self.year=''
        self.label=''
        self.cover=''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
