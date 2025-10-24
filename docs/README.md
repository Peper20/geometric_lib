# Описание модулей
## _module_ circle
Позволяет вычислить площадь круга и длину окружности

### _func_ area
Вычисляет площадь круга

#### Parameters
r: float
    Радиус круга

#### Returns
float
    Площадь круга: pi * r * r

#### Examples
```
>>> area(3)
28.274333882308138
>>> area(3.5)
38.48451000647496
```

### _func_ perimeter
Вычисляет длину окружности

#### Parameters
r: float
    Радиус окружности

#### Returns
float
    Длина окружности: 2 * pi * r

#### Examples
```
>>> perimeter(5)
31.41592653589793
>>> perimeter(7.7)
48.38052686528282
```

## _module_ rectangle
Позволяет вычислить площадь и периметр прямоугольника

### _func_ area
Вычисляет площадь прямоугольника

#### Parameters
a: float
    Длина одной из сторон

b: float
    Длина смежной к a стороне

#### Returns
float
    Площадь прямоугольника: a * b

#### Examples
```
>>> area(3, 4)
12
>>> area(3.1, 3.5)
10.85
```

### _func_ perimeter
Вычисляет периметр прямоугольника

#### Parameters
a: float
    Длина одной из сторон

b: float
    Длина смежной к a стороне

#### Returns
float
    Периметр прямоугольника: (a + b) * 2

#### Examples
```
>>> perimeter(2, 5)
14
>>> perimeter(2.1, 7.7)
19.6
```

## _module_ square
Позволяет вычислить площадь и периметр квадрата

### _func_ area
Вычисляет площадь квадрата

#### Parameters
a: float
    Длина стороны квадрата

#### Returns
float
    Площадь квадрата: a * a

#### Examples
```
>>> area(3)
9
>>> area(3.5)
12.25
```

### _func_ perimeter
Вычисляет периметр квадрата

#### Parameters
a: float
    Длина стороны квадрата

#### Returns
float
    Периметр квадрата: 4 * a

#### Examples
```
>>> perimeter(3)
12
>>> perimeter(3.7)
14.8
```

## _module_ triangle
Позволяет вычислить площадь и периметр треугольника

### _func_ area
Вычисляет площадь треугольника

#### Parameters
a: float
    Длина стороны треугольника

h: float
    Длина высоты треугольника к стороне a

#### Returns
float
    Площадь треугольника: a * h / 2

#### Examples
```
>>> area(3, 4)
6.0
>>> area(3.7, 4.1)
7.585
```

### _func_ perimeter
Вычисляет периметр треугольника

#### Parameters
a: float
    Длина первой стороны треугольника

b: float
    Длина второй стороны треугольника

c: float
    Длина третьей стороны треугольника

#### Returns
float
    Периметр треугольника: a + b + c

#### Examples
```
>>> perimeter(3, 4, 6)
13
>>> perimeter(3.7, 4.1, 0.3)
8.1
```

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Последние изменения
- `aeb2aec` — add docs to README.md
- `aeb46db` — add docstrings
- `c2ba828` — add triangle.py, fix rectangle perimeter
- `b2bb9e0` — rectangle.py