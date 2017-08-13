from ticket.cli import output


def test_show_prints_to_stdout(capsys):
    output.show('test')
    out, err = capsys.readouterr()
    assert out == 'test\n'


def test_show_error_prints_to_stderr(capsys):
    output.show_error('fail')
    out, err = capsys.readouterr()
    assert err == 'fail\n'
