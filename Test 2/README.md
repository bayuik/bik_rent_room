# Maximum Proficiency Level Calculation

This Python script calculates the maximum proficiency level Juned can achieve in a sports match scenario, given an initial proficiency level, opponents' proficiency levels, and proficiency increases upon defeating each opponent.

## Problem Description

Juned can choose the order in which he fights opponents, and he can only fight those with proficiency levels lower than or equal to his own. After each win, his proficiency level increases. The goal is to determine the highest proficiency level he can achieve.

## Input Format

The input includes:
1. `N` (number of opponents) and `M` (initial proficiency level of Juned)
2. A list `A` representing opponents' proficiency levels.
3. A list `B` representing the increase in proficiency upon defeating each opponent.

## Output Format

The output is the maximum proficiency level that Juned can reach.

## Example

For example, with the input:
```plaintext
N = 4, M = 2
A = [8, 9, 3, 2]
B = [5, 4, 1, 3]

```

The output will be:
Output 1: 6

## Requirements
Python 3.x

## Running the Code
1. Clone this repository.
2. Run the script using Python:
```
python maximum_proficiency_level.py
```

The script will output the maximum proficiency level for each example provided.
```
Output 1: 6
Output 2: 3
Output 3: 23
```