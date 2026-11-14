# Mortal Fibonacci Rabbits

A Python solution to the [Rosalind Mortal Fibonacci Rabbits](https://rosalind.info/problems/fibd/) problem.

## Problem

Starting with one pair of newborn rabbits, calculate the number of pairs remaining after `n` months when rabbits live for `m` months. Each pair begins reproducing at one month old and produces one new pair per month; rabbits die after reaching the end of their lifespan.

## Approach

Keep a list whose entries count rabbit pairs by age, from newborns to the oldest living age. Each month, the pairs old enough to reproduce become the new newborns, the other pairs age by one month, and pairs beyond the lifespan are dropped. The result is the sum of all age groups.

- Time: `O(n * m)`
- Space: `O(m)`

## Run

Requires Python 3. Run the program and provide `n m` on standard input:

```text
python practice.py
6 3
```

Output:

```text
4
```
