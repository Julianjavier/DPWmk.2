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


        p = Page()

        bodark = Character()
        bodark.name="Bodark Bjorn"
        bodark.str = 15
        bodark.dex = 7
        bodark.chr = 8
        bodark.int = 3
        bodark.con = 10


        nock = Character()
        nock.name= "Nock Fletching"
        nock.str = 7
        nock.dex = 15
        nock.chr = 12
        nock.int = 6
        nock.con = 3

        magnar = Character()
        magnar.name="Magnar Magnil"
        magnar.str = 16
        magnar.dex = 17
        magnar.chr = 10
        magnar.int = 2
        magnar.con = 8


        lina = Character()
        lina.name= "Lina Medina"
        lina.str = 5
        lina.dex = 5
        lina.chr = 3
        lina.int = 15
        lina.con = 15

        players = {
            "bodark":bodark,
            "nock":nock,
            "magnar":magnar,
            "lina":lina
        }

        p.character(players["bodark"])
        render =  p.print_info()

        if self.request.GET:
            if self.request.GET.has_key('char'):

                character = self.request.GET['char']

                if players.has_key(character):
                    p.character(players[character])
                    render = p.print_info()

        self.response.write(render)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
