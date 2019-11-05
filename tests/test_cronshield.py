#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cronshield` package."""

import re

from click.testing import CliRunner

from cronshield import cli


def test_no_args():
    """Test the CLI with no args."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert "Missing argument" in result.output


def test_help():
    """Test the CLI's --help option."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert re.search(r"--help\s+Show this message and exit.", help_result.output) is not None


def test_success():
    """Test that the successful execution suppresses output."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--", "python", "-c", "import sys; print('hello'); sys.exit(0)"])
    assert help_result.exit_code == 0
    assert len(help_result.output) == 0


def test_error():
    """Test that the error is reported."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--", "python", "-c", "import sys; print('hello'); sys.exit(1)"])
    assert help_result.exit_code == 1
    assert re.search(r"cronshield detected failure or error output for the command", help_result.output) is not None
    assert "hello" in help_result.output
