import pytest
from click.testing import CliRunner
from src.cli.app import app


@pytest.fixture
def runner():
    return CliRunner()


def test_ticket(runner):
    result = runner.invoke(app, ["run"])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Hello, ticket'

