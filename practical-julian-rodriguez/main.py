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

        model= MusicModel()
        page_view = MusicView()

        self.response.write(model.dos)
        self.response.write(page_view.fullPage)

class MusicModel(object):
    def __init__(self):

        self.dos = []

        self.full_url="http://rebeccacarroll.com/api/music/music.json"
        req=urllib2.Request(self.full_url)
        opener=urllib2.build_opener()
        data=opener.open(req)
        jsondoc=json.load(data)

        for i in range (0, 9):
            self.mdo = MusicObject()
            track= jsondoc['songs']['track'][i]
            self.mdo.artist=track['artist']
            self.mdo.cover=track['cover']
            self.mdo.label=track['label']
            self.mdo.title=track['title']
            self.mdo.length=track['length']
            self.mdo.year=track['year']
            self.dos.append(self.mdo)

class MusicView(object):
    def __init__(self):

        model= MusicModel()


        self.open = '''
        <!DOCTYPE>
        <html>
            <body>
        <nav>
            <li><a href="?q=bob">Bob Dylan</a></li>
            <li><a href="?q=stones">The Rolling Stones</a></li>
            <li><a href="?q=john">John Lennon</a></li>
        </nav>

        '''

        self.content = '''
        '''

        self.close = '''
            </body>
        </html>
        '''

        self.content += '''
            <h1>'''+model.mdo.title+'''</h1>
            <h1>'''+model.mdo.year+'''</h1>
            <h1>'''+model.mdo.length+'''</h1>
            <h1>'''+model.mdo.label+'''</h1>
            <img src="'''+model.mdo.cover+'''"/>
        '''

        self.fullPage = self.open + self.content + self.close

        # @property
        # def content():
        #     self.__content
        #
        # @content.setter
        # def content():
        #     content = self.__content
        #     return content



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
