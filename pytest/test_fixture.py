import conftest


def test_abc(fxtr):
  assert fxtr.bark() == "abc"
  assert 0


def test_bcd(fxtr):
  assert fxtr.bark() == "abc"
  assert 0