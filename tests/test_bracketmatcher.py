import pytest

from src.bracketmatcher import klammer_pruefer_count, klammer_pruefer_simple, klammer_pruefer_findall

@pytest.mark.parametrize("pruefling, expected_result",
                         [("abc", 1),
                          ("", 1),
                          ("()", 1),
                          (")))(((", 1),
                          ("())(()", 1),
                          ("abc()def()", 1),
                          ("(c(oder)) b(yte)", 1),
                          ("(hello (world))", 1),
                          ("(", 0),
                          (")", 0),
                          ("(((((", 0),
                          ("))))", 0),
                          ("(coder)(byte))", 0),
                          ("((hello (world))", 0),
                          ])
def test__klammer_pruefer(pruefling, expected_result):
    assert klammer_pruefer_simple(pruefling) == expected_result
    assert klammer_pruefer_findall(pruefling) == expected_result
    assert klammer_pruefer_count(pruefling) == expected_result
