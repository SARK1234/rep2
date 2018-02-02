import pytest
class Test():
    def test_001(self):
        assert 1
if __name__ == '__main__':
    pytest.main("-s test_001.py")
