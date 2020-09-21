from pre_commit_hook.todo_check import check_contain_bad_text


def test_pdb():
    """
    Test that regex picks up usage of pdb
    GIVEN: text with `import pdb`
    WHEN: run check for bad text
    THEN: returns True
    """
    result = check_contain_bad_text("import pdb; pdb.set_trace()")
    assert result


def test_todo():
    """
    Test that regex picks up `todo` in text
    GIVEN: text with `todo`
    WHEN: run check for bad text
    THEN: returns True
    """
    result = check_contain_bad_text("# todo")
    assert result
