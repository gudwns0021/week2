print('I love {}for "{}!"'.format('Geeks', 'Geeks'))
print('{0}and{1}'.format('Geeks','Potal'))
print('{1}and{0}'.format('Geeks','Potal'))




import random
x = random.randint(1, 100)
y = random.randint(1, 100)

answer = int('{x} + {y}'.format(x, y))

flag = (answer == (x+y))
print(flag)