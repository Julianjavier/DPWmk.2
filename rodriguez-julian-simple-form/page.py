
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

            <div class="address">
                <h3>Address</h3>
                <input type="text" name="address" placeholder="Address:">
            </div>

            <div class="check-box">
                <hr>
                <h3>Toppings</h3>
                <input type="checkbox" name="topping1" value="Meat-Lovers"><p>Meat-Lovers</p><br>
                <input type="checkbox" name="topping2" value="Peperoni"><p>Peperoni</p><br>
                <input type="checkbox" name="topping3" value="Pineapple"><p>Pineapple</p><br>
                <input type="checkbox" name="topping4" value="The Flying Calzo"><p>The Flying Calzo</p><br>
                <hr>
            </div>

            <h3>Serving Size</h3>
            <select name="select" class="select-list">
                <option value="Personal">Personal</option>
                <option value="Small">Small</option>
                <option value="Medium">Medium</option>
                <option value="Large">Large</option>
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

    def content_page(self, var1, var2, var3, var4, var5):
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
        '''

        self.address_open='''<h3>'''
        self.address= var5
        self.address_close='''</h3>
         <hr>
        '''


        self.radio_open='''
        <h3>Toppings</h3>
        <h1>'''
        self.content2= var3

        self.radio_close=''' </h1>
        <hr>
        '''

        self.select_open='''
        <h3>Serving Size</h3>

        <h1>'''
        self.content3= var4

        self.select_close=''' </h1>
        '''

        self.page_close='''
        </div>
    </body>
</html>
        '''

        return self.page_open \
               + self.name_open + self.full_name + self.name_close \
               + self.address_open + self.address + self.address_close\
               + self.radio_open + self.content2 + self.radio_close\
               + self.select_open + self.content3 + self.select_close \
               +self.page_close