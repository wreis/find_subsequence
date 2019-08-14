"""Test script"""

import pytest
from click.testing import CliRunner
from find_subsequence import find_subsequence

def test_valid_input():
    runner = CliRunner()
    result = runner.invoke(find_subsequence, ['data/input_1.txt', '9', 'values'])
    assert result.exit_code == 0

def test_invalid_input():
    runner = CliRunner()
    result = runner.invoke(find_subsequence)
    assert result.exit_code == 2
    result = runner.invoke(find_subsequence, ['data/input_1'])
    assert result.exit_code == 2

def test_subseq():
    data_dir = {
        'data/input_1.txt': [
            {
                'n': '9',
                'metric': 'values',
                'out': "6\n",
            },
            {
                'n': '4',
                'metric': 'differences',
                'out': "16\n",
            },
        ],
        'data/input_2.txt': [
            {
                'n': '20',
                'metric': 'values',
                'out': "27\n",
            },
            {
                'n': '10',
                'metric': 'values',
                'out': "27\n",
            },
            {
                'n': '5',
                'metric': 'differences',
                'out': "58\n",
            },
        ],
        'data/input_3.txt': [
            {
                'n': '100',
                'metric': 'values',
                'out': "82\n",
            },
            {
                'n': '30',
                'metric': 'values',
                'out': "44\n",
            },
            {
                'n': '10',
                'metric': 'differences',
                'out': "40\n",
            },
        ],
    }
    for filename in data_dir.keys():
        for case in data_dir[filename]:
            runner = CliRunner()
            result = runner.invoke(
                find_subsequence, [filename, case['n'], case['metric']]
            )
            assert result.output == case['out']
            assert result.exit_code == 0
