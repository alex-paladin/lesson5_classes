# comment line added in DEV branch

class Gadget:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_name(self):
        a = 'My name is '+self.name
        print(a)

    def describe_yourself(self):
        print(f'I am {self.color}')


class Smartphone(Gadget):

    def __init__(self, name, color, memory):
        super().__init__(name, color)
        self.memory = memory

    def show_name(self):
        a = 'My name is '+self.name+' and I am a smartphone!'
        print(a)

    def describe_yourself(self):
        print(f'I am {self.color} and I can store {self.memory} Gb')

class Tablet(Gadget):

    def __init__(self, name, color, display):
        super().__init__(name, color)
        self.display = display

    def show_name(self):
        a = 'My name is '+self.name+' and I am a tablet PC!'
        print(a)

    def describe_yourself(self):
        print(f'I am {self.color} and I have {self.display} inch display')


object_list = [
            Smartphone('iPhone ','white',64),
            Smartphone('iPhone','black',128),
            Tablet('iPad','silver',10.5),
            Tablet('iPad', 'white', 12.9),
            Tablet('Samsung Galaxy Tab', 'white', 10.5)
]

for obj in object_list:

    print('Hello!')
    obj.show_name()
    obj.describe_yourself()
