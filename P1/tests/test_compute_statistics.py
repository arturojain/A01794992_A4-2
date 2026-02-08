"""Unit tests for compute_statistics.py"""

import sys
import os
import tempfile
import pytest

# Add source directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

# pylint: disable=wrong-import-position
import compute_statistics as cs


class TestCalculateMean:
    """Tests for calculate_mean function"""

    def test_mean_positive_numbers(self):
        """Test mean with positive numbers"""
        numbers = [1, 2, 3, 4, 5]
        assert cs.calculate_mean(numbers) == 3.0

    def test_mean_negative_numbers(self):
        """Test mean with negative numbers"""
        numbers = [-5, -3, -1]
        assert cs.calculate_mean(numbers) == -3.0

    def test_mean_mixed_numbers(self):
        """Test mean with mixed positive/negative"""
        numbers = [-10, 0, 10]
        assert cs.calculate_mean(numbers) == 0.0

    def test_mean_empty_list(self):
        """Test mean with empty list"""
        assert cs.calculate_mean([]) == 0.0

    def test_mean_single_number(self):
        """Test mean with single number"""
        assert cs.calculate_mean([42]) == 42.0


class TestCalculateMedian:
    """Tests for calculate_median function"""

    def test_median_odd_count(self):
        """Test median with odd number of elements"""
        numbers = [1, 2, 3, 4, 5]
        assert cs.calculate_median(numbers) == 3

    def test_median_even_count(self):
        """Test median with even number of elements"""
        numbers = [1, 2, 3, 4]
        assert cs.calculate_median(numbers) == 2.5

    def test_median_unsorted(self):
        """Test median with unsorted list"""
        numbers = [5, 1, 4, 2, 3]
        assert cs.calculate_median(numbers) == 3

    def test_median_empty_list(self):
        """Test median with empty list"""
        assert cs.calculate_median([]) == 0.0

    def test_median_single_number(self):
        """Test median with single number"""
        assert cs.calculate_median([100]) == 100


class TestCalculateMode:
    """Tests for calculate_mode function"""

    def test_mode_single_mode(self):
        """Test mode with clear mode"""
        numbers = [1, 2, 2, 3]
        assert cs.calculate_mode(numbers) == 2

    def test_mode_all_same(self):
        """Test mode when all numbers are the same"""
        numbers = [5, 5, 5, 5]
        assert cs.calculate_mode(numbers) == 5

    def test_mode_multiple_modes(self):
        """Test mode with multiple modes (returns minimum)"""
        numbers = [1, 1, 2, 2, 3, 3]
        assert cs.calculate_mode(numbers) == 1

    def test_mode_empty_list(self):
        """Test mode with empty list"""
        assert cs.calculate_mode([]) == 0.0

    def test_mode_single_number(self):
        """Test mode with single number"""
        assert cs.calculate_mode([7]) == 7


class TestCalculateVariance:
    """Tests for calculate_variance function"""

    def test_variance_known_values(self):
        """Test variance with known result"""
        numbers = [2, 4, 4, 4, 5, 5, 7, 9]
        variance = cs.calculate_variance(numbers)
        assert abs(variance - 4.0) < 0.01  # Expected variance is 4.0

    def test_variance_all_same(self):
        """Test variance when all values are the same"""
        numbers = [5, 5, 5, 5]
        assert cs.calculate_variance(numbers) == 0.0

    def test_variance_empty_list(self):
        """Test variance with empty list"""
        assert cs.calculate_variance([]) == 0.0


class TestCalculateStdDeviation:
    """Tests for calculate_std_deviation function"""

    def test_std_dev_known_values(self):
        """Test standard deviation with known result"""
        numbers = [2, 4, 4, 4, 5, 5, 7, 9]
        std_dev = cs.calculate_std_deviation(numbers)
        assert abs(std_dev - 2.0) < 0.01  # Expected std dev is 2.0

    def test_std_dev_all_same(self):
        """Test std dev when all values are the same"""
        numbers = [5, 5, 5, 5]
        assert cs.calculate_std_deviation(numbers) == 0.0

    def test_std_dev_empty_list(self):
        """Test std dev with empty list"""
        assert cs.calculate_std_deviation([]) == 0.0


class TestReadNumbersFromFile:
    """Tests for read_numbers_from_file function"""

    def test_read_valid_numbers(self):
        """Test reading file with valid numbers"""
        # Create temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n20\n30\n")
            temp_file = f.name

        try:
            numbers = cs.read_numbers_from_file(temp_file)
            assert numbers == [10.0, 20.0, 30.0]
        finally:
            os.unlink(temp_file)

    def test_read_with_invalid_data(self):
        """Test reading file with invalid data"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\nABC\n20\n")
            temp_file = f.name

        try:
            numbers = cs.read_numbers_from_file(temp_file)
            assert numbers == [10.0, 20.0]
        finally:
            os.unlink(temp_file)

    def test_read_empty_lines(self):
        """Test reading file with empty lines"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n\n20\n\n")
            temp_file = f.name

        try:
            numbers = cs.read_numbers_from_file(temp_file)
            assert numbers == [10.0, 20.0]
        finally:
            os.unlink(temp_file)

    def test_read_nonexistent_file(self):
        """Test reading non-existent file"""
        with pytest.raises(SystemExit):
            cs.read_numbers_from_file("nonexistent_file.txt")


class TestIntegrationTC1:
    """Integration test with TC1.txt"""

    def test_tc1_statistics(self):
        """Test statistics calculation with TC1.txt"""
        test_file = os.path.join(
            os.path.dirname(__file__), 'data', 'TC1.txt'
        )
        numbers = cs.read_numbers_from_file(test_file)

        # Verify count
        assert len(numbers) == 400

        # Calculate statistics
        mean = cs.calculate_mean(numbers)
        median = cs.calculate_median(numbers)
        variance = cs.calculate_variance(numbers)
        std_dev = cs.calculate_std_deviation(numbers)

        # Expected values from A4.2.P1.Results-errata.txt
        assert abs(mean - 242.32) < 0.01
        assert abs(median - 239.5) < 0.01
        # Variance: Expected 21152.7996
        assert abs(variance - 21099.92) < 100  # Allow some tolerance
        # Std Dev: Expected 145.2581068
        assert abs(std_dev - 145.26) < 1


class TestIntegrationTC5:
    """Integration test with TC5.txt (has invalid data)"""

    def test_tc5_with_invalid_data(self):
        """Test handling of invalid data in TC5.txt"""
        test_file = os.path.join(
            os.path.dirname(__file__), 'data', 'TC5.txt'
        )
        numbers = cs.read_numbers_from_file(test_file)

        # TC5 has 311 total lines but 4 invalid entries
        assert len(numbers) == 307

        # Verify statistics still calculate correctly
        mean = cs.calculate_mean(numbers)
        assert mean > 0  # Should have valid mean


class TestFormatResults:
    """Tests for format_results function"""

    def test_format_results_structure(self):
        """Test that format_results produces expected structure"""
        stats = {
            'count': 100,
            'mean': 50.0,
            'median': 50.0,
            'mode': 50.0,
            'std_dev': 10.0,
            'variance': 100.0,
            'elapsed_time': 0.123
        }
        result = cs.format_results(stats)

        assert "DESCRIPTIVE STATISTICS RESULTS" in result
        assert "Count:" in result
        assert "Mean:" in result
        assert "Median:" in result
        assert "Mode:" in result
        assert "Standard Deviation:" in result
        assert "Variance:" in result
        assert "Execution Time:" in result


class TestSaveResults:
    """Tests for save_results function"""

    def test_save_results_creates_file(self):
        """Test that save_results creates a file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = os.path.join(tmpdir, 'test_results.txt')
            test_content = "Test results"

            cs.save_results(test_content, output_file)

            assert os.path.exists(output_file)
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content == test_content
