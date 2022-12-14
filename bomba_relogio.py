n= int(input())
p = int(input())
inicial = n
def imprimeSegundos(n):
    while n>0:
        print(f"Atenção faltam {n} segundos...")
        n=n-1
    return n
    

if (imprimeSegundos(n)) ==5:
    print(f"Seu tempo está acabando!")

        