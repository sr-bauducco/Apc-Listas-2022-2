print(f"O programa funciona?")
resposta1 = input().upper()
if resposta1 == "SIM":
    print(f"Você entende o que fez?")
    resposta2 = input().upper()
    if resposta2 == "SIM":
        print(f"Ótimo. Então não mexe!")
    else:
        print(f"Já foi na tutoria?")
        resposta3 = input().upper()
        if resposta3 == "SIM":
            print(f"Choremos!")
        else:
            print(f"Temos um time a disposição!")
else:
    print(f"Você sabe onde está o erro?")
    resposta4 = input().upper()
    if resposta4 == "SIM":
        print(f"Acha que pode solucionar sozinho?")
        resposta5 = input().upper()
        if resposta5 == "SIM":
            print(f"Então mão na massa!")
        else:
            print(f"Já pesquisou no Google?")
            resposta6 = input().upper()
            if resposta6 == "SIM":
                print(f"Já foi na tutoria?")
                resposta7 = input().upper()
                if resposta7 == "SIM":
                    print(f"Choremos!")
                else:
                    print(f"Temos um time a disposição!")
            else:
                print(f"Corre lá então!")
    else:
        print(f"Já foi na tutoria?")
        resposta8 = input().upper()
        if resposta8 == "SIM":
            print(f"Choremos!")
        else:
            print(f"Temos um time a disposição!")

                
        