import pytest
from dog import Dog


@pytest.fixture(scope="session", params=["dogA", "dogB"])
def fxtr(request):
    yield Dog(request.param) 
    print ("tear down")