from random import randint
import time
print('Игра "Кубики"')
print()#Спрашиваем у пользователей, как их зовут и сколько "бросков" сделают
while True: #Предохраняем от ввода одинаковых имён игроков
    p1 = input('Введите имя первого играющего: ')
    p2 = input('Введите имя второго играющего: ')
    if p1 != p2:
        break
    else:
        print('Имена игроков не могут быть одинаковыми!')
povt = int(input('Сколько партий?(рек. нечётное кол-во): '))#Кол-во партий
w1 = 0  #Инициализируем счётчики побед, ничьей и проигрышей
w2 = 0
fr = 0
print()
print('Игра началась!')
print()
for n in range(povt): #Начинаем основной цикл игры, симулирующий игровой процесс
    time.sleep(1)
    print('Партия', n + 1)
    print('Бросает', p1) #Бросок первого игрока
    time.sleep(3)
    n11 = randint(1, 6) #Результат на первом кубике
    n12 = randint(1, 6) #рез-тат на втором
    sum1 = n11 + n12    #Сумма результатов броска для сравнения
    print('[', n11, ']', '[', n12, ']', sep = '') #Показываем результат 1
    time.sleep(1)
    print('Бросает', p2)#Бросок второго игрока
    time.sleep(3)
    n21 = randint(1, 6) #Рез-тат на первом
    n22 = randint(1, 6) #рез-тат на втором
    sum2 = n21 + n22    #Находим сумму результатов бросков
    print('[', n21, ']', '[', n22, ']', sep = '')#Показываем результат 2
    time.sleep(1)
    if sum1 > sum2:         #Сравниваем суммы результатов бросков
        print('Выиграл', p1)
        w1 += 1
    elif sum2 > sum1:
        print('Выиграл', p2)
        w2 += 1
    else:
        print('Ничья!')
        fr += 1
    print()
if w1 > w2:    #Сравниваем и выводим кол-во выигранных рпартий и ничьих
    print('Счёт ', w1, ':', w2, ' в пользу ', p1, sep = '')
    print('Ничьих:', fr)
elif w2 > w1:
    print('Счёт ', w1, ':', w2, ' в пользу ', p2, sep = '')
    print('Ничьих:', fr)
else:
    print('Ничья! Счёт ', w1, ':', w2, sep = '')
    print('Ничьих:', fr)
print()
e = input('Press "ENTER" to continue...')
    
        
