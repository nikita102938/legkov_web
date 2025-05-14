from flask import *
from генератор import *

app = Flask(__name__)


x1v, x2v, x3v, x4v, yr, cl, knopka, li, kc, fl, titlez = '', '', '', '', '', '', '', '', '', 1, ''
list_otv = []


@app.route('/Главная')
def main():
    return render_template('glavn1.html')


@app.route('/Уравнения')
def equations():
    return render_template('yrav.html')


@app.route('/Обучение')
def training():
    return render_template('mater.html')


@app.route('/Калькулятор', methods=['POST', "GET"])
def kalkuleit():
    if request.method == "POST":
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        if a == '': a='a'
        if b == '': b = 'b'
        if c == '': c = 'c'
        return render_template('kalk.html', a='a', b='b', c='c', otv=kalk(a, b, c), fl=1)
    return render_template('kalk.html', a='a', b='b', c='c', fl=0)


@app.route('/Уравнения/<title>', methods=['POST', "GET"])
def maiin(title):
    global cl, yr, x1v, x2v, li, knopka, kc, x3v, x4v, fl, titlez, list_otv
    if request.method == "POST" and fl == 0:
        if title == 'new': title = titlez
        kokr = request.form['select-1']
        if kokr == 'k1':
            try:
                prov = float(request.form['x'])
            except:
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Введено не число',
                                       knopka=knopka, li=li, otv='onn', sp=list_otv, kot=len(list_otv))
        elif kokr == 'k2':
            try:
                prov = [float(request.form['x1']), float(request.form['x2'])]
            except:
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Введено не число',
                                       knopka=knopka, li=li, otv='onn', sp=list_otv, kot=len(list_otv))
        elif kokr == 'k4':
            try:
                prov = [float(request.form['x1']), float(request.form['x2']), float(request.form['x3']),
                        float(request.form['x4'])]
            except:
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Введено не число',
                                       knopka=knopka, li=li, otv='onn', sp=list_otv, kot=len(list_otv))
        if kokr == 'k0':
            if kc == 'Нет корней':
                fl = 1
                if [['Корней нет'], 'v'] not in list_otv: list_otv.append([['Корней нет'], 'v'])
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Верное решение',
                                       knopka=knopka, li=li, otv='ov', sp=list_otv, kot=len(list_otv))
            else:
                if [['Корней нет'], 'l'] not in list_otv: list_otv.append([['Корней нет'], 'l'])
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                       knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
        elif kokr == 'k1':
            if kc == '1 корень':
                x = request.form['x']
                if x1v == x:
                    fl = 1
                    if [['x=' + str(x)], 'v'] not in list_otv: list_otv.append([['x=' + str(x)], 'v'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Верное решение',
                                           knopka=knopka, li=li, otv='ov', sp=list_otv, kot=len(list_otv))
                else:
                    if [['x=' + str(x)], 'l'] not in list_otv: list_otv.append([['x=' + str(x)], 'l'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                           knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
            else:
                if [['x=' + str(request.form['x'])], 'l'] not in list_otv: list_otv.append(
                    [['x=' + str(request.form['x'])], 'l'])
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                       knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
        elif kokr == 'k2':
            if kc == '2 корня':
                x1 = request.form['x1']
                x2 = request.form['x2']
                if (x1v == x1 and x2v == x2) or (x1v == x2 and x2v == x1):
                    fl = 1
                    if [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'v'] not in list_otv: list_otv.append(
                        [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'v'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Верное решение',
                                           knopka=knopka, li=li, otv='ov', sp=list_otv, kot=len(list_otv))
                else:
                    if [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'l'] not in list_otv: list_otv.append(
                        [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'l'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                           knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
            else:
                if [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'l'] not in list_otv: list_otv.append(
                    [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}'], 'l'])
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                       knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
        elif kokr == 'k4':
            if kc == '4 корня':
                x1, x2, x3, x4 = request.form['x1'], request.form['x2'], request.form['x3'], request.form['x4']
                prov = [x1, x2, x3, x4]
                prov.sort()
                xv = [x1v, x2v, x3v, x4v]
                xv.sort()
                pro = [f'x₁={request.form['x1']}', f'x₂={request.form['x2']}', f'x₃={request.form['x3']}',
                       f'x₄={request.form['x4']}']
                if xv == prov:
                    fl = 1
                    if [pro, 'v'] not in list_otv: list_otv.append([pro, 'v'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Верное решение',
                                           knopka=knopka, li=li, otv='ov', sp=list_otv, kot=len(list_otv))
                else:
                    if [pro, 'l'] not in list_otv: list_otv.append([pro, 'l'])
                    return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                           knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
            else:
                if [[f'x₁={request.form['x1']}', f'x₂={request.form['x2']}', f'x₃={request.form['x3']}',
                     f'x₄={request.form['x4']}'], 'l'] not in list_otv: list_otv.append([[f'x₁={request.form['x1']}',
                                                                                          f'x₂={request.form['x2']}',
                                                                                          f'x₃={request.form['x3']}',
                                                                                          f'x₄={request.form['x4']}'],
                                                                                         'l'])
                return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status='Неверное решение',
                                       knopka=knopka, li=li, otv='ol', sp=list_otv, kot=len(list_otv))
        else:
            return 'error, Возникла ошибка. Перезагрузите сайт.'
    else:
        if fl or titlez != title or title == 'new':
            if title == 'new':
                title = titlez
            else:
                titlez = title
            x1v, x2v, x3v, x4v, yr, cl, knopka, li, kc = '', '', '', '', '', '', '', '', ''
            if title == 'Легкие':
                yr = easy()
                cl = 'btn-oval'
                knopka = 'b1'
                li = 'l1'
            elif title == 'Нормальные':
                yr = normal()
                cl = 'btn-oval2'
                knopka = 'b2'
                li = 'l2'
            elif title == 'Сложные':
                yr = hard()
                cl = 'btn-oval3'
                knopka = 'b3'
                li = 'l3'
            if len(yr) == 5:
                kc = '4 корня'
                x1v, x2v, x3v, x4v = yr[1], yr[2], yr[3], yr[4]
            elif len(yr) == 3:
                x1v, x2v = yr[1], yr[2]
                kc = '2 корня'
            else:
                if yr[1] == 'No':
                    kc = 'Нет корней'
                else:
                    kc = '1 корень'
                    x1v = yr[1]
            fl = 0
            list_otv = []
        return render_template('base1.html', title=title, yrav=yr[0], cl=cl, status=f'Вы ещё не решали({x1v} {x2v} {x3v} {x4v})', knopka=knopka, li=li, otv='on', sp=list_otv, kot=len(list_otv))


if __name__ == '__main__':
    app.run(debug=True)
