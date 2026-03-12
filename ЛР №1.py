spisok1 = [1,2,3,4,5,6,7,8,9,1]
print("Cоздание списка из 10 аргументов. ", spisok1)
print("Вывод предпоследнего, последнего и первого элемента.", spisok1[-2], ",", spisok1[-1], ",", spisok1[0])
spisok1[2] = 1
print("Изменение третьего элемента. ", spisok1[2])
print("Вывод чисел из диапазона. ", spisok1[1:6])
spisok1.append(1)
print("Добавление элемента 1 в конец списка.", spisok1)
spisok1.insert(len(spisok1)//2, 7)
print("Добавление элемента 7 в середину списка. ", spisok1)
print("Вывод количества 1 в списке. ", spisok1.count(1))
spisok2 = spisok1.copy()
spisok1 = spisok1[::-1]
print("Вывод второго списка и инвертированного первого. ", spisok2, ", ", spisok1)