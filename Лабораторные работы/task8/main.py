money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while (money_capital+salary) >= spend:
   spend += spend*increase
   month += 1
   money_capital -= spend - salary #TODO Оформить решение

print(month)
