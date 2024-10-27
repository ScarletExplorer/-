money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
mount = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital > 0:
        spend = spend+spend*increase
        money_capital = money_capital + salary - spend
        mount += 1
print("Количество месяцев, которое можно протянуть без долгов:", mount)
