def menorSalario(lista_num):
    num= [float(i) for i in lista_num]
    if len(num)>0:
        menor = min(num)
    #   num.index(menor)
        return num.index(menor)+1
    else:
        return 0


parada = False
entrada = ''
lista_nome = []
lista_num = []
while parada == False:
    entrada = input().split(",")
    if entrada[0] == "Fim":
        parada = True
    else:
        lista_nome.append(entrada[0])
        lista_num.append(entrada[1])
        parada = False
        
if menorSalario(lista_num)>=1:
    print(lista_nome[menorSalario(lista_num)-1])
else:
    print ("Não tem")

    
