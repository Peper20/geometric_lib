import math


def area(r: float) -> float:
    '''
    Вычисляет площадь круга

    Parameters
    ----------
    r: float
        Радиус круга

    Returns
    -------
    float
        Площадь круга: pi * r * r

    Examples
    --------
    >>> area(3)
    28.274333882308138
    >>> area(3.5)
    38.48451000647496
    '''
    return math.pi * r * r


def perimeter(r: float) -> float:
    '''
    Вычисляет длину окружности

    Parameters
    ----------
    r: float
        Радиус окружности

    Returns
    -------
    float
        Длина окружности: 2 * pi * r

    Examples
    --------
    >>> perimeter(5)
    31.41592653589793
    >>> perimeter(7.7)
    48.38052686528282
    '''
    return 2 * math.pi * r
