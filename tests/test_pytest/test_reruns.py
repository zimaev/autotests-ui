import random
import pytest

PLATFORM = "Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски реализуеются на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])


@pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Windows")  # Перезапуск при выполнении условия
def test_rerun_with_condition():
    assert random.choice([True, False])
