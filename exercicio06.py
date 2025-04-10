dezevinte=0
qlqrnum=0
for i in range(10):
    num=int(input("Digite um número: "))
    if num>=10 and num<=20:
        dezevinte+=1
    else:
        qlqrnum+=1
print(f"Numeros entre 10 e vinta{dezevinte}, numeros que não estão entre 10 e vinte{qlqrnum}.")

"""dezevinte=0
qlqrnum=0
for i in range(10):
    num=int(input("Digite um número: "))
    if num>=10 and num<=20:
        dezevinte+=1
qlqrnum = i - dezevinte
print(f"Numeros entre 10 e 20 {dezevinte}, numeros que não estão entre 10 e 20 {qlqrnum}.")"""