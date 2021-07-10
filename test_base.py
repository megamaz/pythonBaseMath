import BaseMath
import numpy

math = BaseMath.Math(16)

def test_multipleSymbols():
    A, B = math.symbol("A", "B")
    assert int(A) == 10 and int(B) == 11

def test_resultCorrect():
    # a test to test if the returned results are correct
    for base in range(2, 36):

        m = BaseMath.Math(base)
        print(f"Testing base {base}.")
        for a in range(base**2):
            for b in range(base**2):
                # expected result
                expectResult = numpy.base_repr(a * b, base)
                finalResult = m.calculate(f"{numpy.base_repr(a, base).upper()} * {numpy.base_repr(b, base).upper()}")
        
                assert str(finalResult) == expectResult, f"Expected {expectResult}, got {finalResult} at base {base} a={a}, b={b}. Base 10 expected number: {a * b}, Base 10 result number: {finalResult.value}"
