import conftest

def test_abc1(fxtr):
  assert fxtr.bark() == "abc2"
  assert 0