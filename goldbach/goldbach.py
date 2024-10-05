RANGE_START = 2
SQUARE_ROOT_OF_NUMBER_TO_CHECK = 0.5
NUMBER_EVEN_TWO = 2
NUMBER_ODD_ONE = 1
"""
Constants:
----------
RANGE_START (int): 
    The starting value (2) for checking divisors when determining if a number is prime.

SQUARE_ROOT_OF_NUMBER_TO_CHECK (float): 
    Represents the exponent (0.5) used to calculate the square root of a number, 
    which limits the range of divisors.

NUMBER_EVEN_TWO (int): 
    The value 2, used for determining whether a number is even.

NUMBER_ODD_ONE (int): 
    The value 1
"""


def is_prime(number_to_check: int) -> bool:
    """
    Determines if a given number is prime.

    A prime number is a number greater than 1 that has no divisors
    other than 1 and itself. This function returns `True` if the input
    number is prime, and `False` otherwise.

    Parameters:
    -----------
    number_to_check (int): The number to check for primality.

    Returns:
    --------
    bool: True if the number is prime, False otherwise.

    Logic:
    ------
    - If the number is less than 2, it is not prime.
    - Checks divisibility from 2 up to the square root of the number (rounded up).
    - If any divisor in this range divides the number evenly, it is not prime.
    """
    if number_to_check < NUMBER_EVEN_TWO:
        return False

    return not any(number_to_check % i == 0
                   for i in range(RANGE_START,
                                  int(number_to_check **
                                      SQUARE_ROOT_OF_NUMBER_TO_CHECK)
                                  + NUMBER_ODD_ONE))


def is_even_number(input_number: int) -> bool:
    """
    Determines if a given number is even.

    Parameters:
    -----------
    input_number (int): The number to check for evenness.

    Returns:
    --------
    bool: True if the number is even, False if it is odd.
    """
    return False if input_number % NUMBER_EVEN_TWO == NUMBER_ODD_ONE else True


def print_output(number: int, first_prime: int, second_prime: int) -> None:
    """
    Prints a formatted message showing that the given number is the sum of two prime numbers.

    Parameters:
    -----------
    number (int): The original number to be expressed as a sum of two primes.
    first_prime (int): The first prime number in the sum.
    second_prime (int): The second prime number in the sum.

    Returns:
    --------
    None
    """
    print(
        f"The number {number} equals to the sum of "
        f"{first_prime} and {second_prime}"
    )


def list_of_two_primes(input_number: int) -> list[tuple]:
    """
    This function finds all pairs of prime numbers whose sum equals the input number.
    It iterates over possible prime candidates for the first number and computes the
    second prime as the difference between the input number and the first prime.
    If both numbers in the pair are prime, the pair is added to the result list.

    Parameters:
    -----------
    input_number (int):
        The number to be expressed as the sum of two prime numbers.

    Returns:
    --------
    list[tuple]:
        A list of tuples, where each tuple contains two prime
        numbers whose sum equals the input number.

    Logic:
    ------
    - For each number from 2 up to the input number, the function checks if both
        the number and the difference between the input number and this number are prime.
    - If both numbers are prime, the pair is added to the result list.
    """
    return_list = []
    for first_prime in range(NUMBER_EVEN_TWO, input_number):
        second_prime = input_number - first_prime

        if is_prime(first_prime) and is_prime(second_prime):
            return_list.append((first_prime, second_prime))

    return return_list


def is_goldbach_conjecture(input_number: int) -> bool:
    """
    Goldbach's Conjecture states that every even number greater than 2 can be
    expressed as the sum of two prime numbers. This function returns `True`
    if the input number is even, as it is a candidate for the conjecture,
    and `False` otherwise.

    Parameters:
    -----------
    input_number (int):
        The number to check for qualification under Goldbach's Conjecture.

    Returns:
    --------
    bool: True if the number is even and greater than 2
          (a candidate for the conjecture), False if the number is odd.
    """
    return False if not is_even_number(input_number) else True


def user_input() -> int:
    """
    Prompts the user to enter an integer.

    This function displays a prompt asking the user to input a number.
    The input is converted to an integer before being returned.

    Returns:
    --------
    int: The integer entered by the user.
    """
    return int(input("Enter a number: "))


def get_integer() -> int:
    """
    Continuously prompts the user for input until a valid integer is provided.

    Returns:
    --------
    int: The valid integer input provided by the user.

    Logic:
    ------
    - Uses a while loop to repeatedly ask for input.
    - If the input cannot be converted to an integer, an error message is printed
      and the loop continues until a valid integer is entered.
    """
    while True:
        try:
            input_number = user_input()
        except ValueError:
            print(f"Input number is not an Integer")
        else:
            break
    return input_number


def print_the_pair_numbers(number: int, list_pair_primes: list[tuple]) -> None:
    """
    Print pairs of prime numbers alongside a specified number.

    Parameters:
    number (int): The number to be printed alongside each
                  pair of prime numbers.
    list_pair_primes (list[tuple]): A list of tuples, where each tuple
                                    contains two prime numbers.
    """
    for first_number, second_number in list_pair_primes:
        print_output(number, first_number, second_number)


def main() -> None:
    """
    The main entry point of the program.

    This function prompts the user to input an integer, checks if the integer
    satisfies Goldbach's conjecture, and if so, retrieves and prints pairs of
    prime numbers that sum up to the specified integer.
    """
    number = get_integer()

    if is_goldbach_conjecture(number):
        print_the_pair_numbers(number,
                               list_of_two_primes(number))


if __name__ == '__main__':
    main()
