---
title: "pydantic"
---

## Erste Schritte

```bash
pip install pydantic
```

✔ Type Hints
✔ Data Validation
✔ Serialization
✖ built-in

```py
from pydantic import BaseModel, field_validator
from pydantic import EmailStr  # pip install pydantic[email]


class User(BaseModel):
    name: str
    age: int
    email: EmailStr

    @field_validator('age')
    def val_age(cls, value:int) -> int:
        if value <= 0:
            raise ValueError(f"age must be positive, current age: {value}")
        return value
```

```py
# invalid
# user = User(name='Jim', age=21, email='jim')
# user = User(name='Jim', age=-21, email='jim@example.com')

# valid
user = User(name='Jim', age=21, email='jim@example.com')
```

## JSON Serialization

```py
user_obj = User(name='Jim', age=21, email='jim@example.com')
user_to_json = user.model_dump_json()
user_to_dict = user.model_dump()
user_obj_by_json = User.model_validate_json('{"name":"Jim","age":21,"email":"jim@example.com"}')

print(f"Normal Instanz:\n\ttype:\t{type(user_obj)}", f"\tvalue:\t{user_obj}", sep='\n', end=f"\n{'-' * 60}\n")
print(f"Als json:\n\ttype:\t{type(user_to_json)}", f"\tvalue:\t{user_to_json}", sep='\n', end=f"\n{'-' * 60}\n")
print(f"Als dict:\n\ttype:\t{type(user_to_dict)}", f"\tvalue:\t{user_to_dict}", sep='\n', end=f"\n{'-' * 60}\n")
print(f"Als obj (aus string/json):\n\ttype:\t{type(user_obj_by_json)}", f"\tvalue:\t{user_obj_by_json}", sep='\n', end=f"\n{'-' * 60}\n")
```
