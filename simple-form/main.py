
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()

        if self.request.GET:
            p.content = "First Name " + self.request.GET['fname']
            self.response.write(p.print_out_page())
        else:
            self.response.write(p.print_out_form())


class Page(object):

    header ='''
        <!DOCTYPE>
        <html>
            <head>
                <link rel="stylesheet" href="css/style.css" type="text/css" />
                <title>Welcome</title>
            </head>
            <body>
            '''

    content = ''' Hello there '''

    form_content='''
        <form>
            <input type="text" placeholder="First Name" name="fname"/>
            <input type="submit" value="submit"/>

        </form
    '''

    close = '''
        </body>
        </html>
    '''

    def __init__(self):
        pass

    def print_out_page(self):
        return self.header +self.content + self.close

    def print_out_form(self):
        return self.header +self.form_content + self.close

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
