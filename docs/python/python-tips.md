---
title: "Python Tipps"
---

```py title="Global Imports and Variables"
import math
from datetime import date


n = 10_000_000  # n = 10000000  # comfortable reading with `_`
a, b = 10, 5
f = 234.606
name = "Jimmy"
my_date = date(2024, 5, 24)
```

## Type Annotation

[//]: # (--8<-- [start:type-annotation])

```py
def myprint(name: str) -> None:
    print(name)
```

!!! info

    Bei der Type Annotation muss es sich nicht zwingend um einen ganz bestimmten Datentyp, wie `#!py str` oder `#!py int` handeln, sondern kann auch etwas abstrakteres sein, wie zum Beispiel `#!py Iterable` aus `collections.abc`:
    
    - Abstract Base Classes for Containers: [https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes){:target="_blank"}

[//]: # (--8<-- [end:type-annotation])

## f-String

### Basic

```py
print(f"10 + 5 = {a + b}")  # 10 + 5 = 15
```

### Thousends Seperator

```py
print(n)         # 10000000
print(f"{n:_}")  # 10_000_000
print(f"{n:,}")  # 10,000,000
```

> support only `_` and `,`

### Special Formatting

```py
print(f'{f:.2f}')  # 234.61
```

```py
print(f"{a + b = }")    # a + b = 15
print(f"{a * b = }")    # a * b = 50
print(f"{bool(a) = }")  # bool(a) = True
print(f"{name = }")     # name = 'Jimmy'
```

```py
print(f'{my_date:%d.%m.%Y}')  # 24.05.2024
```

### Text Alignment

use a `|` for a better visualisation

```py
print(f"|{name:>30}|")    # |                         Jimmy|
print(f"|{name:<30}|")    # |Jimmy                         |
print(f"|{name:^30}|")    # |            Jimmy             |
print(f"|{name:-^30}|")   # |------------Jimmy-------------|
print(f"|{name:*>30}|" )  # |*************************Jimmy|
```

## Math

operation for two integers and their return type:

- `+`, `-`, `*` and `//` return `#!py int`
- `/` return `#!py float`.

```py
print(f"{a + b:>3} {type(a + b)}")    #  15 <class 'int'>
print(f"{a - b:>3} {type(a - b)}")    #  -5 <class 'int'>
print(f"{a * b:>3} {type(a * b)}")    #  50 <class 'int'>
print(f"{a / b:>3} {type(a / b)}")    # 0.5 <class 'float'>
print(f"{a // b:>3} {type(a // b)}")  #   0 <class 'int'>
```

### Rounding to integer

```py
print(f)              # 234.606
print(int(f))         # 234
print(math.floor(f))  # 234
print(math.ceil(f))   # 235
```
