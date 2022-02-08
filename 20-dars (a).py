

def katta_harf(nom):
    nom=nom[:]
    for n in range(len(nom)):
        nom[n]=nom[n].title()
    return nom


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar=katta_harf(ismlar)
print(yangi_ismlar)