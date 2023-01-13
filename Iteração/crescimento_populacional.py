pa,pb,t1,t2 = input().split()
pa = int(pa)
pb = int(pb)
t1 = float(t1)
t2 = float(t2)

resto = pb-pa
tempo = resto // (t2-t1)
print(tempo)
