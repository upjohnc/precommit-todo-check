from pre_commit_hook import todo_check


def test_line_number():
    """
    Test that the line number for a given text is correct
    """
    input_text = "thing\nother todo "
    line_numbers = todo_check.check_contain_bad_text(input_text)
    assert [2] == line_numbers


def test_no_line_number():
    """
    Test that an empty string is returned if no bad lines
    """
    input_text = "nothing\nandth en more \n  of nothing"
    line_numbers = todo_check.check_contain_bad_text(input_text)
    assert [] == line_numbers
