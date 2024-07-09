my_dict = {'Anna':1997, 'Arthur':568, 'Kaera':561}
print('Dict:', my_dict)
print('Existing value:', my_dict['Kaera'])
print(my_dict.get('Agrona', 'Not existing value'))
my_dict.update({'Agrona': -1589,
                'Sylvie': 572})
print('Deleted value:', my_dict.pop('Anna'))
print('Modified dictionary:', my_dict)

my_set = {1, 1, 2, 2, 3, True, False}
print('Set:', my_set)
my_set.add(5)
my_set.add('str')
my_set.remove(1)
print('Modified set:', my_set)