#!/usr/bin/env python3
"""
Word Frequency Counter Program.

This program reads words from a file and counts the frequency of each
distinct word using manual algorithms (no Counter class).
Results are saved to WordCountResults.txt and displayed on screen.

Usage: python word_count.py <file_path>
"""

import sys
import time


def read_words_from_file(file_path):
    """
    Read words from a file, handling errors.

    Args:
        file_path (str): Path to the input file

    Returns:
        list: List of words (converted to lowercase)
    """
    words = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split line into words (by whitespace)
                line_words = line.strip().split()
                # Convert to lowercase and add to list
                for word in line_words:
                    if word:  # Skip empty strings
                        # Remove common punctuation
                        word = word.lower()
                        words.append(word)

        return words

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except (IOError, OSError) as error:
        print(f"Error reading file: {error}")
        sys.exit(1)


def count_word_frequencies(words):
    """
    Count the frequency of each word manually.

    Args:
        words (list): List of words

    Returns:
        dict: Dictionary with words as keys and frequencies as values
    """
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def sort_frequency_dict(frequency):
    """
    Sort frequency dictionary by word (alphabetically).

    Args:
        frequency (dict): Dictionary of word frequencies

    Returns:
        list: List of tuples (word, count) sorted alphabetically
    """
    # Convert to list of tuples
    items = []
    for word, count in frequency.items():
        items.append((word, count))

    # Sort manually (bubble sort for simplicity and manual implementation)
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sort alphabetically by word
            if items[j][0] > items[j + 1][0]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items


def format_results(sorted_frequencies, total_words, elapsed_time):
    """
    Format word count results as a string.

    Args:
        sorted_frequencies (list): List of (word, count) tuples
        total_words (int): Total number of words
        elapsed_time (float): Execution time in seconds

    Returns:
        str: Formatted results
    """
    results = []
    results.append("=" * 60)
    results.append("WORD FREQUENCY COUNT RESULTS")
    results.append("=" * 60)
    results.append(f"{'WORD':<30} {'FREQUENCY':<15}")
    results.append("-" * 60)

    for word, count in sorted_frequencies:
        results.append(f"{word:<30} {count:<15}")

    results.append("=" * 60)
    results.append(f"Total distinct words: {len(sorted_frequencies)}")
    results.append(f"Total words:          {total_words}")
    results.append(f"Execution Time:       {elapsed_time:.6f} seconds")
    results.append("=" * 60)

    return '\n'.join(results)


def save_results(results_text, output_file='WordCountResults.txt'):
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
        print("Usage: python word_count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    print(f"Reading data from: {file_path}\n")

    # Start timing
    start_time = time.time()

    # Read words from file
    words = read_words_from_file(file_path)

    if not words:
        print("Warning: No words found in the file.")
        sys.exit(0)

    # Count word frequencies
    frequency = count_word_frequencies(words)

    # Sort frequencies alphabetically
    sorted_frequencies = sort_frequency_dict(frequency)

    # End timing
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Format and display results
    results_text = format_results(
        sorted_frequencies, len(words), elapsed_time
    )

    print(results_text)

    # Save results to file
    save_results(results_text)


if __name__ == "__main__":
    main()
