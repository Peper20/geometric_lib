def area(a: float, b: float) -> float:
    '''
    Вычисляет площадь прямоугольника

    Parameters
    ----------
    a: float
        Длина одной из сторон
    b: float
        Длина смежной к a стороне

    Returns
    -------
    float
        Площадь прямоугольника: a * b

    Examples
    --------
    >>> area(3, 4)
    12
    >>> area(3.1, 3.5)
    10.85
    '''
    return a * b


def perimeter(a: float, b: float) -> float:
    '''
    Вычисляет периметр прямоугольника

    Parameters
    ----------
    a: float
        Длина одной из сторон
    b: float
        Длина смежной к a стороне

    Returns
    -------
    float
        Периметр прямоугольника: (a + b) * 2

    Examples
    --------
    >>> perimeter(2, 5)
    14
    >>> perimeter(2.1, 7.7)
    19.6
    '''
    return (a + b) * 2
