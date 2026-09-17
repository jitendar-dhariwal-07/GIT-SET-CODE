def fizz_buzz(n):
    """
    Return the Fizz Buzz sequence from 1 to n.

    Rules:
    - Multiples of 3 should be "Fizz".
    - Multiples of 5 should be "Buzz".
    - Multiples of both 3 and 5 should be "FizzBuzz".
    - Other numbers should be returned as strings.
    """

    result = []

    for number in range(0, n):
        if number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        elif number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")
        else:
            result.append(number)

    return result
