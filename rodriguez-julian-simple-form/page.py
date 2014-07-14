
class main_page(object):
    def __init__(self):
        self.page_open='''
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="wrap">
        '''
        self.page_content='''
            <form method="GET">
                <input type="text" name="firstname" placeholder="First Name:">
                <input type="text" name="lastname" placeholder="First Name:">

            <div>
                <input type="radio" name="content1" value="1">
                <input type="radio" name="content1" value="2">
                <input type="radio" name="content1" value="3">
                <input type="radio" name="content1" value="4">
            </div>

            <select name="select">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>

            <input class="SUBMIT" type="submit" name="submit" value="SUBMIT">

            </form>
        '''

        self.page_close='''
        </div>
    </body>
</html>
        '''

    def print_out(self):
        return self.page_open + self.page_content + self.page_close

    def content_page(self, var1, var2, var3, var4):
        self.page_open='''
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="wrap">
        '''

        self.name_open='''<h1>

        '''
        self.full_name= var1+" "+var2
        self.name_close='''</h1>
        <hr>
        '''

        self.radio_open='''
        <h3>Content1</h3>
        <h1>'''
        self.content2= var3

        self.radio_close=''' </h1>
        <hr>
        '''

        self.select_open='''
        <h3>Content2</h3>

        <h1>'''
        self.content3= var4

        self.select_close=''' </h1>
        <hr>
        '''

        self.page_close='''
        </div>
    </body>
</html>
        '''

        return self.page_open \
               + self.name_open + self.full_name + self.name_close \
               + self.radio_open + self.content2 + self.radio_close\
               + self.select_open + self.content3 + self.select_close \
               +self.page_close