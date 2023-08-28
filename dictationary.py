car={
'brand':'Toyota',
'Price': 30000000,
'Yop':2015,
'name':'Prado',
'Fuel':'Petrol'
}

print(car.get('name'))

if 'Brand' in car:
    print('Toyota is the good one')
elif 'Yop' in car: 
    print(car['Yop'])
    
else:
    print('huu ni uongo')

car.update({'garage':'Extenal garage'})
print(car['garage'])

car['speed']=120
car.pop('Yop')
#car.clear()
print(car)

