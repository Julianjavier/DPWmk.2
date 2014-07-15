
class main_page(object):
    def __init__(self):
        self.page_open='''
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <link href="css/styles.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="wrap">

        <img src="img/fly.png"/>
        '''
        self.page_content='''
            <form method="GET">

            <div class="fullname">
                <h3>Full Name</h3>
                <input type="text" name="firstname" placeholder="First Name:">
                <input type="text" name="lastname" placeholder="Last Name:">
            </div>

            <div class="e-mail">
                <h3>E-Mail</h3>
                <input type="text" name="e-mail" placeholder="First Name:">
            </div>

            <div class="check-box">
                <hr>
                <h3>E-Mail</h3>
                <input type="radio" name="content1" value="1"><p>1</p><br>
                <input type="radio" name="content1" value="2"><p>2</p><br>
                <input type="radio" name="content1" value="3"><p>3</p><br>
                <input type="radio" name="content1" value="4"><p>4</p><br>
                <hr>
            </div>

            <h3>Serving Size</h3>
            <select name="select" class="select-list">
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
        <link href="css/styles.css" rel="stylesheet" type="text/css">
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