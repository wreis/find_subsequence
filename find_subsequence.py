"""find_subsequence.py

Given a list of integers, find the consecutive, non-empty subsequence with the highest sum.
"""

import click
from itertools import islice
import sys

def _subseq_as_differences(iter):
    """Helper function to compute sum of absolute differences in a sequence"""

    sequence = list(iter)
    return sum(
        abs(sequence[i] - sequence[i+1])
        for i in range(0, len(sequence)-1)
    )

def _find_diff_highest_sum(sequence, length):
    """Implements logic for extended task (differences option)"""

    seq_length = len(sequence)
    subsequences = list(
        map(
            lambda seq: _subseq_as_differences(seq),
            (
                map(lambda x: x, islice(sequence, j, length+j))
                for j in range(0, seq_length-length+1)
            )
        )
    )
    return max(subsequences)

def _find_highest_sum(sequence, length):
    """Implements logic for base/original task (values option)"""

    highest_sum = []
    for i in range(2, length+1):
        subsequences = list(
            sum(
                map(lambda x: x, islice(sequence, j, i+j))
            ) for j in range(0, len(sequence)-1)
        )
        highest_sum.append( max(subsequences) )
    return max(highest_sum)

@click.command()
@click.argument(
    'input_file',
    required=True,
    type=click.File('r')
)
@click.argument('n')
@click.argument('metric')
def find_subsequence(input_file, n, metric):
    """Main function which handles input and dispatching"""

    try:
        file_content = list( map(int, input_file.readline().strip().split()) )
    except:
        print("Invalid file content")
        sys.exit(2)
    try:
        length = int(n)
        if length <= 0:
            raise ValueError('Negative integer')
    except ValueError as e:
        print("Please input a positive int as second argument")
        sys.exit(2)
    from_algo = {
        'values': lambda: _find_highest_sum(file_content, length),
        'differences': lambda: _find_diff_highest_sum(file_content, length),
    }
    try:
        highest_sum = from_algo[metric]()
        print(highest_sum)
    except KeyError as e:
        print("Please input either 'values' or 'differences' as third argument")
        sys.exit(2)

if __name__ == '__main__':
    find_subsequence()
