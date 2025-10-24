def area(a: float, h: float) -> float:
    '''
    Вычисляет площадь треугольника

    Parameters
    ----------
    a: float
        Длина стороны треугольника
    h: float
        Длина высоты треугольника к стороне a

    Returns
    -------
    float
        Площадь треугольника: a * h / 2

    Examples
    --------
    >>> area(3, 4)
    6.0
    >>> area(3.7, 4.1)
    7.585
    '''
    return a * h / 2


def perimeter(a: float, b: float, c: float) -> float:
    '''
    Вычисляет периметр треугольника

    Parameters
    ----------
    a: float
        Длина первой стороны треугольника
    b: float
        Длина второй стороны треугольника
    c: float
        Длина третьей стороны треугольника

    Returns
    -------
    float
        Периметр треугольника: a + b + c

    Examples
    --------
    >>> perimeter(3, 4, 6)
    13
    >>> perimeter(3.7, 4.1, 0.3)
    8.1
    '''
    return a + b + c
