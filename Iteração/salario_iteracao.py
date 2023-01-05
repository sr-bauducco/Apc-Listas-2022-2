def maiorSalario(lista_num):
    num = [float(i) for i in lista_num]
    sorted(num,)
    tamanho = len(lista_num)
    if tamanho == 0:
        return "Não tem"
    else: 
        return lista_num[tarmanho-1]


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
print(maiorSalario(lista_num))      