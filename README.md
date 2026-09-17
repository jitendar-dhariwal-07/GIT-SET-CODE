# Broken-Code Challenge: Fizz Buzz

This repository contains a broken implementation of LeetCode Problem 412: Fizz Buzz.

## Problem

Given an integer `n`, return a list of strings containing the numbers from `1` to `n`.

The rules are:

- Return `"FizzBuzz"` if the number is divisible by both `3` and `5`.
- Return `"Fizz"` if the number is divisible by `3`.
- Return `"Buzz"` if the number is divisible by `5`.
- Return the number as a string if it is not divisible by `3` or `5`.

## Example

```text
Input:
n = 15

Output:
[
    "1", "2", "Fizz", "4", "Buzz",
    "Fizz", "7", "8", "Fizz", "Buzz",
    "11", "Fizz", "13", "14", "FizzBuzz"
]
```

## Your Task

The implementation in `src/fizz_buzz.py` contains intentional bugs.

You must:

1. Fork this repository.
2. Clone your fork locally.
3. Read the source code and test cases.
4. Identify and fix the bugs.
5. Run all tests.
6. Commit your changes.
7. Push your solution to your fork.

## Running the Tests

From the project directory, run:

```bash
pytest
```

## Rules

- Modify only the source code.
- Do not delete or modify the tests.
- Do not hardcode the expected output.
- Return exactly one result for every number from `1` to `n`.
- Preserve the required output strings.
- Handle numbers divisible by both `3` and `5` correctly.
- Do not add unnecessary external dependencies.

## Submission Checklist

- [ ] Repository forked.
- [ ] Repository cloned.
- [ ] Source code inspected.
- [ ] Bugs identified.
- [ ] Code fixed.
- [ ] All tests passed.
- [ ] Changes committed.
- [ ] Changes pushed to GitHub.

## Recommended Git Workflow

```bash
git clone [https://github.com/](https://github.com/)<your-username>/broken-code-challenge.git
cd broken-code-challenge

pytest

git add src/fizz_buzz.py
git commit -m "Fix Fizz Buzz implementation"
git push origin main
```
