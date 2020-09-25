import pytest
from pre_commit_hook.todo_check import check_contain_bad_text, regex_todo


def test_pdb():
    """
    Test that regex picks up usage of pdb
    GIVEN: text with `import pdb`
    WHEN: run check for bad text
    THEN: returns True
    """
    result = check_contain_bad_text("import pdb; pdb.set_trace()")
    assert result


good_todo = [
    " todo ",
    "todo",
    "#todo",
    "#TOdo",
    "#  todo",
    "#to do",
    "todo ",
    " to do",
    " to do ",
    "to do ",
]
bad_todo = ["1todo1", "atodo", "todob", "asto doolo", "asto do", "to doolo"]


@pytest.mark.parametrize("given", good_todo)
def test_regex_good(given):
    """
    Test good regex string
    """
    result = regex_todo(given)
    assert result


@pytest.mark.parametrize("given", bad_todo)
def test_regex_bad(given):
    """
    Test bad regex string
    """
    result = regex_todo(given)
    assert not result
