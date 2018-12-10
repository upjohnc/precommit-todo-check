from pre_commit_hook.todo_check import check_contain_bad_text


def test_pdb():
    result = check_contain_bad_text('import pdb; pdb.set_trace()')
    assert result


def test_todo():
    result = check_contain_bad_text('# todo')
    assert result
