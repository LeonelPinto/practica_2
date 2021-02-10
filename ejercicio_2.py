import pluck
def seleccionar_val():
    valor1 = {'a': 1,'b':3,'c':4,'a':8}
    print(valor1.pluck([valor1],'a'))
