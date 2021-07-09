import baseMath

math = baseMath.Math(16)

def test_multipleSymbols():
    A, B = math.symbol("A", "B")
    assert int(A) == 10 and int(B) == 11