# single_level_Inheritance

class GamboaA:
    def father(self):
        print('I am PistoB father')

class PistoB(GamboaA):
    def child1(self):
        print('I am a child1')


obj = PistoB()
obj.father()
obj.child1()



