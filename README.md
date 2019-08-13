# Merantix Engineering Assignment
Assignment for Merantix Software and Data Engineers.

## Base task
Given a list of integers, find the consecutive, non-empty subsequence with the highest _sum_.

## Context
Time series are an ubiquitous type of data, appearing in many of the projects Merantix is working on.
For instance, conventional vehicles are equipped with a variety of sensors, which collect enormous amounts of data
every second. Conversely, we might have anonymized health care records of a large number of patients,
spanning multiple years, and want to identify temporal patterns to gain insight about how diseases develop over time.

To make use of this large pool of data in our pipeline, we need to identify interesting subsequences.
The task is an abstraction of this, with the list of integers representing the sensor data and the sum is the metric to evaluate if a subsequence is interesting.

## Usage
### Input:
A file path to a file with a single line that contains the integer sequence separated by space, e.g.,
```
3 -5 1 2 -1 4 -3 1 -2
```

### Output:
The command should print to stdout the _sum_ of the desired non-empty subsequence, e.g., for the input above the output would be `6` from the subsequence `1 2 -1 4`.


## Extension tasks
After finishing the first task, the following other tasks should be tackled:
* The input is extended by a second parameter `n` that restricts the maximum length of the subsequence to n.
* The input is extended by a third parameter which changes how the metric is calculated.
  Instead of the _sum_ of the values we want to find the highest _sum_ of the absolute values of the differences of neighboring pairs.
  As an example, for the input above the absolute differences would be: `8 6 1 3 5 7 4 3` and therefore the output should be `16` for `n = 4` as `-1 4 -3 1` result in the absolute differences of `5 7 4` which adds up to `16`.
  The expected input parameter is `values` for the original behavior and `differences` for the new one.

## Examples
You can find example input files in the data folder.


```
python find_subsequence.py data/input_1.txt 9 values
>> 6
```

```
python find_subsequence.py data/input_1.txt 4 differences
>> 16
```

```
python find_subsequence.py data/input_2.txt 10 values
>> 27
```

```
python find_subsequence.py data/input_2.txt 5 differences
>> 58
```

```
python find_subsequence.py data/input_3.txt 30 values
>> 44
```

```
python find_subsequence.py data/input_3.txt 10 differences
>> 40
```

## Deliverables
* Code:

    * A _compressed_ (`tar.gz`) folder with the __Python__ (version 3.7) source file(s).
      The main function should be in a file called `find_subsequence.py` and be callable as demonstrated in the examples.
      Our goal is to check your software engineering capabilities, so while this is a small task, please also think about overall common best practices such as readability, maintainability and *more*.
    * The necessary library requirements should be in a [`requirements.txt`](https://pip.pypa.io/en/stable/user_guide/#requirements-files) file next to the python sources.
    * Any additional information should reside in a `README.md` file also included in the folder.

* Time (this will not be taken into account, but will only be used to improve this exercise)
