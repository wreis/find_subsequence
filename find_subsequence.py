"""find_subsequence.py

Given a list of integers, find the consecutive, non-empty subsequence with the highest sum.
"""

import click
from itertools import islice

def _find_highest_subseq(sequence, size):
    subsequences = list(
        sum( map(int, islice(sequence, j, size+j, 1)) ) for j in range(0, len(sequence)-1)
    )
    return max(subsequences)

@click.command()
@click.argument(
    'input_file',
    required=True,
    type=click.File('r')
)
def find_subsequence(input_file):
    file_content = input_file.readline().strip().split()
    highest_sum = []
    for i in range(2, len(file_content)+1):
        subseq = _find_highest_subseq(file_content,i)
        highest_sum.append( subseq )
    print( max(highest_sum) )

if __name__ == '__main__':
    find_subsequence()
