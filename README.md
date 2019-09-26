# Description

Utility to evaluate if a subsequence is interesting

## Setup

This package contains a handy docker image setup which will run automated tests and
can be used for futther development in an isolated env.

To build the image run:

    $ docker build -t merantix .

this should output something along these lines:

    =========================== 3 passed in 0.18 seconds ===========================

## Install

    $ pip install .

then

    $ find_subsequence data/input_1.txt 9 values

or

    $ python find_subsequence.py data/input_1.txt 9 values
