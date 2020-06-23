a=['swades','avengers','transformers']
l=[]
for movies in a:                         #for er next word die indexing bujai eta je kno kicu hte pare
    l.append(a)
print(l)
print()
print()
a=['swades','avengers','transformers']
l=[]
for movies in a:
    l.append(movies)
print(l)
print()
print()
a=['swades','avengers','transformers']
l=[]
for movies in a:
    l.append(movies +'  are good')
print(l)
print()
print()

print([movies+ ' are good.' for movies in a] )
print()
print()
a={"swades":9,"avengers":8,"transformers":4}                   #loop e condition apply krar age 2nd brcet not 3rd
l=[]
for movies in a:
    if a[movies]>6:
        l.append(movies +'  are good')
print(l)
print()
print()
print()
print()
print([movies + '  are good' for movies in a if a[movies]>6])           # must list e convert krte hbe er jonno 3rd bracket dite hbe
