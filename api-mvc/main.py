
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

            wm = WeatherModel(zip)
            wv = WeatherView()
            wv.dos = wm.dos

            f.additional_view = wv.c

        self.response.write(f.print_out())

class WeatherView(object):
    def __init__(self):
        self.dos = []
        self.c = ''

    @property
    def dos(self):
        pass

    @dos.setter
    def dos(self, arr):
        self.__dos = arr
        self.create_display()


    def create_display(self):
        for do in self.__dos:
            self.c+= "Day: " + do.day
            self.c+= "( "+do.date+" )"
            self.c+= " High "+ do.high+ " Low: " + do.low
            self.c+= "<img src=\"img/" + do.code + '.png" /> '
            self.c+= "<br />"
            print self.c


class WeatherModel(object):

    def __init__(self, z):
        self.url = "http://xml.weather.yahoo.com/forecastrss?p="

        request = urllib2.Request(self.url+z)

        opener = urllib2.build_opener()

        opener.open(request)

        self.data = opener.open(request)
        self.parse()

    def parse(self):
        xmldoc = minidom.parse(self.data)
        forecast = xmldoc.getElementsByTagName("yweather:forecast")

        self.__dos = []

        for item in forecast:
            do = WeatherDataObject()
            do.day = item.attributes['day'].value
            do.date = item.attributes['date'].value
            do.high = item.attributes['high'].value
            do.low = item.attributes['low'].value
            do.code = item.attributes['code'].value
            do.text = item.attributes['text'].value
            self.__dos.append(do)

        print self.__dos[0].day

    @property
    def dos(self):
        return self.__dos

class WeatherDataObject(object):
    def __init__(self):
        self.high = 0
        self.low = 0
        self.code = 0
        self.description = ''
        self.date = ''
        self.day =''


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

    additional_view = ""

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
        self._content = self._form_open + self.create_inputs() + self._form_close + self.additional_view
        return Page.print_out(self)

# '''
#     def print_out(self):
#         return self._head+ self._form_open + self.create_inputs() + self._form_close + self._close
# '''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
