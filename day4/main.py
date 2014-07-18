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
        # self.response.write('Hello world!')

        # p= Page()

        f= FormPage()
        f.inputs = [{'type':'text', 'placeholder':'First Name', 'name':'fname'},
        {'type':'email','placeholder':'Email','name':'email'},
        {'type':'button', 'name':'submit', 'value':'Go'}]

        f.print_out()
        self.response.write(f.print_out())

class Page(object):
    _head = '''
    <!DOCTYPE html>
        <html>
            <head>
                <title>{self.title}</title>
                <link rel="stylesheet" type="text/css" {self.css_url}>
            </head>
        <body>
    '''
    _content = ''

    _close = '''
    </body>
    </html>
    '''

    def __init__(self):
        pass

    def print_out(self):
        return self._head + self._content + self._close

class FormPage(Page):

    __inputs = []

    _form_open = '''<form method="GET" action="" />'''

    _form_close = '''</form '''

    def __init__(self):
        Page.__init__(self)

    @property
    def inputs(self):
        pass

    @inputs.setter
    def inputs(self, i):
        self.__inputs = i

    def create_inputs(self):
        tot_inputs = ''

        for i in self.__inputs:
            tot_inputs += '<input type="'+ i['type'] + '" name="' + i['name'] + '"'
            if 'placerholder' in i:
                tot_inputs += ' placeholder= "' + i['placeholder'] + '"/>'
            if 'value' in i:
                tot_inputs += 'value="' + i['value'] + '"'
            tot_inputs += '"/>'

        return tot_inputs

    def print_out(self):
        self._content = self._form_open + self.create_inputs() + self._form_close
        return Page.print_out(self)

'''
    def print_out(self):
        return self._head+ self._form_open + self.create_inputs() + self._form_close + self._close
'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
