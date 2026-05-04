# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

def main(productos: int) -> dict:
    diccionario: OrderedDict = OrderedDict()
    
    for  _ in range(productos):
        item = input()
        producto, precio = item.rsplit(" ", 1)
        
        if producto not in diccionario:
            diccionario.setdefault(producto, int(precio))
        else:
            diccionario[producto] += int(precio)
    
    return diccionario
    

if __name__ == "__main__":
    productos = int(input())
    
    resultado: dict = main(productos)
    
    for _ in resultado.keys():
        print(f'{_} {resultado[_]}')
