import pytest
from click.testing import CliRunner
from src.ticket import ticket


@pytest.fixture
def runner():
    return CliRunner()


def test_ticket(runner):
    result = runner.invoke(ticket, ["run"])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, ticket'

