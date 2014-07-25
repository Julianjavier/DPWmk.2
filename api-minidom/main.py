
import webapp2
import urllib2
from xml.dom import minidom

class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Hello world!')

        # p= Page()

        f= FormPage()
        f.inputs = [{'type':'text', 'placeholder':'Zip Code', 'name':'zip'},
        {'type':'submit', 'name':'submit', 'value':'Get Weather'}]

        if self.request.GET:
            zip = self.request.GET['zip']

            request = urllib2.Request("http://xml.weather.yahoo.com/forecastrss?p="+zip)

            opener = urllib2.build_opener()

            opener.open(request)

            data = opener.open(request)

            xmldoc = minidom.parse(data)

            titles = xmldoc.getElementsByTagName("title")

            images = xmldoc.getElementsByTagName("image")


            forecast = xmldoc.getElementsByTagName("yweather:forecast")

            c = ""

            for i in forecast:
                c += i.attributes['day'].value + "(" + i.attributes['date'].value + ")"
                c += " HIGH: " + i.attributes['high'].value + '%deg; ' + "LOW: " + i.attributes['low'].value + '%deg;'
                c += "<img scr= \"images/" + i.attributes['code'].value + '.png" width="30">'
                c +='<br/>'
                self.response.write(c)

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
