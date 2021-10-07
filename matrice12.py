matrice=[]
n=int(input('Introdueti numarul de linii:'))
if ((n>=2) and (n<=10)):
    print("Introduceti elementele matricei:")
    for l in range(0,n):
        l=[]
        for e in range(0,n):
            e=int(input())
            l.append(e)
        matrice.append(l)
    print("Elementele matricei sunt", matrice)
    d_principala=[]    
    d_secundara=[]
    mai_sus_d_principala=[]
    mai_jos_d_principala=[]
    mai_sus_d_secundara=[]
    mai_jos_d_secundara=[]
    #a
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i==j:
                d_principala.append(matrice[i][j])
    print(f"Elementele diagonalei principale sunt: {d_principala}")
    print("Suma diagonalei principale=", sum(d_principala))
    #b
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if (i+j)==(len(matrice)-1):
                d_secundara.append(matrice[i][j])
    print(f"Elementele diagonalei secundare sunt: {d_secundara}")
    print("Suma diagonalei seundare =", sum(d_secundara))
    #c
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i<j:
                mai_sus_d_principala.append(matrice[i][j])
    print(f"Elementele mai sus de diagonala principala sunt: {mai_sus_d_principala}")
    print("Suma elementelor mai sus de diagonala principala =", sum(mai_sus_d_principala))
    #d
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if i>j:
                mai_jos_d_principala.append(matrice[i][j])
    print(f"Elementele mai jos de diagonala principala sunt: {mai_jos_d_principala}")
    print("Suma elementelor mai jos de diagonala principala =", sum(mai_jos_d_principala))
    #e
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if (i+j)<(len(matrice)-1):
                mai_sus_d_secundara.append(matrice[i][j])
    print(f"Elementele mai sus de diagonala secundara sunt: {mai_sus_d_secundara}")
    print("Suma elementelor mai sus de diagonala secundara =", sum(mai_sus_d_secundara))
    #f
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            if (i+j)>(len(matrice)-1):
                mai_jos_d_secundara.append(matrice[i][j])
    print(f"Elementele mai sus de diagonala secundara sunt: {mai_jos_d_secundara}")
    print("Suma elementelor mai sus de diagonala secundara =", sum(mai_jos_d_secundara))
else:
    print("Dati un numar cuprins intre 2 si 10")