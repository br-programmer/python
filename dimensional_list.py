listFruits = [['manzana', 'pera', 'uva'], 
             ['naranja', 'mandarina', 'limon'], 
             ['coco', 'guanabana', 'guineo']]

for fruits in listFruits:
    for fruit in fruits:
        print(fruit)
    print('===========')

listListNumber = [[[1, 2, 3], [9, 11]], [[51]]]
for listNumber in listListNumber:
    for numbers in listNumber:
        print('===========')
        for number in numbers:
            print(number)