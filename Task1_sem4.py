# Вычислить число c заданной точностью d 
# Пример: при d = 0.001, π = 3.141.d=0.001,
# π=3.141.﻿﻿

from math import pi

d =  int(input("Введите необходимое количество знаков после точки в числе Пи:\n"))
print(f'число Пи с заданной точностью {d} будет равно {round(pi, d)}')



