
# Рисуем фигуры
print('ФИГУРА - A')
print('------------------------------------------')
h = 0
for h in range(0, 7):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        if w in range(1, h + 1) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    for w in range(h):
        if w in range(h - 1) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
print('------------------------------------------')
print('ФИГУРА - B')
print('------------------------------------------')
for h in range(0, 7):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for y in range(0, h):
        print('*', end=' ')
    print()
print('------------------------------------------')
print('ФИГУРА - C')
print('------------------------------------------')
for h in range(0, 7):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for y in range(0, h):
        print('*', end=' ')
    print()
for h in range(5, -1, -1):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        if w in range(1, h + 1) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    for w in range(h):
        if w in range(h - 1) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
print('------------------------------------------')
print('ФИГУРА - D')
print('------------------------------------------')
for h in range(0, 7):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for y in range(0, h):
        print('*', end=' ')
    print()
for h in range(5, -1, -1):
    for i in range(h, 6):
        print(' ', end=' ')
    for w in range(0, h + 1):
        if w in range(1, h) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    for w in range(h):
        if w in range(0, h - 1) and h != 6:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()

print('------------------------------------------')

user_number = int(input('Введите пожалуйста высоту(Биссектрису):'))

print('------------------------------------------')
print('Tреугольник 1')
print('------------------------------------------')
for h in range(0, user_number):
    for i in range(h + 1, user_number):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    for y in range(0, h):
        print('*', end=' ')
    print()

print('------------------------------------------')
print('Tреугольник 2')
print('------------------------------------------')

for h in range(user_number, -1, -1):
    for i in range(h, user_number):
        print(' ', end=' ')
    for w in range(0, h - 1):
        print('*', end=' ')
    for y in range(0, h):
        print('*', end=' ')
    print()

print('------------------------------------------')
print('Tреугольник 3')
print('------------------------------------------')

for h in range(user_number, -1, -1):
    for i in range(h, user_number):
        print('*', end=' ')
    print()
for w in range(1, user_number):
    for u in range(w, user_number):
        print('*', end=' ')
    print()

print('------------------------------------------')
print('Tреугольник 4')
print('------------------------------------------')

for h in range(0, user_number):
    for i in range(h + 1, user_number):
        print(' ', end=' ')
    for w in range(0, h + 1):
        print('*', end=' ')
    print()
for h in range(user_number - 1, -1, -1):
    for i in range(h, user_number):
        print(' ', end=' ')
    for w in range(0, h):
        print('*', end=' ')
    print()
print('------------------------------------------')



