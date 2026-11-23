from batch_calculator import process_calculation

def test_batch_addition():

    operation = "add"
    a = "4"
    b = "6"
    expected = ("OK", 10, "")

    result = process_calculation(operation, a, b)

    assert result == expected
