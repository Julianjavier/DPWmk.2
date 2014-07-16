
class Page(object):

    __css = ""
    header = '''
    <!DOCTYPE HTML>
        <head>
        <title></title>
        <link rel="stylesheet" type="text/css" href="{self.css}">
        </head>
        <body>
    '''

    __content="WELCOME"

    closer= '''
        </body>
    </html>
    '''

    def __init__(self):
        pass


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, c):
        self.__content = c

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, c):
        self.__css = c
        self.header = self.header.format(**locals())

    def print_out(self):
        return self.header + self.__content + self.closer