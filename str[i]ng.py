entry = input()
cont=1
lista=[]
while cont< len(entry):
    if  cont < len(entry):
        lista.append(entry[cont])
        cont+=2
        
lista = str(lista.replace(" ",""))
print(f"{''.join(str(i) for i in lista)}")

