
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
int_money = int(input("Введите планируемую сумму вклада: "))
int_month = int(input("Введите планируемый срок вклада, месяцев: "))
percent: list[float] = list(per_cent.values())
percent_m = [i / 12 * int_month  for i in percent]
deposit = [i * int_money/100 for i in percent_m]
print(deposit)
sum = [i * int_money/100+int_money for i in percent_m]
max_sum = round(max(sum),2)
max_deposit = round(max(deposit),2)
print("Наилучший результат вложения за указанный срок: ", max_sum, 'руб.')
print("Ваша прибыль составит: ", max_deposit, 'руб.')


