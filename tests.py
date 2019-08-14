"""Test script"""

import pytest
from click.testing import CliRunner
from find_subsequence import find_subsequence

def test_valid_input():
    runner = CliRunner()
    result = runner.invoke(find_subsequence, ['data/input_1.txt'])
    assert result.exit_code == 0

def test_invalid_input():
    runner = CliRunner()
    result = runner.invoke(find_subsequence)
    assert result.exit_code == 2
    result = runner.invoke(find_subsequence, ['data/input_1'])
    assert result.exit_code == 2

def test_subseq():
    runner = CliRunner()
    data_dir = {
        'data/input_1.txt': "6\n",
        'data/input_2.txt': "27\n",
        'data/input_3.txt': "82\n",
    }
    for filename in data_dir.keys():
        result = runner.invoke(find_subsequence, [filename])
        assert result.output == data_dir[filename]
        assert result.exit_code == 0
