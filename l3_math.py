from decimal import Decimal

P1=3.1415926
PI=Decimal(P1)
radius=(input('Введите радиус круга в сантиметрах: '))
r=Decimal(radius)
print(f'Длина окружности с заданным радиусом в сантиметрах {2*PI*r}, в метрах {PI*r/50}')

