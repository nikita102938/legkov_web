from random import *


def abb(a, s):
    if s == 1:
        if a == 1:
            return 'x²'
        elif a == -1:
            return '-x²'
        return f'{a}x²'
    else:
        if a == 1:
            return '-x²'
        elif a == -1:
            return 'x²'
        return f'{-a}x²'


def bbb(b, s):
    if s == 1:
        if b == 1:
            return 'x'
        elif b == -1:
            return '-x'
        return f'{b}x'
    else:
        if b == 1:
            return '-x'
        elif b == -1:
            return 'x'
        return f'{-b}x'


def easy():
    x1, x2, a = 0, 0, 0
    while x1 == 0: x1 = randint(-10, 10)
    while x2 == 0 or x1 == -x2: x2 = randint(-10, 10)
    while a == 0: a = randint(-3, 3)
    b, c = -(x1 + x2) * a, x1 * x2 * a
    if a == 1:
        yr = 'x²'
    elif a == -1:
        yr = '-x²'
    else:
        yr = str(a) + 'x²'
    if b < 0:
        yr += str(b) + 'x'
    elif b == 1:
        yr += '+x'
    elif b == -1:
        yr += '-x'
    else:
        yr += '+' + str(b) + 'x'
    if c < 0:
        yr += str(c) + '=0'
    else:
        yr += '+' + str(c) + '=0'
    if x1 == x2:
        yrav = (yr, str(x1))
    else:
        yrav = (yr, str(x1), str(x2))
    return yrav


def normal():
    n = randint(1, 12)
    x1, x2, a, b, c = 0, 0, 0, 0, 0
    while a == 0: a = randint(-5, 5)
    if n < 3:
        while x1 == 0: x1 = randint(-10, 10)
        if n == 1:
            x2 = x1
        else:
            while x2 == 0 or x1 == -x2: x2 = randint(-10, 10)
        b, c = -(x1 + x2) * a, x1 * x2 * a
    elif n == 3 or n == 4 or n == 5 or n == 6 or n == 11 or n == 12:
        while x1 == 0: x1 = randint(-10, 9)
        x1 += 0.25 * randint(0, 3)
        if n == 5:
            x2 = x1
        else:
            while x2 == 0: x2 = randint(-10, 9)
        b, c = -(x1 + x2) * a, x1 * x2 * a
    elif n == 7:
        x1 = randint(1, 10)
        x2 = -x1
        c = x1 ** 2 * -a
    elif n == 9 or n == 10:
        while x1 == 0: x1 = randint(-10, 9)
        if n == 10:
            x1 += 0.25 * randint(0, 3)
        b = -x1 * a
    if randint(1, 2) == 1:
        if a == 1:
            yr = 'x²'
        elif a == -1:
            yr = '-x²'
        else:
            yr = str(a) + 'x²'
        if b < 0:
            yr += str(b) + 'x'
        elif b > 0:
            yr += '+' + str(b) + 'x'
        if c < 0:
            yr += str(c)
        elif c > 0:
            yr += '+' + str(c)
        yr += '=0'
    else:
        if b == 0 and c < 0:
            if a == 1:
                yr = f'x²={-c}'
            else:
                yr = f'{a}x²={-c}'
        elif b != 0 and c == 0:
            if randint(1, 2) == 1:
                if a == 1:
                    yr = 'x²='
                elif a == -1:
                    yr = '-x²='
                else:
                    yr = f'{a}x²='
                if b == 1:
                    yr += '-x'
                elif b == -1:
                    yr += 'x'
                else:
                    yr += f'{-b}x'
            else:
                if b == 1:
                    yr = 'x='
                elif b == -1:
                    yr = '-x='
                else:
                    yr = f'{b}x='
                if a == 1:
                    yr += '-x²'
                elif a == -1:
                    yr += 'x²'
                else:
                    yr += f'{-a}x²'
        elif b != 0 and c != 0:
            if a > 0 and b > 0 and c > 0:
                yr = f'{abb(a, 1)}+{bbb(b, 1)}+{c}=0'
            elif a < 0 and b < 0 and c < 0:
                yr = f'{abb(a, 1)}{bbb(b, 1)}{c}=0'
            elif a > 0 and b < 0 and c < 0:
                yr = f'{abb(a, 1)}={bbb(b, 2)}+{-c}'
            elif a < 0 and b > 0 and c > 0:
                yr = f'{bbb(b, 1)}+{c}={abb(a, 2)}'
            elif a > 0 and c > 0 and b < 0:
                yr = f'{abb(a, 1)}+{c}={bbb(b, 2)}'
            elif a > 0 and b > 0 and c < 0:
                yr = f'{abb(a, 1)}+{bbb(b, 1)}={-c}'
            elif b > 0 and a < 0 and c < 0:
                yr = f'{bbb(b, 1)}={abb(a, 2)}+{-c}'
            elif c > 0 and b < 0 and a < 0:
                yr = f'{c}={abb(a, 2)}+{bbb(b, 2)}'
        else:
            yr = f'{abb(a, 1)}=0'
    if int(x1) == x1: x1 = int(x1)
    if int(x2) == x2: x2 = int(x2)
    if x1 == x2:
        yrav = (yr, str(x1))
    else:
        yrav = (yr, str(x1), str(x2))
    return yrav


def hard():
    if randint(1, 5) in [1, 5]:
        return normal()
    else:
        ww = randint(1, 3)
        if ww == 1:
            a, b, c = 0, 0, 0
            while a == 0: a = randint(-5, 5)
            while b == 0: b = randint(-15, 15)
            cx = round((b ** 2) / (4 * a))
            while c == 0 and a > 0: c = randint(cx + 1, cx + 10)
            while c == 0 and a < 0: c = randint(cx - 10, cx - 1)
            yr = abb(a, 1)
            if b < 0:
                yr += bbb(b, 1)
            else:
                yr += f'+{bbb(b, 1)}'
            if c > 0:
                yr += f'+{c}=0'
            else:
                yr += f'{c}=0'
            yrav = (yr, 'No')
            return yrav
        elif ww == 2:
            a, b, c, x1, x2, z = 0, 0, 0, 0, 0, 0
            www = randint(1, 10)
            while a == 0: a = randint(-3, 3)
            if www == 1 or www == 2:
                z1, z2 = randint(-20, -1), randint(-20, -1)
                b = -a * (z1 + z2)
                c = a * z1 * z2
                yr = abb(a, 1)[:-1] + '⁴'
                if b > 0:
                    yr += '+' + bbb(b, 1) + '²'
                else:
                    yr += bbb(b, 1) + '²'
                if c > 0:
                    yr += '+' + str(c) + '=0'
                else:
                    yr += str(c) + '=0'
                return (yr, 'No')
            elif www in [3, 4, 5]:
                x1 = randint(-6, -1)
                x3 = randint(1, 10)
                x4 = -x3
                b = -a * (x1 + x3 ** 2)
                c = a * x1 * x3 ** 2
                yr = abb(a, 1)[:-1] + '⁴'
                if b > 0:
                    yr += '+' + bbb(b, 1)[:-1] + '²'
                else:
                    yr += bbb(b, 1) + '²'
                if c > 0:
                    yr += '+' + str(c) + '=0'
                else:
                    yr += str(c) + '=0'
                return (yr, str(x3), str(x4))
            else:
                x1 = randint(1, 10)
                x2 = randint(1, 10)
                b = -a * (x1 ** 2 + x2 ** 2)
                c = a * x2 ** 2 * x1 ** 2
                yr = abb(a, 1)[:-1] + '⁴'
                if b > 0:
                    yr += '+' + bbb(b, 1) + '²'
                else:
                    yr += bbb(b, 1) + '²'
                if c > 0:
                    yr += '+' + str(c) + '=0'
                else:
                    yr += str(c) + '=0'
                if x1 == x2:
                    return (yr, str(x1), str(-x1))
                else:
                    return (yr, str(x1), str(-x1), str(x2), str(-x2))
        elif ww == 3:
            a, b, c, x1, x2, z = 0, 0, 0, 0, 0, 0
            while a == 0: a = randint(-3, 3)
            while x1 == 0: x1 = randint(-10, 10)
            while x2 == 0: x2 = randint(-10, 10)
            numm = randint(1, 10)
            if randint(1, 2) == 1: numm *= -1
            xp1 = x1 + numm
            xp2 = x2 + numm
            if numm > 0:
                x = f'(x+{numm})'
            else:
                x = f'(x{numm})'
            b = -a * (xp1 + xp2)
            c = a * xp1 * xp2
            if a == 1:
                yr = f'{x}²'
            elif a == -1:
                yr = f'-{x}²'
            else:
                yr = f'{a}{x}²'
            if b == 1:
                yr += x
            elif b == 1:
                yr += f'-{x}'
            elif b < 0:
                yr += f'{b}{x}'
            else:
                yr += f'+{b}{x}'
            if c > 0:
                yr += f'+{c}=0'
            else:
                yr += f'{c}=0'
            if x1 == x2:
                return (yr, str(x2))
            else:
                return (yr, str(x1), str(x2))


def kalk(a, b, c):
    if a == 'a': a = 1
    if b == 'b': b = 1
    if c == 'c': c = 1
    try:
        a, b, c = int(a), int(b), int(c)
    except:
        return ['Введено не число']
    yr = ''
    if a == 0 and b == 0 and c == 0:
        return ['ВЫ ДУМАЕТЕ ЭТО СМЕШНО?!']
    if a == 0:
        if b == 1:
            yr = 'x'
        else:
            yr = f'{b}x'
        if c > 0:
            yr += f'+{c}'
        elif c < 0:
            yr += f'{c}'
        yr += '=0'
    elif b == 0:
        if a == 1:
            yr = 'x²'
        else:
            yr = f'{a}x²'
        if c > 0:
            yr += f'+{c}'
        elif c < 0:
            yr += f'{c}'
        yr += '=0'
    elif c == 0:
        if a == 1:
            yr = 'x²'
        else:
            yr = f'{a}x²'
        if b == 1:
            yr += '+x=0'
        elif b == -1:
            yr += '-x=0'
        elif b > 0:
            yr += f'+{b}x=0'
        else:
            yr += f'{b}x=0'
    else:
        if a == 1:
            yr = 'x²'
        else:
            yr = f'{a}x²'
        if b == 1:
            yr += '+x'
        elif b == -1:
            yr += '-x'
        elif b > 0:
            yr += f'+{b}x'
        else:
            yr += f'{b}x'
        if c > 0:
            yr += f'+{c}=0'
        else:
            yr += f'{c}=0'
    otv = [yr]
    if a == 0 and b != 0 and c != 0:
        otv.append('Так как a=0, то уравнение линейное.')
        otv.append(f'{b}x={-c}')
        if b != 1: otv.append(f'x={-c}/{b}')
        if len(str(abs(abs(-c / b) - abs(round(-c / b))))) < 4:
            otv.append(f'x={-c / b}')
            otv.append(f'Ответ: {-c / b}')
        else:
            otv.append(f'Ответ: {-c}/{b}')
    elif a != 0 and b == 0 and c != 0:
        otv.append(f'x²={-c}/{a}')
        if -c / a < 0:
            otv.append(f'Так как квадрат числа отрицателен, то x не существует')
        else:
            otv.append(f'x=±√({-c}/{a})')
            if len(str((-c / a) ** 0.5)) <= 5:
                otv.append(f'x=±{(-c / a) ** 0.5}')
                otv.append(f'Ответ: ±{(-c / a) ** 0.5}')
            else:
                otv.append(f'Ответ: ±√({-c}/{a})')
    elif a != 0 and c == 0 and b != 0:
        if b > 0:
            otv.append(f'x({a}x+{b})=0')
            otv.append(f'{a}x+{b}=0 или x=0')
        else:
            otv.append(f'x({a}x{b})=0')
            otv.append(f'{a}x{b}=0 или x=0')
        otv.append(f'x={-b}/{a}')
        if len(str(-b / a)) < 5:
            otv.append(f'x={-b / a}')
            otv.append(f'Ответ: x=0, x={-b / a}')
        else:
            otv.append(f'Ответ: x=0, x={-b}/{a}')
    elif (a != 0 and b == 0 and c == 0) or (a == 0 and b != 0 and c == 0):
        otv.append('x=0')
        otv.append('Ответ: x=0')
    else:
        otv.append('Найдем дискриминант')
        otv.append(f'D=b²-4ac={b}²-4*({a})*({c})={b ** 2 - 4 * a * c}')
        if b ** 2 - 4 * a * c < 0:
            otv.append('Так как D<0, то уравнение не имеет корней')
            otv.append('Ответ: Корней нет')
        elif b ** 2 - 4 * a * c == 0:
            otv.append('Так как D=0, то уравнение имеет 1 корень:')
            if len(str(-b/(2*a))) > 5:
                otv.append(f'x=-b/2a={-b}/{2*a}')
                otv.append(f'Ответ: {-b}/{2*a}')
            else:
                otv.append(f'x=-b/2a={-b}/{2 * a}={-b/(2*a)}')
                otv.append(f'Ответ: {-b/(2*a)}')
        else:
            otv.append('Так как D=0, то уравнение имеет 2 корня:')
            d = b**2 -4*a*1
            if len(str((d)**0.5)) < 5:
                if len(str((-b + d ** 0.5)/(2*a))) < 7:
                    otv.append(f'x₁=({-b}+√{d})/{2 * a}={(-b+d**0.5)/(2*a)}')
                    x1 = f'{(-b+d**0.5)/(2*a)}'
                else:
                    otv.append(f'x₁=({-b}+√{d})/{2*a}={-b+d**0.5}/{2*a}')
                    x1 = f'{-b+d**0.5}/{2*a}'
                if len(str((-b - d ** 0.5) / (2 * a))) < 7:
                    x2 = f'{(-b-d**0.5)/(2*a)}'
                    otv.append(f'x₂=({-b}-√{d})/{2 * a}={(-b-d**0.5)/(2*a)}')
                else:
                    x2 = f'{-b+d**0.5}/{2*a}'
                    otv.append(f'x₂=({-b}-√{d})/{2 * a}={-b-d**0.5}/{2*a}')
                otv.append(f'Ответ: x₁={x1}; x₂={x2}')
            else:
                otv.append(f'x=({-b}±√{d})/{2*a}')
                otv.append(f'Ответ: ({-b}±√{d})/{2*a}')
    return otv
