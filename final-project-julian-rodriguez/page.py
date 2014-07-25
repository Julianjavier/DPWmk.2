__author__ = 'julianrodriguez'


class Page(object):
    def __init__(self):
        self._open ='''
        <!DOCTYPE html>
        <html>
            <head>
                <title>SEARCH.dot.EAT</title>
                <link href='http://fonts.googleapis.com/css?family=Raleway' rel='stylesheet' type='text/css'>
                <link href="css/style.css" rel="stylesheet" type="text/css">
            </head>
        <body>

            <header>
                <img src="img/search-01.png">
            </header>
            <hr>
            <div class="wrap">
        '''

        self._content= ''

        self._close='''

            </div>
        <footer>

        </footer>
        </body>
        </html>
        '''


    def print_out(self):
            self.update()
            return self.all

    def update(self):
        self.all = self._open + self._content + self._close
        self.all = self.all.format(**locals())

class FormPage(Page):
    def __init__(self):
        Page. __init__(self)
        self.__form_open= '<form method="GET" action="">'
        self.__inputs= '''
                <input class="text" type="text"  name="code" placeholder="Key Word" required/>
                <button class="submit" type="submit"/>SUBMIT</button>
        '''
        self.__form_close= '</form>'

        self.page_content= ''


        self._content = self.__form_open + self.__inputs + self.__form_close

    def update(self):
        self.all = self._open + self.__form_open  + self.__inputs + self.__form_close + self.page_content + self._close
        self.all = self.all.format(**locals())