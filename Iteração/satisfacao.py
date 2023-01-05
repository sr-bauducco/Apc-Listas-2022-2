def calcula(lista_num):
    soma=0.00
    num = [float(i) for i in lista_num]
    if len(num) == 0:
        return "0.00"
    else:
        media = sum(num)/ len(lista_num)
    return  f"{media:.2f}"

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
print(calcula(lista_num))


    


