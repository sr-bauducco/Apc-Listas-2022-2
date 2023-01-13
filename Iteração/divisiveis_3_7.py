n = int(input())

comuns = []
while n >= 0:
    if (n%3==0 and n%7==0):
        comuns.append(n)
    n = n-1
comuns = sorted(comuns)
print(" ".join(map(str,comuns)))

    
    