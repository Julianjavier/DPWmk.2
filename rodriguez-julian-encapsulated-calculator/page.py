
class Character(object):
    def __init__(self):
        self.__name = ""                                                               ##
        self.__str = 10                                                                 ##
        self.__dex = 10                  ## These will hold values for the character sheet
        self.__chr = 10
        self.__int = 10                                                                 ##
        self.__con = 10                                                                 ##

    ###getter for private variable
    @property
    def name(self):
        return self.__name

    ###setter for private variable
    @name.setter
    def name(self, name):
        self.__name = name

    ###
    @property
    def str(self):
        return self.__str

    @str.setter
    def str(self, str):
        self.__str = str

    ###
    @property
    def dex(self):
        return self.__dex

    @dex.setter
    def dex(self, dex):
        self.__dex = dex

    ###
    @property
    def chr(self):
        return self.__chr

    @chr.setter
    def chr(self, chr):
        self.__chr = chr

    ###
    @property
    def int(self):
        return self.__int

    @int.setter
    def int(self, int):
        self.__int = int

    ###
    @property
    def con(self):
        return self.__con

    @con.setter
    def con(self, con):
        self.__con = con

    @property
    def total(self):
        return self.__str + self.__dex + self.__chr + self.__int + self.__con

class Page(object):
    def __init__(self):
        ##HTML Template

        self.charcter = Character()

        self.__open = '''

        <!DOCTYPE html>
        <html>
            <head>
                <title></title>
                <link href="css/style.css" rel="stylesheet" type="text/css">
                <link href='http://fonts.googleapis.com/css?family=Cinzel:400,700' rel='stylesheet' type='text/css'>
            </head>
        <body>

            <header>
                <img src="img/Vagrant.png">
            </header>

            <nav>
                <a href="?char=bodark" >Bodark Bjorn</a>
                <a href="?char=nock" >Nock Fletching</a>
                <a href="?char=magnar" >Magnar Magnil</a>
                <a href="?char=lina" >Lina Medina</a>
            </nav>

            <div class="wrap">

        '''
        self.__content = '''

                    <h2>{self.character.name}</h2>
                    <hr>

                    <div>
                        <h4 class="inline">Strength</h4>
                        <p>{self.character.str}</p>
                    </div>

                    <div>
                        <h4 class="inline">Dexterity</h4>
                        <p>{self.character.dex}</p>
                    </div>

                    <div>
                        <h4 class="inline">Charisma</h4>
                        <p>{self.character.chr}</p>
                    </div>

                    <div>
                        <h4 class="inline">Intelligence</h4>
                        <p>{self.character.int}</p>
                    </div>

                    <div>
                        <h4 class="inline">Constitution</h4>
                        <p>{self.character.con}</p>
                    </div>

                    <hr>

                    <div>
                        <h3 class="inline">Total Level</h3>
                        <p>{self.character.total}</p>
                    </div>

                </div>

                '''

        self.__close = '''
            </div>
            <div class="fake"></div>
            <footer> <p>Property  of Team Vagrant</p> </footer
        </body>
        </html>
        '''

    def print_info(self): ##function to print page
        all = self.__open + str(self.__content) + self.__close
        return all.format(**locals())

    def character(self, character): ##function to link format link
        self.character = character

    # @property   ##getter
    # def totalVal(self):
    #     return self.__all
    #
    # @totalVal.setter  ##setter
    # def totalVal(self, newTotal):
    #     self.__all = str(newTotal)
