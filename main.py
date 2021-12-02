def sekilolustur1(sayi):
    for i in range(sayi):           #1
        for j in range(1,i+2):      #1 2
            print(j,end="")         #1 2 3
        print()
def sekilolustur2(sayi):
    for i in range(sayi):           #*
        for j in range(1,i+2):      #* *
            print("*",end="")       #* * *
        print()
def sekilolustur3(sayi):
    for i in range(sayi):           #* * *
        for j in range(sayi-i):     #* *
            print("*",end="")       #*
        print()
def sekilolustur4(sayi):
    for i in range(sayi):           #***1
        for j in range(sayi-i):     #**12
            print("*",end="")       #*123
        for k in range(1, i + 2):
            print(k, end="")
        print()
def sekilolustur5(sayi):
    for i in range(sayi):
        print(" "*(sayi-i),end="")
        for j in range(1,i+2):      #    1
            print(j,end="")         #  1 2 1
        for j in range(i,0,-1):     #1 2 3 2 1
            print(j,end="")
        print()
#--------------------------------------------------

girilensayi=int(input("kaça kadar devam etsin="))
sekilolustur1(girilensayi)

girilensayi2=int(input("kaç tane yıldız oluşsun ="))
sekilolustur2(girilensayi2)

girilensayi3=int(input("tersten kaç tane yıldız oluşsun ="))
sekilolustur3(girilensayi3)

girilensayi4=int(input("tersten kaç tane yıldız oluşsun ve yanına rakam yazılısn ="))
sekilolustur4(girilensayi4)

girilensayi5=int(input("örüntü kaça kadar gitsin ="))
sekilolustur5(girilensayi5)

#--------------------------------------------------


