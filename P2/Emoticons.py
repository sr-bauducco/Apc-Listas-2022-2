def reverso(emoticon):
    reverso=""
    for i in range(len(emoticon)):
         for c in emoticon[2-(i)]:
            reverso= reverso + c
    return reverso

def substitui(frase,reverso,emoticon):
    if len(emoticon) > 1 :
        frase = frase.replace(emoticon,"")
        reverso = reverso(emoticon)
        print(frase.replace(reverso,""))   
    else:
        print(frase.replace(emoticon,""))
    
    

emoticon = input()
vazio=True
frase = " "
while frase != "":
    frase = input()
    substitui(frase,reverso,emoticon)
    frase= frase

    
    
