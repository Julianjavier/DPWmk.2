
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
                <option value="1" name="content2">1</option>
                <option value="2" name="content2">2</option>
                <option value="3" name="content2">3</option>
            </select>

            </form>
        '''

        self.page_close='''
        </div>
    </body>
</html>
        '''

    def print_out(self, var1, var2, var3, var4):
        return self.page_open + self.page_content + self.page_close

    def content_page(self):
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

        self.full_name_open='''<h1>

        '''
        self.content1= var1+" "+var2
        self.full_name_close='''</h1>
        <hr>
        '''

        self.radio_open='''
        <h3>Current Class</h3>
        <h1>'''
        self.content2= var3
        self.radio_close=''' </h1>
        <hr>
        '''

        self.select_open='''
        <h3>Land of Origin</h3>

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