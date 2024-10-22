#! /usr/bin/python3

class gato:
    
    __name = None
    __hambre = True
    __sleepy = False
    
    def __init__(self, aname = "micifu") -> None:
        self.__name = aname
        self.pedirComida()
    
    def __str__(self) -> str:
        answ = f"me llamo {self.__name}"
        return answ

    def comer(self):
        self.__hambre = False
        self.__sleepy = True

    def dormir(self):
        print(f"{self.__name}: zzzzz")
        self.__sleepy = False
        self.__hambre = True

    def pedirComida(self):
        if self.__hambre:
            print(f"{self.__name}: dame comida, esclavo")
        else:
            print(f"{self.__name}: no tengo hambre")

    def tocar(self):
        if not self.__hambre:
            print(f"{self.__name}: dejameeeee")
        else:
            self.prrr()
            self.pedirComida()

    def prrr(self):
        print("prrrr")

    
if __name__ == "__main__":
      
    # g0 = gato()
    # # print(g0)
    # g0.pedirComida()
    # g0.comer()
    # g0.pedirComida()
        
    g1 = gato("Noche")
    # print(g1)
    g1.pedirComida()
    g1.comer()    
    g1.pedirComida()    
    g1.tocar()
    g1.dormir()
    g1.tocar()







