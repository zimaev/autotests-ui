import pytest


@pytest.mark.xfail(reason="JIRA-312")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="JIRA-344")
def test_without_bug():
    pass
