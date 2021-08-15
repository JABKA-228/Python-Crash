pizza=['Margherita', 'Marinara', 'Quattro Stagioni']
for i in pizza:
    print('I like', i, 'pizza!')
print('I really love pizza!')
friend_pizzas=pizza[:]
pizza.append('Frutti di Mare')
friend_pizzas.append('Carbonara')
print('\nMy favorite pizzas are:')
for i in pizza:
    print(i)
print("\nMy friend's favorite pizzas are:")
for y in friend_pizzas:
    print(y)
