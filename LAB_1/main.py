
import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        buf = False
        while (buf != True):
            print(prompt)
            coef_str = input()
            try:
                float(coef_str)
                buf = True
            except ValueError:
                buf = False
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней биквадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        root = -b / (2.0 * a)
        if root >= 0.0:
            Root1 = -math.sqrt(root)
            Root2 = math.sqrt(root)
            result.append(Root1)
            result.append(Root2)
        elif root < 0.0:
            return result

    elif D < 0.0:
        return result

    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0 * a)
        root2 = (-b - sqD) / (2.0 * a)

        if root1 >= 0.0:
            if math.sqrt(root1) == 0.0:
                Root1 = math.sqrt(root1)
                result.append(Root1)
            elif math.sqrt(root1) != 0.0:
                Root1 = -math.sqrt(root1)
                Root2 = math.sqrt(root1)
                result.append(Root1)
                result.append(Root2)

        if root2 >= 0.0:
            if math.sqrt(root2) == 0.0:
                Root5 = math.sqrt(root2)
                result.append(Root5)
            elif math.sqrt(root2) != 0.0:
                Root3 = -math.sqrt(root2)
                Root4 = math.sqrt(root2)
                result.append(Root3)
                result.append(Root4)

    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    while a == 0.0:
        print('a не равно нулю')
        a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        if (roots[0] == 0.0) or (roots[0] == -0.0):
            print('Один корень: 0.0')
        elif roots[0] != 0.0:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, {}'.format(roots[0], roots[1], roots[2], roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4
