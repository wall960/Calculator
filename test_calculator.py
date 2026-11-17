from calculator import add, subtract, multiply, divide

def test_add():
    #Arrange
    a = 2
    b = 3

    #Act
    result = add(a, b)

    #Assert
    assert result == 5

def test_divide():
    #Arrange
    a = 6
    b = 2

    #Act
    result = divide(a, b)

    #Assert
    assert result == 3

def test_multiply():
    #Arrange
    a = 5
    b = 3

    #Act
    result = multiply(a, b)

    #Assert
    assert result == 15

def test_subtract():
    #Arrange
    a = 7
    b = 3

    #Act
    result = subtract(a, b)

    #Assert
    assert result == 4

def test_divide_uneven():
    #Arrange
    a = 5
    b = 2

    #Act
    result = divide(a, b)

    #Assert
    assert result == 2.5

