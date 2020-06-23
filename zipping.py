list1=[1,2,3,4]
list2=['joy','kou','loi','pol']
super=list(zip(list1,list2))
print(super)
sup1=list( zip(*super) )
print(sup1)

books=['physics','chemistry','math']
number=[3,4,6]
price=[9,8,6]

sentences=[]
for (a,b,c) in zip (books,number,price):
    a,b,c= str(a),str(b),str(c)
    sentence='rahim bought  '+ a+'    '+ b+  ' at $ ' +c   +' each.'
    sentences.append(sentence)

print(sentences)