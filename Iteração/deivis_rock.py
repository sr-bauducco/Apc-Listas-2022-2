def media(dinheiros):
    soma=0.00
    num = [float(i) for i in dinheiros]
    if len(num) == 0:
        return "0.00"
    else:
        media = sum(num)/ len(dinheiros)
    return  int(media)


amigos,ingresso = input().split()
ingresso = int(ingresso)
amigos = int(amigos)
dinheiros = []
parada = 0
while parada < amigos:
    dinheiros.append(input())
    parada = parada+1
    
print(f"media: {media(dinheiros):.0f}")
media = int(media(dinheiros))
if media >= ingresso:
    print(f"o rock reinara mais uma vez")
else:
    print(f"rockeiros trabalhando ja")
    
