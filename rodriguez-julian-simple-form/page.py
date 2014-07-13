
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
                <input type="text" name="firstname" placeholder="First Name:">

            <div>
                <input type="radio" name="rating" value="1">
                <input type="radio" name="rating" value="2">
                <input type="radio" name="rating" value="3">
                <input type="radio" name="rating" value="4">
            </div>

            <select name="select">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>

            </form>
        '''

        self.page_close='''
        </div>
    </body>
</html>
        '''

    def print_out(self):
        return self.page_open + self.page_content + self.page_close