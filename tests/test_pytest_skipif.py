import pytest

SYSTEM_VERSION = "1.2.0"


@pytest.mark.skipif(
    condition=SYSTEM_VERSION == "1.3.0",
    reason="Версия ОС")
def test_system_version_valid():
    pass


@pytest.mark.skipif(
    condition=SYSTEM_VERSION == "1.2.0",
    reason="Версия ОС")
def test_system_version_invalid():
    pass
