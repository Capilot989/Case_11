import turtle as trt
import runnng_square as RS
import mink_curve as MC
import levi as LV
import koch as KC
import ice_fract_1 as IF1
import ice_fract_2 as IF2
import carpet as CR
import branch as BR
import bin_tree as BT
import H_fractale as H
import vicsek as VC

def print_menu():
    print('=====МЕНЮ ВЫБОРА ФРАКТАЛА====\n\n')
    print(
        'Доступные фракталы:\n'
        '1: Бегущий квадрат\n'
        '2: Бинарное дерево\n'
        '3: Ветка\n'
        '4: Кривая Коха\n'
        '5: Снежинка Коха\n'
        '6: Кривая Минковского\n'
        '7: Ледяной фрактал (Версия 1)\n'
        '8: Ледяной фрактал (Версия 2)\n'
        '9: Кривая Леви\n'
        '10: Ковер\n'
        '11: H-фрактал\n'
        '12: Фрактал Вичека\n'
    )
def available_fractales(
        size, depth, angle,
        koef, total, x, y,
        width, height
):
    fractales = {
        1: lambda: RS.running_sq(size, angle, koef, depth),
        2: lambda: BT.tree(size, depth, total),
        3: lambda: BR.branch(depth, size, total),
        4: lambda: KC.koch(size, depth, total),
        5: lambda: KC.snowflake(size, depth, total),
        6: lambda: MC.mink_curve(depth, size, total),
        7: lambda: IF1.ice_fract(depth, size, total),
        8: lambda: IF2.ice_fract_2(depth, size, total),
        9: lambda: LV.levi(size, depth, total),
        10: lambda: CR.sierpinski_carpet(x, y, size, depth, total),
        11: lambda: H.H_recursive(x, y, width, height, depth, 0, total),
        12: lambda: VC.vicsek(x, y, size, depth, total)
    }
    return fractales



def determine_total(choise: int, depth: int) -> int:
    totals = {
        2: BT.count_segments(depth),
        3: BR.count_branches(depth),
        4: KC.count_segments(depth),
        5: KC.count_segments(depth) * 3,
        6: MC.count_segments(depth),
        7: IF1.count_segments(depth),
        8: IF2.count_segments(depth),
        9: LV.count_segments(depth),
        10: CR.count_squares(depth),
        11: H.count_H_segments(depth),
        12: VC.count_squares(depth)
    }
    return totals[choise]

def main():
    size = 0
    angle = 15
    koef = 0.15
    total = 10000
    x = 0
    y = 0
    width = 0
    height = 0

    print_menu()
    while True:
        choise = int(input('Введите номер выбранного фрактала: '))
        if 1 <= choise <= 12:
            break

    depth = int(input('Введите глубину рекурсии: '))

    if choise == 1:
        angle = int(input('Введите угол поворота квадратов: '))
        koef = float(input('Введите коэфициент уменьшения квадратов (0:1): '))

    if choise == 11:
        height = int(input('Введите высоту фрактала: '))
        width = int(input('Введите ширину фрактала: '))
    else:
        size = int(input('Введите размер фрактала: '))

    if 10 <= choise <= 12:
        x = int(input('Введите координату x для начала фрактала: '))
        y = int(input('Введите координату y для начала фрактала: '))

    if choise != 1:
        total = determine_total(choise, depth)

    fractales = available_fractales(
        size, depth, angle,
        koef, total,
        x, y, width, height
    )

    func = fractales.get(choise)
    func()


if __name__ == '__main__':
    trt.tracer(False)
    main()
    trt.update()
    trt.done()
