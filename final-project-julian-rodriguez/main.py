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
from page import *
import json
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        view = FormPage()
        view.form_header = "Food App"

        #gets the modle and view to de presented on the page(model gathers data.)
        if self.request.GET:

            if self.request.GET.has_key('search'):

                search = self.request.GET['search']

                f_modle =  FoodModle()
                searchResults = f_modle.search(search)

                f_view = FoodView()
                f_view.dos = searchResults
                f_view.update()
                view.page_content = f_view.content

            elif self.request.GET.has_key('page'):

                f_modle =  FoodModle()
                id = self.request.GET['id']
                f_modle.read_by_id(id)

                f_view = FoodDetailsView()
                f_view.dos = f_modle.dos
                f_view.update()
                view.page_content = f_view.content


        self.response.write(view.print_out())

class FoodView(object):
    def __init__(self):
        self.fdo = FoodDataObject() #data object that holds information
        self.dos = []
        self.content = ''

    def update(self):
        for recipe in self.dos:
            #content that will be printed on the view. This is take from the page class.
            self.content += '''
            <div class="matches">

                <img src=" '''+recipe.image_big +''' ">

                <div class="title">
                    <h3>''' + recipe.recipe_name + ''' </h3>
                </div>

                <div class="data">
                    <h3>'''+str(recipe.rating)+''' out of 5</h3>
                    <hr class="clear">
                    <h3>Total Time: '''+str(recipe.time) +'''</h3>
                    <hr class="clear2">
                    <a class="link" href="/?page=''' +recipe.id+ '''">GET STARTED</a>
                </div>
            </div>
            '''

class FoodDetailsView(object):
    def __init__(self):
        self.fdo = FoodDataObject() #data object that holds information
        self.dos = []
        self.content = ''

    def update(self):
        for recipe in self.dos:
            #content that will be printed on the view. This is take from the page class.
            self.content += '''
            <div class="matches">

                <img src=" '''+recipe.image_big +''' ">

                <div class="title">
                    <h3>''' + recipe.recipe_name + ''' </h3>
                </div>

                <div class="data">
                    <h3>'''+str(recipe.rating)+''' out of 5</h3>
                    <hr class="clear">
                    <h3>Total Time: '''+str(recipe.time) +'''</h3>
                    <hr class="clear2">
                    <a class="link" href= "''' +recipe.link_a+ '''">GET STARTED</a>
                </div>
            </div>
            '''



class FoodModle(object):
    ''' This class handles the data requests and sorting data from the API'''


    def __init__(self):

        self.__dos = []


    def search(self, query = ''):  #request for data ^^^^^ in the url (api)

        self.full_url = 'http://api.yummly.com/v1/api/recipes?_app_id=835c05a2&_app_key=5d0e15329a55763e866fdcbfffc512f6&q=' + query

        req = urllib2.Request(self.full_url)

        opener = urllib2.build_opener()

        data = opener.open(req)

        #parse it
        jsondoc= json.load(data)

        self.__fdo = FoodDataObject()

        #loop to read thru the objects
        for recipe in jsondoc['matches']:
            fdo = FoodDataObject()

            #First Data Call from the api
            fdo.recipe_name = recipe['recipeName'].replace("{" , '"')
            fdo.recipe_name = fdo.recipe_name.replace("}" , '"')
            fdo.rating = recipe['rating']

            fdo.id = recipe ['id']


            #This calls the second part of the api
            self.__fdo.url = "http://api.yummly.com/v1/api/recipe/" + str(fdo.id) + "?_app_id=835c05a2&_app_key=5d0e15329a55763e866fdcbfffc512f6"
            req2 = urllib2.Request(self.__fdo.url)
            opener2 = urllib2.build_opener()
            data2 = opener2.open(req2)
            jsondoc2 = json.load(data2)

            #data from the second data calll
            fdo.image_big = jsondoc2['images'][0]['imageUrlsBySize']["360"]
            fdo.link_a = jsondoc2["source"]["sourceRecipeUrl"]
            fdo.time = jsondoc2["totalTime"]

            self.__dos.append(fdo)

        return self.__dos;

    def read_by_id(self, id):

        # request a url passing it the id

        # parse the returned json

        # put the parsed data into a FoodDataObject

        # return the FoodDataObject

        pass

class FoodDataObject(object):
    def __init__(self):
        self.ingredients = ''
        self.rating = ''
        self.id = ''
        self.code = 0
        self.recipe_name = ''
        self.image = ''

        self.image_big = ''
        self.link_a = ''
        self.time =''


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
