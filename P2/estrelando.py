def brilha(branco,preto):
    if branco > 0:
        print(branco* "☆" + preto*"★")
        brilha(branco-1,preto+1)
        print(branco* "☆" + preto*"★")
    else:
        print(branco* "☆" + preto*"★")
        
brilha(5,0)