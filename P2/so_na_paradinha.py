def imprime(x,y,intervalo=1):
    if x > y:
        y_inicial= y
        while y <= x:
            print(y,end=" ")
            y= y+intervalo
        y = y_inicial
        print()
        if y+intervalo >= x:
            pass
        else:
            imprime(x,y,intervalo= intervalo+1)
    else:
        x_inicial= x
        while x <= y:
            print(x,end=" ")
            x= x+intervalo
        x = x_inicial
        print()
        if x+intervalo >= y:
            pass
        else:
            imprime(x,y,intervalo= intervalo+1)        
    

x,y = input().split(',')
x= int(x)
y= int(y)
imprime(x,y)