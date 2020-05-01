class person():
    name =  'person name '
    def speak(self):
        print('person speak') 
    
    @staticmethod
    def eat():
        print('person eat')

class lin(person):
    # name = ' lins name '
    def speak(self):
        print("lins speak")

    @staticmethod
    def eat():
        print('lins eat')

zejia  =  lin()
zejia.speak()
zejia.__class__.eat()

print(zejia.__class__.name)