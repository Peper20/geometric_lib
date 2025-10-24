def area(a: float) -> float:
    '''
    Вычисляет площадь квадрата

    Parameters
    ----------
    a: float
        Длина стороны квадрата

    Returns
    -------
    float
        Площадь квадрата: a * a

    Examples
    --------
    >>> area(3)
    9
    >>> area(3.5)
    12.25
    '''
    return a * a


def perimeter(a: float) -> float:
    '''
    Вычисляет периметр квадрата

    Parameters
    ----------
    a: float
        Длина стороны квадрата

    Returns
    -------
    float
        Периметр квадрата: 4 * a

    Examples
    --------
    >>> perimeter(3)
    12
    >>> perimeter(3.7)
    14.8
    '''
    return 4 * a
