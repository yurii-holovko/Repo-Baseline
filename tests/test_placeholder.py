import pytest

from main import DEFAULT_PORT, build_welcome_message, get_port, parse_port


def test_build_welcome_message_defaults_name():
    message = build_welcome_message("", 8000)
    assert message == "Hello, World! Listening on 8000."


def test_get_port_defaults_when_env_missing(monkeypatch):
    monkeypatch.delenv("APP_PORT", raising=False)
    assert get_port() == DEFAULT_PORT


def test_get_port_reads_env(monkeypatch):
    monkeypatch.setenv("APP_PORT", "5000")
    assert get_port() == 5000


def test_parse_port_rejects_non_integer():
    with pytest.raises(ValueError, match="integer"):
        parse_port("not-a-number")


def test_parse_port_rejects_out_of_range():
    with pytest.raises(ValueError, match="between"):
        parse_port("70000")
