christianNames=[]
boysChristianNames=['Elisha', 'Isack', 'Noah']
girlsChristianNames=['Mirian', 'Rebeka', 'Devotha']
#apending sub list in a superlist
christianNames.append(boysChristianNames)
christianNames.append(girlsChristianNames)
christianNames[2:4]=['Asha','Juma' , 'Amina']
christianNames.remove('Juma')
christianNames.insert(3, 'Solomon')
christianNames.pop()
print(christianNames)
