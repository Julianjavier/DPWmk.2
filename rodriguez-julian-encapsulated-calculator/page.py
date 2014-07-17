
class Character(object):
    def __init__(self):
        self.__name = ""                                                               ##
        self.__str = 0                                                                 ##
        self.__dex = 0                  ## These will hold values for the character sheet
        self.__int = 0                                                                 ##
        self.__con = 0                                                                 ##

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def total(self):
        return self.str + self.dex + self.int + self.con

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
            <footer> <p>Property  of Team Vagrant</p> </footer
        </body>
        </html>
        '''

    def print_info(self):
        all = self.__open + str(self.__content) + self.__close
        return all.format(**locals())

    def character(self, character):
        self.character = character

    # @property   ##getter
    # def totalVal(self):
    #     return self.__all
    #
    # @totalVal.setter  ##setter
    # def totalVal(self, newTotal):
    #     self.__all = str(newTotal)
