import random
from functools import wraps


def log(template):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            execution_time = random.randint(
                1, 10
            )  # Используйте random.randint() для генерации случайного времени выполнения
            print(template.format(execution_time))
            return result

        return wrapper

    return decorator
