s = input()

for c in range(len(s)):
    if c%2 >0:
        print(s[c].replace(" ",""),end="",sep="")
    else:
        pass