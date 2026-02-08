"""Unit tests for convert_numbers.py"""

import sys
import os
import tempfile
import pytest

# Add source directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

# pylint: disable=wrong-import-position
import convert_numbers as cn


class TestToBinary:
    """Tests for to_binary function"""

    def test_binary_zero(self):
        """Test binary conversion of 0"""
        assert cn.to_binary(0) == '0'

    def test_binary_one(self):
        """Test binary conversion of 1"""
        assert cn.to_binary(1) == '1'

    def test_binary_small_number(self):
        """Test binary conversion of small number"""
        assert cn.to_binary(10) == '1010'

    def test_binary_power_of_two(self):
        """Test binary conversion of power of 2"""
        assert cn.to_binary(16) == '10000'

    def test_binary_large_number(self):
        """Test binary conversion of large number"""
        assert cn.to_binary(255) == '11111111'

    def test_binary_random_number(self):
        """Test binary conversion of random number"""
        # 42 in binary is 101010
        assert cn.to_binary(42) == '101010'

    def test_binary_very_large(self):
        """Test binary conversion of very large number"""
        # 1000000 in binary
        result = cn.to_binary(1000000)
        # Verify by converting back
        assert int(result, 2) == 1000000


class TestToHexadecimal:
    """Tests for to_hexadecimal function"""

    def test_hex_zero(self):
        """Test hex conversion of 0"""
        assert cn.to_hexadecimal(0) == '0'

    def test_hex_single_digit(self):
        """Test hex conversion of single digit"""
        assert cn.to_hexadecimal(9) == '9'

    def test_hex_with_letters(self):
        """Test hex conversion requiring letters"""
        assert cn.to_hexadecimal(10) == 'A'
        assert cn.to_hexadecimal(15) == 'F'

    def test_hex_small_number(self):
        """Test hex conversion of small number"""
        assert cn.to_hexadecimal(16) == '10'

    def test_hex_255(self):
        """Test hex conversion of 255"""
        assert cn.to_hexadecimal(255) == 'FF'

    def test_hex_256(self):
        """Test hex conversion of 256"""
        assert cn.to_hexadecimal(256) == '100'

    def test_hex_large_number(self):
        """Test hex conversion of large number"""
        # 1000 in hex is 3E8
        assert cn.to_hexadecimal(1000) == '3E8'

    def test_hex_very_large(self):
        """Test hex conversion of very large number"""
        result = cn.to_hexadecimal(1000000)
        # Verify by converting back
        assert int(result, 16) == 1000000


class TestReadNumbersFromFile:
    """Tests for read_numbers_from_file function"""

    def test_read_valid_numbers(self):
        """Test reading file with valid numbers"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n20\n30\n")
            temp_file = f.name

        try:
            numbers = cn.read_numbers_from_file(temp_file)
            assert numbers == [10, 20, 30]
        finally:
            os.unlink(temp_file)

    def test_read_with_invalid_data(self):
        """Test reading file with invalid data"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\nABC\n20\n")
            temp_file = f.name

        try:
            numbers = cn.read_numbers_from_file(temp_file)
            assert numbers == [10, 20]
        finally:
            os.unlink(temp_file)

    def test_read_with_negative_numbers(self):
        """Test reading file with negative numbers (should skip)"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n-5\n20\n")
            temp_file = f.name

        try:
            numbers = cn.read_numbers_from_file(temp_file)
            # Negative numbers are skipped
            assert numbers == [10, 20]
        finally:
            os.unlink(temp_file)

    def test_read_empty_lines(self):
        """Test reading file with empty lines"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            f.write("10\n\n20\n\n")
            temp_file = f.name

        try:
            numbers = cn.read_numbers_from_file(temp_file)
            assert numbers == [10, 20]
        finally:
            os.unlink(temp_file)

    def test_read_nonexistent_file(self):
        """Test reading non-existent file"""
        with pytest.raises(SystemExit):
            cn.read_numbers_from_file("nonexistent_file.txt")


class TestConversionAccuracy:
    """Tests to verify conversion accuracy"""

    def test_conversion_consistency(self):
        """Test that conversions are consistent"""
        test_numbers = [0, 1, 10, 100, 255, 256, 1000, 65535]

        for num in test_numbers:
            # Convert using our functions
            binary = cn.to_binary(num)
            hexadecimal = cn.to_hexadecimal(num)

            # Verify by converting back
            assert int(binary, 2) == num, f"Binary conversion failed for {num}"
            assert int(hexadecimal, 16) == num, \
                f"Hex conversion failed for {num}"


class TestIntegrationTC1:
    """Integration test with TC1.txt"""

    def test_tc1_conversions(self):
        """Test conversions with TC1.txt"""
        test_file = os.path.join(
            os.path.dirname(__file__), 'data', 'TC1.txt'
        )
        numbers = cn.read_numbers_from_file(test_file)

        # Verify we read numbers
        assert len(numbers) > 0

        # Test a few specific conversions from TC1
        # First number should be 6980368
        if numbers[0] == 6980368:
            assert cn.to_binary(6980368) == '11010101000001100010000'
            assert cn.to_hexadecimal(6980368) == '6A8310'


class TestFormatResults:
    """Tests for format_results function"""

    def test_format_results_structure(self):
        """Test that format_results produces expected structure"""
        conversions = [
            (10, '1010', 'A'),
            (255, '11111111', 'FF'),
        ]
        result = cn.format_results(conversions, 0.123)

        assert "NUMBER BASE CONVERSION RESULTS" in result
        assert "NUMBER" in result
        assert "BINARY" in result
        assert "HEXADECIMAL" in result
        assert "10" in result
        assert "1010" in result
        assert "A" in result or "A " in result
        assert "255" in result
        assert "FF" in result
        assert "Execution Time:" in result


class TestSaveResults:
    """Tests for save_results function"""

    def test_save_results_creates_file(self):
        """Test that save_results creates a file"""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = os.path.join(tmpdir, 'test_conversion.txt')
            test_content = "Test conversion results"

            cn.save_results(test_content, output_file)

            assert os.path.exists(output_file)
            with open(output_file, 'r', encoding='utf-8') as f:
                content = f.read()
                assert content == test_content


class TestEdgeCases:
    """Tests for edge cases"""

    def test_binary_boundary_values(self):
        """Test binary conversion at boundary values"""
        assert cn.to_binary(0) == '0'
        assert cn.to_binary(1) == '1'
        assert cn.to_binary(2) == '10'
        assert cn.to_binary(3) == '11'

    def test_hex_boundary_values(self):
        """Test hex conversion at boundary values"""
        assert cn.to_hexadecimal(0) == '0'
        assert cn.to_hexadecimal(1) == '1'
        assert cn.to_hexadecimal(9) == '9'
        assert cn.to_hexadecimal(10) == 'A'
        assert cn.to_hexadecimal(15) == 'F'
        assert cn.to_hexadecimal(16) == '10'
