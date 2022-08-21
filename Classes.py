class  student:
    name = 'Mateus'
    lastname = 'Goncalves de Ouro'

    def getGrades(self):
        print(self.name + ' ' + self.lastname)
        return '2:1'


mateus = student()
mateus.getGrades()
