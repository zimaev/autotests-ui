import pytest

@pytest.mark.skip(reason="Работа в процессе")
def test_feature_in_development():
    pass

@pytest.mark.skip(reason="Работа в процессе")
class TestSuiteSkip:

    def test_feature_in_development_01(self):
        pass

    def test_feature_in_development_02(self):
        pass