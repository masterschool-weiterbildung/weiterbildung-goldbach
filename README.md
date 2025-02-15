# Prime Number and Goldbach's Conjecture Checker

## Overview
This Python program determines whether a number is prime, checks for evenness, and verifies Goldbach's conjecture by finding two prime numbers that sum up to an even integer.

## Features
- Check if a number is prime.
- Determine if a number is even.
- Find pairs of prime numbers that sum to a given even number.
- Verify Goldbach's conjecture.

## Constants
- `RANGE_START (int)`: The starting value (2) for checking divisors in primality tests.
- `SQUARE_ROOT_OF_NUMBER_TO_CHECK (float)`: Exponent (0.5) for calculating square roots.
- `NUMBER_EVEN_TWO (int)`: Represents the number 2, used for even-number checks.
- `NUMBER_ODD_ONE (int)`: Represents the number 1.

## Functions
### `is_prime(number_to_check: int) -> bool`
Determines if a given number is prime.

### `is_even_number(input_number: int) -> bool`
Checks if a number is even.

### `list_of_two_primes(input_number: int) -> list[tuple]`
Finds all pairs of prime numbers whose sum equals the given number.

### `is_goldbach_conjecture(input_number: int) -> bool`
Checks whether a number satisfies Goldbach's conjecture.

### `get_integer() -> int`
Prompts the user for an integer input and validates it.

### `print_the_pair_numbers(number: int, list_pair_primes: list[tuple]) -> None`
Prints pairs of prime numbers that sum up to the given number.

### `main() -> None`
Main function to handle user input and process Goldbach's conjecture.

## Usage
Run the script and enter a number when prompted:
```sh
python script.py
```
