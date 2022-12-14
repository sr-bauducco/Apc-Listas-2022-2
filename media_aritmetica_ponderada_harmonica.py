num1,num2,num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
letra = input().upper()
if letra == "P":
    print(f"Ponderada")
    peso1,peso2,peso3 = input().split()
    peso1 = int(peso1)
    peso2 = int(peso2)
    peso3 = int(peso3)
    soma = (num1*peso1)+(num2*peso2)+(num3*peso3)
    print(f"{soma/(peso1+peso2+peso3):.2f}")
elif letra == "A":
     print(f"Aritmetica")
     soma = num1+num2+num3
     print(f"{soma/3:.2f}")
elif letra == "H":
    print(f"Harmonica")
    soma =( 1/num1 )+ (1/num2) +( 1/num3)
    print(f"{3/soma:.2f}")
else:
    print(f"Operacao inexistente")
    
    
    
    
    