# _level_Inheritance

class GamboaA:
    def father(self):
        print('I am PistoB father')

class PistoB(GamboaA):
    def child1(self):
        print('I am a child1')

class LindaC(GamboaA, PistoB):
    def p_child1(self):
        print('I am PistoB child and GamboaA g_child')


obj = PistoB()
obj.father()
obj.child1()
# obj.p_child1()