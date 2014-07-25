
import webapp2
import urllib2

import json

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        # p= Page()

        p= FormPage()
        p.inputs = [{'type':'text', 'placeholder':'City Code', 'name':'city'},
                    {'type':'text', 'placeholder':'Country Code', 'name':'country'},
                    {'type':'submit', 'name':'submit', 'value':'Get Weather'}]

        if self.request.GET:
            city = self.request.GET['city']
            country = self.request.GET['country']

            request = urllib2.Request("http://api.openweathermap.org/data/2.5/weather?q="+city+","+country)

            opener = urllib2.build_opener()

            opener.open(request)

            data = opener.open(request)

            jsondoc = json.load(data)

            temp = jsondoc['main']['temp']

            f = (float(temp)- 263.15) * 1.8 + 32

            self.response.write(city +" is currently "+ str(f) + "&deg;")


        self.response.write(p.print_out())

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

    _form_close = '''</form> '''

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
            if 'placeholder' in i:
                tot_inputs += ' placeholder= "' + i['placeholder'] + '"'
            if 'value' in i:
                tot_inputs += 'value="' + i['value'] + '"'
            tot_inputs += '/>'

        return tot_inputs

    def print_out(self):
        self._content = self._form_open + self.create_inputs() + self._form_close
        return Page.print_out(self)

# '''
#     def print_out(self):
#         return self._head+ self._form_open + self.create_inputs() + self._form_close + self._close
# '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
