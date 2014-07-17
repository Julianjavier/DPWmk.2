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

from page import Character
from page import Page


class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write("Herro")

        p = Page()

        bodark = Character()
        bodark.name="Bodark Bjorn"
        bodark.str = 15
        bodark.dex = 7
        bodark.chr = 8
        bodark.int = 3
        bodark.con = 10


        nock = Character()
        nock.__name= "Nock Fletching"
        nock.__str = 7
        nock.__dex = 15
        nock.__chr = 12
        nock.__int = 6
        nock.__con = 3

        players = {
            "bodark":bodark,
            "nock":nock
        }

        if self.request.GET:
            if self.request.GET.has_key('char'):

                character = self.request.GET['char']

                if players.has_key(character):
                    p.character(players[character])
                    render = p.print_info()

        else:
            render =  p.character(players["bodark"])

        self.response.write(render)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
