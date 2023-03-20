summa=0
n = int(input("Введите количество билетов для покупки: "))
while n<0:
    print("Количество билетов не может быть отрицательным")
    n = int(input("Введите количество билетов для покупки: "))
for i in range(1, n + 1):
    l = int(input(f"Введите возраст посетителя: №{i} "))
    while l<=0 or l>100:
        print("Неправильный возраст")
        l = int(input(f"Введите возраст посетителя: №{i} "))
    if 0<=l<18:
        s=0
    elif 18<=l<25:
        s=990
    else:
        s=1390
    summa=summa+s
print("Полная стоимость: ", summa)
if n>3:
    summa=summa*0.9
    print("Cтоимость с учетом скидки: ", summa)