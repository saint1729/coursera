# Fibonacci Number

<center><img src="logo.png" height="200px"></center>

Fibonacci numbers are defined recursively: $F_0=0$, $F_1=1$,
and $F_n=F_{n-1}+F_{n-2}$ for $n \ge 1$.
This definition results in the recursive function `compute_fibonacci_number_naive`
that you see on the left in the file `fibonacci_number.py`.

# Running the Naive Solution
Try to compute $F_{10}$ using this function.
For this, comment out everything except for the
implementation of the `fibonacci_number_naive` function
and add the line
```
print(fibonacci_number_naive(10))
```
to the end of the file and press the green Run button
at the top left corner of the Python file. You'll see that it will print the result (55) in the
Run pane at the bottom in blink of an eye. Now, change 10 to 40 and press the Run button again. You'll see
that the solution hangs and does not print anything. Stop it by pressing the red Stop button in the Run pane.

Let's try to understand why our current solution hangs.
To this end, let's add *debug printing* to the `fibonacci_number_naive` function:
add the line
```
print("Compute F sub", n)
```
to the beginning of the function and run it again.
You'll see a seemingly endless series of recursive calls in the Run pane:
```
Compute F sub 1
Compute F sub 0
Compute F sub 7
Compute F sub 6
Compute F sub 5
Compute F sub 4
Compute F sub 3
Compute F sub 2
Compute F sub 1
Compute F sub 0
Compute F sub 1
Compute F sub 2
Compute F sub 1
Compute F sub 0
Compute F sub 3
```
This output, in particular, reveals the reason why our
current solution is so slow:
*it computes the same thing again many times*.


# Task

## Implement an Efficient Solution
Implement the `fibonacci_number` function.
Make sure to avoid recomputing the same thing again.


## Test Your Solution
Now, switch to the file `fibonacci_number_unit_tests.py`.
It consists of several unit tests. The function `test_small`
checks that your implementation computes the same as the naive one
for all $0 \le n < 8$ (this is affordable,
since for $n < 8$ the
`fibonacci_number_naive` is fast enough).
The function `test_large`
checks that your implementation computes $F_{30}$, $F_{35}$, and
$F_{40}$ correctly.

Enter the value of $F_{35}$ to the placeholder and
run the unit tests by pressing the green Execute button.
Make sure that all tests pass.

## Check Your Solution
Finally, press the "Check Task" button in the
Task Description pane. If everything is OK,
submit to Coursera/edX.

<div class='hint'>Compute the value of the 35-th Fibonacci number and add it here. This way, the function test_large will also check that your implementation computes $F_{35}$ correctly.</div>
