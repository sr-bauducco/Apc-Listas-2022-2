import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

def calculaDistancia(x1,x2,y1,y2):
    d = ((x2-x1)**2)+((y2-y1)**2)
    dab = math.sqrt(d)
    if dab <= 100:
        print(f"É o amor da minha vida!")
    elif dab <= 200:
        print(f"Talvez dê certo")
    else:
        print(f"Não vale a pena investir")


calculaDistancia(x1,x2,y1,y2)