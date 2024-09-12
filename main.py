spb_price = 50_000
msc_price = 80_000
ekb_price = 40_000

print("Приветствую в системе помощи туриста!")
print("Доступные города: spb, msc, ekb")
city = input("Введите город: ")
count = int(input("Введите количество туристов: "))

if city == "spb":
    total = spb_price * count
elif city == "msc":
    total = msc_price * count
elif city == "ekb":
    total = ekb_price * count
else:
    print("Такого города нет")
    exit()

print("Итоговый бюджет: " + str(total))
