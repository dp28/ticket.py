import pytest
from click.testing import CliRunner
from src.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_start_fails_without_an_argument(runner):
    result = runner.invoke(cli, ["start"])
    assert result.exit_code != 0


def test_start_fails_with_an_invalid_ticket_number(runner):
    result = runner.invoke(cli, ["start", "bla"])
    assert result.exit_code != 0