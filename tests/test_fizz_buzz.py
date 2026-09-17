from src.fizz_buzz import fizz_buzz


def test_basic_fizz_buzz():
    result = fizz_buzz(15)

    assert result == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


def test_small_input():
    result = fizz_buzz(5)

    assert result == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
    ]


def test_input_three():
    result = fizz_buzz(3)

    assert result == [
        "1",
        "2",
        "Fizz",
    ]


def test_input_fifteen():
    result = fizz_buzz(15)

    assert result[14] == "FizzBuzz"


def test_numbers_are_strings():
    result = fizz_buzz(2)

    assert result == ["1", "2"]
    assert all(isinstance(value, str) for value in result)


def test_multiple_of_three():
    result = fizz_buzz(9)

    assert result[2] == "Fizz"
    assert result[5] == "Fizz"
    assert result[8] == "Fizz"


def test_multiple_of_five():
    result = fizz_buzz(10)

    assert result[4] == "Buzz"
    assert result[9] == "Buzz"


def test_multiple_of_both_three_and_five():
    result = fizz_buzz(30)

    assert result[14] == "FizzBuzz"
    assert result[29] == "FizzBuzz"


def test_no_extra_values():
    result = fizz_buzz(7)

    assert len(result) == 7


def test_zero_input():
    result = fizz_buzz(0)

    assert result == []
