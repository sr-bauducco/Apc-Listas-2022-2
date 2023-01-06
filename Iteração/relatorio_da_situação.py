def maiorSalario(lista_num):
    num= [float(i) for i in lista_num]
    if len(num)==0:
        return "Não tem"
    else:
        maior = max(num)
        return num.index(maior)
 
def menorSalario(lista_num):
    num= [float(i) for i in lista_num]
    if len(num)>0:
        menor = min(num)
        return num.index(menor)+1
    else:
        return 0

def media(lista_num):
    soma=0.00
    num = [float(i) for i in lista_num]
    if len(num) == 0:
        return "0.00"
    else:
        media = sum(num)/ len(lista_num)
    return  f"{media:.2f}"

entrada = ''
parada = 0
lista_nome = []
lista_num = []
n=int(input())
while parada < n:
    entrada = input().split(",")
    lista_nome.append(entrada[0])
    lista_num.append(entrada[1])
    parada = parada+1
if n == 0:
    print (f'Não tem média')
    print(f'Não tem')
    print(f'Não tem')
else:
    print(media(lista_num))
    print(lista_nome[maiorSalario(lista_num)], lista_num[maiorSalario(lista_num)])
    print(lista_nome[menorSalario(lista_num)-1], lista_num[menorSalario(lista_num)-1])
