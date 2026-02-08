#!/usr/bin/env python3
"""
Number Base Converter Program.

This program reads numbers from a file and converts them to binary and
hexadecimal representation using manual algorithms (no built-in functions).
Results are saved to ConversionResults.txt and displayed on screen.

Usage: python convert_numbers.py <file_path>
"""

import sys
import time


def read_numbers_from_file(file_path):
    """
    Read numbers from a file, handling invalid data.

    Args:
        file_path (str): Path to the input file

    Returns:
        list: List of valid integers
    """
    numbers = []
    invalid_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = int(line)
                        if number < 0:
                            print(f"Warning: Negative number on line "
                                  f"{line_num}: {number} (skipped)")
                            invalid_count += 1
                        else:
                            numbers.append(number)
                    except ValueError:
                        print(f"Warning: Invalid data on line {line_num}: "
                              f"'{line}' (skipped)")
                        invalid_count += 1

        if invalid_count > 0:
            print(f"\nTotal invalid entries skipped: {invalid_count}\n")

        return numbers

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except (IOError, OSError) as error:
        print(f"Error reading file: {error}")
        sys.exit(1)


def to_binary(number):
    """
    Convert a number to binary representation manually.

    Args:
        number (int): Number to convert (must be >= 0)

    Returns:
        str: Binary representation
    """
    if number == 0:
        return '0'

    binary = ''
    temp = number

    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2

    return binary


def to_hexadecimal(number):
    """
    Convert a number to hexadecimal representation manually.

    Args:
        number (int): Number to convert (must be >= 0)

    Returns:
        str: Hexadecimal representation (uppercase)
    """
    if number == 0:
        return '0'

    hex_digits = '0123456789ABCDEF'
    hexadecimal = ''
    temp = number

    while temp > 0:
        remainder = temp % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        temp = temp // 16

    return hexadecimal


def format_results(conversions, elapsed_time):
    """
    Format conversion results as a string.

    Args:
        conversions (list): List of tuples (number, binary, hexadecimal)
        elapsed_time (float): Execution time in seconds

    Returns:
        str: Formatted results
    """
    results = []
    results.append("=" * 70)
    results.append("NUMBER BASE CONVERSION RESULTS")
    results.append("=" * 70)
    results.append(f"{'NUMBER':<15} {'BINARY':<30} {'HEXADECIMAL':<15}")
    results.append("-" * 70)

    for number, binary, hexadecimal in conversions:
        results.append(f"{number:<15} {binary:<30} {hexadecimal:<15}")

    results.append("=" * 70)
    results.append(f"Total conversions: {len(conversions)}")
    results.append(f"Execution Time:    {elapsed_time:.6f} seconds")
    results.append("=" * 70)

    return '\n'.join(results)


def save_results(results_text, output_file='ConversionResults.txt'):
    """
    Save results to a file.

    Args:
        results_text (str): Results to save
        output_file (str): Output file path
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(results_text)
        print(f"\nResults saved to: {output_file}")
    except (IOError, OSError) as error:
        print(f"Error saving results: {error}")


def main():
    """Main function to execute the program."""
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    print(f"Reading data from: {file_path}\n")

    # Start timing
    start_time = time.time()

    # Read numbers from file
    numbers = read_numbers_from_file(file_path)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    # Convert numbers
    conversions = []
    for number in numbers:
        binary = to_binary(number)
        hexadecimal = to_hexadecimal(number)
        conversions.append((number, binary, hexadecimal))

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Format and display results
    results_text = format_results(conversions, elapsed_time)

    print(results_text)

    # Save results to file
    save_results(results_text)


if __name__ == "__main__":
    main()
