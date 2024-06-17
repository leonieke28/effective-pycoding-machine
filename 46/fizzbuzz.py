from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


assert fizzbuzz(3) == "Fizz"
assert fizzbuzz(7) == 7
assert fizzbuzz(10) == "Buzz"
assert fizzbuzz(15) == "FizzBuzz"
