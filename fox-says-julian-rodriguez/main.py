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
        p = PageBuilder()
        p.title = "Welcome!"

        whale = Whale()
        wolf = Wolf()
        lion = Lion()

        if self.request.GET:
            animal = self.request.GET['an']

            if animal == "o1":
                p.animal = whale
            elif animal == "o2":
                p.animal = wolf
            elif animal == "o3":
                p.animal = lion
            else:
                p.animal == lion

        self.response.write(p.print_out())

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

        self.content = '''

            <hr>

            <img src="{self.animal.url}">

            <div>
                <h1>{self.animal.name}</h1>
                <li>Phylum: {self.animal.phylum}</li>
                <li>Class: {self.animal.a_class}</li>
                <li>Order: {self.animal.order}</li>
                <li>Family: {self.animal.family}</li>
                <li>Genus: {self.animal.genus}</li>
                <li>Life Span: {self.animal.life}</li>
                <li>Habitat: {self.animal.habitat}</li>
                <li>Geolocation: {self.animal.geolocation}</li>
                <li>Sound: {self.animal.sound}</li>
            </div>

        </div>
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

    def print_out(self):
        output = self.open + self.nav + self.content + self.close
        return output.format(**locals())

class Animal(object):
     def __init__(self):

        self._sound = "Null"

        self.name = ""
        self.phylum = ""
        self.a_class = ""
        self.order = ""
        self.family = ""
        self.genus = ""
        self.url = ""
        self.life = ""
        self.habitat = ""
        self.geolocation = ""

     @property
     def sound(self):
        return self._sound


class Wolf(Animal):
    def __init__(self):

        Animal.__init__(self)

        self._sound = "HOOOOOWWWWWWLLLLLL"

        self.name = "German Grey Wolf"
        self.phylum = "Chordata"
        self.a_class = "Mammalia"
        self.order = "Carnivora"
        self.family = "Canidae"
        self.genus = "Canis"
        self.url = "http://cdn1.spiegel.de/images/image-260730-galleryV9-cpos.jpg"
        self.life = "10 years"
        self.habitat = "Dence woodlands and Plains"
        self.geolocation = "Asia, Europa and North America"


class Whale(Animal):
    def __init__(self):

        Animal.__init__(self)

        self._sound = "wwwwhhhhaaaalllleeeessss"

        self.name = "Blue Whale"
        self.phylum = "Chordata"
        self.a_class = "Mammalia"
        self.order = "Cetacea"
        self.family = "Balaenopteridae"
        self.genus = "Balaenoptera"
        self.url = "http://www.amosphotography.com/data/photos/310_1diver_and_bluewhale.jpg"
        self.life = "20 years"
        self.habitat = "The Ocean"
        self.geolocation = "We went over this."


class Lion(Animal):
    def __init__(self):

        Animal.__init__(self)

        self._sound = "MEOW"

        self.name = "African Savanna Lion"
        self.phylum = "Chordata"
        self.a_class = "Mammalia"
        self.order = "Carnivora"
        self.family = "Felidae"
        self.genus = "Panthera"
        self.url = "http://www.universeofsymbolism.com/images/lion-2.jpg"
        self.life = "15 years"
        self.habitat = "South Africa plains"
        self.geolocation = "Africa"


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
