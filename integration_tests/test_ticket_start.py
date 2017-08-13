import pytest
from click.testing import CliRunner
from ticket.cli.app import app


@pytest.fixture
def runner():
    return CliRunner()


def test_start_fails_without_an_argument(runner):
    result = runner.invoke(app, ["start"])
    assert result.exit_code != 0


def test_start_fails_with_an_invalid_ticket_number(runner):
    result = runner.invoke(app, ["start", "bla"])
    assert result.exit_code != 0
