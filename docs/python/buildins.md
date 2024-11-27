---
title: "Python: buildins"
---

## zip()

```py
names = ["Bob", "Jim"]
ages = [53, 28]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

## enumerate()

Wenn zusätzlich ein Index benötigt wird

```py
tasks = [
    'Wäsche aufhängen',
    'Küche aufräumen',
    'Müll raus bringen',
]

for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")
```

## sorted()

```py
peoples = [
    {'name': 'Bob', 'age': 45},
    {'name': 'Kim', 'age': 51},
    {'name': 'Louis', 'age': 18},
]

sorted_peoples = sorted(peoples, key=lambda person: person['age'], reverse=True)

print(sorted_peoples)
```

## @decorator

```py
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # start timer
        result = func(*args, **kwargs)  # call decorated function
        end_time = time.time()  # stop timer
        print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec.")
        return result
    
    return wrapper
```

```py
@timer
def example_function(n):
    return f"The sum is {sum(range(n))}"

example_function(999999)
```

Der `decorator` kann auch so verstanden werden:

```py
def example_function(n):
    return f"The sum is {sum(range(n))}"

example_function = timer(example_function)

example_function(999999)
```
