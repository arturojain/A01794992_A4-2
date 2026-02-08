"""Unit tests for word_count.py"""

import sys
import os
import tempfile
import pytest

# Add source directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

# pylint: disable=wrong-import-position
import word_count as wc


class TestReadWordsFromFile:
    """Tests for read_words_from_file function"""

    def test_read_single_line(self):
        """Test reading single line with words"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("hello world")
            temp_file = f.name

        try:
            words = wc.read_words_from_file(temp_file)
            assert words == ['hello', 'world']
        finally:
            os.unlink(temp_file)

    def test_read_multiple_lines(self):
        """Test reading multiple lines"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("hello\nworld\npython")
            temp_file = f.name

        try:
            words = wc.read_words_from_file(temp_file)
            assert words == ['hello', 'world', 'python']
        finally:
            os.unlink(temp_file)

    def test_read_mixed_case(self):
        """Test that words are converted to lowercase"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("Hello WORLD Python")
            temp_file = f.name

        try:
            words = wc.read_words_from_file(temp_file)
            assert words == ['hello', 'world', 'python']
        finally:
            os.unlink(temp_file)

    def test_read_empty_lines(self):
        """Test reading file with empty lines"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("hello\n\nworld\n\n")
            temp_file = f.name

        try:
            words = wc.read_words_from_file(temp_file)
            assert words == ['hello', 'world']
        finally:
            os.unlink(temp_file)

    def test_read_nonexistent_file(self):
        """Test reading non-existent file"""
        with pytest.raises(SystemExit):
            wc.read_words_from_file("nonexistent_file.txt")


class TestCountWordFrequencies:
    """Tests for count_word_frequencies function"""

    def test_count_single_word(self):
        """Test counting single word"""
        words = ['hello']
        freq = wc.count_word_frequencies(words)
        assert freq == {'hello': 1}

    def test_count_multiple_different_words(self):
        """Test counting multiple different words"""
        words = ['hello', 'world', 'python']
        freq = wc.count_word_frequencies(words)
        assert freq == {'hello': 1, 'world': 1, 'python': 1}

    def test_count_repeated_words(self):
        """Test counting repeated words"""
        words = ['hello', 'world', 'hello', 'python', 'world']
        freq = wc.count_word_frequencies(words)
        assert freq == {'hello': 2, 'world': 2, 'python': 1}

    def test_count_all_same_word(self):
        """Test counting when all words are the same"""
        words = ['test', 'test', 'test']
        freq = wc.count_word_frequencies(words)
        assert freq == {'test': 3}

    def test_count_empty_list(self):
        """Test counting empty list"""
        words = []
        freq = wc.count_word_frequencies(words)
        assert freq == {}


class TestSortFrequencyDict:
    """Tests for sort_frequency_dict function"""

    def test_sort_alphabetically(self):
        """Test that words are sorted alphabetically"""
        freq = {'zebra': 1, 'apple': 2, 'banana': 1}
        sorted_freq = wc.sort_frequency_dict(freq)

        # Extract just the words
        words = [word for word, count in sorted_freq]
        assert words == ['apple', 'banana', 'zebra']

    def test_sort_maintains_counts(self):
        """Test that sorting maintains correct counts"""
        freq = {'c': 3, 'a': 1, 'b': 2}
        sorted_freq = wc.sort_frequency_dict(freq)

        assert sorted_freq == [('a', 1), ('b', 2), ('c', 3)]

    def test_sort_single_item(self):
        """Test sorting single item"""
        freq = {'word': 5}
        sorted_freq = wc.sort_frequency_dict(freq)
        assert sorted_freq == [('word', 5)]

    def test_sort_empty_dict(self):
        """Test sorting empty dictionary"""
        freq = {}
        sorted_freq = wc.sort_frequency_dict(freq)
        assert sorted_freq == []


class TestIntegrationTC1:
    """Integration test with TC1.txt"""

    def test_tc1_word_count(self):
        """Test word counting with TC1.txt"""
        test_file = os.path.join(
            os.path.dirname(__file__), 'data', 'TC1.txt'
        )
        words = wc.read_words_from_file(test_file)

        # Verify we read words
        assert len(words) > 0

        # Count frequencies
        freq = wc.count_word_frequencies(words)

        # Verify distinct words
        assert len(freq) > 0

        # Check if 'conservative' appears twice (from results file)
        if 'conservative' in freq:
            assert freq['conservative'] == 2


class TestFormatResults:
    """Tests for format_results function"""

    def test_format_results_structure(self):
        """Test that format_results produces expected structure"""
        sorted_freq = [
            ('apple', 3),
            ('banana', 1),
            ('cherry', 2),
        ]
        result = wc.format_results(sorted_freq, 6, 0.123)

        assert "WORD FREQUENCY COUNT RESULTS" in result
        assert "WORD" in result
        assert "FREQUENCY" in result
        assert "apple" in result
        assert "3" in result
        assert "banana" in result
        assert "1" in result
        assert "cherry" in result
        assert "2" in result
        assert "Total distinct words: 3" in result
        assert "Total words:          6" in result
        assert "Execution Time:" in result


class TestSaveResults:
    """Tests for save_results function"""

    def test_save_results_creates_file(self):
        """Test that save_results creates a file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = os.path.join(tmpdir, 'test_word_count.txt')
            test_content = "Test word count results"

            wc.save_results(test_content, output_file)

            assert os.path.exists(output_file)
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content == test_content


class TestEndToEnd:
    """End-to-end tests"""

    def test_complete_workflow(self):
        """Test complete workflow from file to results"""
        # Create test file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("hello world\nhello python\nworld")
            temp_file = f.name

        try:
            # Read words
            words = wc.read_words_from_file(temp_file)
            assert len(words) == 5

            # Count frequencies
            freq = wc.count_word_frequencies(words)
            assert freq['hello'] == 2
            assert freq['world'] == 2
            assert freq['python'] == 1

            # Sort frequencies
            sorted_freq = wc.sort_frequency_dict(freq)
            assert sorted_freq[0][0] == 'hello'  # First alphabetically
            assert sorted_freq[1][0] == 'python'
            assert sorted_freq[2][0] == 'world'

        finally:
            os.unlink(temp_file)

    def test_case_insensitivity(self):
        """Test that counting is case-insensitive"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("Hello HELLO hello")
            temp_file = f.name

        try:
            words = wc.read_words_from_file(temp_file)
            freq = wc.count_word_frequencies(words)

            # All variants should be counted as 'hello'
            assert freq.get('hello', 0) == 3
            assert freq.get('Hello', 0) == 0
            assert freq.get('HELLO', 0) == 0

        finally:
            os.unlink(temp_file)
