
class constructor(object):
    def __init__(self):
        self.__name = ""                                                               ##
        self.__str = 0                                                                 ##
        self.__def = 0                                                                 ##
        self.__agl = 0                  ## These will hold values for the character sheet
        self.__int = 0                                                                 ##
        self.__con = 0                                                                 ##
        self.__totla = self.__str + self.__def + self.__agl + self.__int + self.__con  ##

class Page(object):
    def __init__(self):
        ##HTML Template
        self.__open = '''

        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
                <link href="css/style.css" rel="stylesheet" type="text/css">

            </head>
        <body>

            <div class="wrap">
                <header>
                    <img src="img/Title-01.png">
                </header>

        '''
        self.__content = '''

                <nav>
                    <a href="?char=bodark" >Bodark Bjorn</a>
                    <a href="?char=nock" >Nock Fletching</a>
                    <a href="?char=magnar" >Magnar Magnil</a>
                    <a href="?char=lina" >Lina Medina</a>
                </nav>

                    <h2>{self.NAME}</h2>
                    <hr>

                    <div>
                        <h4 class="inline">Strength</h4>
                        <p>{self.STR}</p>
                    </div>

                    <div>
                        <h4 class="inline">Dexterity</h4>
                        <p>{self.DEX}</p>
                    </div>

                    <div>
                        <h4 class="inline">Charisma</h4>
                        <p>{self.CHR}</p>
                    </div>

                    <div>
                        <h4 class="inline">Intelligence</h4>
                        <p>{self.INT}</p>
                    </div>

                    <div>
                        <h4 class="inline">Constitution</h4>
                        <p>{self.CON}</p>
                    </div>

                    <hr>

                    <div>
                        <h3 class="inline">Total Level</h3>
                        <p>{self.total}</p>
                    </div>

                </div>

                '''

        self.__close = '''
            </div>
            <footer> <p>Property  of Team Vagrant</p> </footer
        </body>
        </html>
        '''

        self.__all = self.__open + str(self.__content) + self.__close