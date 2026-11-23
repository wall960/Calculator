from batch_calculator import process_calculation
import pytest

def test_batch_addition():

    operation = "add"
    a = "4"
    b = "6"
    expected = ("OK", 10, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_subtraction():

    operation = "subtract"
    a = "60"
    b = "43"
    expected = ("OK", 17, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_multiplication():

    operation = "multiply"
    a = "8"
    b = "3"
    expected = ("OK", 24, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_division():

    operation = "divide"
    a = "6"
    b = "2"
    expected = ("OK", 3, "")

    result = process_calculation(operation, a, b)

    assert result == expected


def test_batch_negative_addition():

    operation = "add"
    a = "-32"
    b = "-6"
    expected = ("OK", -38, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_negative_multiplication():

    operation = "multiply"
    a = "-7"
    b = "-5"
    expected = ("OK", 35, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_decimal_addition():

    operation = "add"
    a = "3.02"
    b = "2.011"
    expected = ("OK", pytest.approx(5.031), "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_whitespace():

    operation = "   add  "
    a = "  12"
    b = "8 "
    expected = ("OK", 20, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_empty_first_operand():

    operation = "add"
    a = ""
    b = "5"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_empty_second_operand():

    operation = "add"
    a = "5"
    b = ""
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_invalid_first_operand():

    operation = "add"
    a = "hello"
    b = "5"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_invalid_second_operand():

    operation = "add"
    a = "5"
    b = "hello"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_upper_boundary():

    operation = "add"
    a = "1000"
    b = "0"
    expected = ("OK", 1000, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_lower_boundary():

    operation = "add"
    a = "-1000"
    b = "0"
    expected = ("OK", -1000, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_above_range():

    operation = "add"
    a = "1001"
    b = "0"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_below_range():

    operation = "add"
    a = "-1001"
    b = "0"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_valid_decimal_precision():

    operation = "add"
    a = "1.234"
    b = "2"
    expected = ("OK", 3.234, "")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_excessive_decimal_precision():

    operation = "add"
    a = "1.2345"
    b = "2"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_unknown_operation():

    operation = "power"
    a = "2"
    b = "3"
    expected = ("ERROR", "", "UNKNOWN_OPERATION")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_division_by_zero():

    operation = "divide"
    a = "10"
    b = "0"
    expected = ("ERROR", "", "DIVISION_BY_ZERO")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_unknown_operation_takes_priority():

    operation = "power"
    a = "hello"
    b = "0"
    expected = ("ERROR", "", "UNKNOWN_OPERATION")

    result = process_calculation(operation, a, b)

    assert result == expected

def test_batch_invalid_number_takes_priority():

    operation = "divide"
    a = "hello"
    b = "0"
    expected = ("ERROR", "", "INVALID_NUMBER")

    result = process_calculation(operation, a, b)

    assert result == expected

