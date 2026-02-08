#!/usr/bin/env python3
"""
Compute Descriptive Statistics Program.

This program reads numbers from a file and computes descriptive statistics
(mean, median, mode, standard deviation, variance) using manual algorithms.
Results are saved to StatisticsResults.txt and displayed on screen.

Usage: python compute_statistics.py <file_path>
"""

import sys
import time


def read_numbers_from_file(file_path):
    """
    Read numbers from a file, handling invalid data.

    Args:
        file_path (str): Path to the input file

    Returns:
        list: List of valid numbers (float)
    """
    numbers = []
    invalid_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        number = float(line)
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


def calculate_mean(numbers):
    """
    Calculate the arithmetic mean of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Mean value
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    """
    Calculate the median of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Median value
    """
    if not numbers:
        return 0.0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2

    if n % 2 == 0:  # Even number of elements
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2

    # Odd number of elements
    return sorted_numbers[mid]


def calculate_mode(numbers):
    """
    Calculate the mode (most frequent value) of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Mode value (returns first mode if multiple exist)
    """
    if not numbers:
        return 0.0

    # Count frequencies manually
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find maximum frequency
    max_freq = max(frequency.values())

    # Find the number(s) with maximum frequency
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    # Return the first mode (or smallest if multiple)
    return min(modes) if modes else 0.0


def calculate_variance(numbers):
    """
    Calculate the population variance of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Population variance
    """
    if not numbers:
        return 0.0

    mean = calculate_mean(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diffs) / len(numbers)

    return variance


def calculate_std_deviation(numbers):
    """
    Calculate the population standard deviation of a list of numbers.

    Args:
        numbers (list): List of numbers

    Returns:
        float: Population standard deviation
    """
    if not numbers:
        return 0.0

    variance = calculate_variance(numbers)
    return variance ** 0.5


def format_results(stats):
    """
    Format statistics results as a string.

    Args:
        stats (dict): Dictionary containing statistics:
            - count (int): Number of data points
            - mean (float): Mean value
            - median (float): Median value
            - mode (float): Mode value
            - std_dev (float): Standard deviation
            - variance (float): Variance
            - elapsed_time (float): Execution time in seconds

    Returns:
        str: Formatted results
    """
    results = []
    results.append("=" * 60)
    results.append("DESCRIPTIVE STATISTICS RESULTS")
    results.append("=" * 60)
    results.append(f"Count:               {stats['count']}")
    results.append(f"Mean:                {stats['mean']}")
    results.append(f"Median:              {stats['median']}")
    results.append(f"Mode:                {stats['mode']}")
    results.append(f"Standard Deviation:  {stats['std_dev']}")
    results.append(f"Variance:            {stats['variance']}")
    results.append("=" * 60)
    results.append(f"Execution Time:      {stats['elapsed_time']:.6f} seconds")
    results.append("=" * 60)

    return '\n'.join(results)


def save_results(results_text, output_file='StatisticsResults.txt'):
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
        print("Usage: python compute_statistics.py <file_path>")
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

    # Calculate statistics
    count = len(numbers)
    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    std_dev = calculate_std_deviation(numbers)
    variance = calculate_variance(numbers)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Format and display results
    stats = {
        'count': count,
        'mean': mean,
        'median': median,
        'mode': mode,
        'std_dev': std_dev,
        'variance': variance,
        'elapsed_time': elapsed_time
    }
    results_text = format_results(stats)

    print(results_text)

    # Save results to file
    save_results(results_text)


if __name__ == "__main__":
    main()
