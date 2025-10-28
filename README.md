# Play with triangular numbers

A program to generate a sequence of the first $n$ triangular numbers.

## 📝 Description

This program generates a sequence of triangular numbers. Triangular numbers represent the total number of dots in a triangle, where each new row adds one more dot than the previous.

  * The **1st** triangular number is 1.
  * The **2nd** is $1 + 2 = 3$.
  * The **3rd** is $1 + 2 + 3 = 6$.
  * The **4th** is $1 + 2 + 3 + 4 = 10$.

The program takes an integer $n$ and outputs the first $n$ numbers in this sequence as a comma-separated list.

-----

## 🎯 Problem Statement

### Input:

  * A single integer ($n$).

### Output:

  * A string of comma-separated numbers representing the first $n$ triangular numbers.
  * "NoProceed" if $n$ is not a positive integer.

### Rules:

1.  The input number **$n$** must be a **positive integer** (greater than 0).
2.  If the input is zero, negative, or a non-integer, the program should output the message **"NoProceed"**.

-----

## 💡 Examples

### Example 1 (n = 1)

**Input:**

```
1
```

**Output:**

```
1
```

**Explanation:** The first number in the sequence is 1.

### Example 2 (n = 3)

**Input:**

```
3
```

**Output:**

```
1, 3, 6
```

**Explanation:** The first 3 triangular numbers are 1, (1+2)=3, and (1+2+3)=6.

### Example 3 (n = 5)

**Input:**

```
5
```

**Output:**

```
1, 3, 6, 10, 15
```

**Explanation:** The first 5 numbers are 1, 3, 6, (1+2+3+4)=10, and (1+2+3+4+5)=15.

### Example 4 (n = 0)

**Input:**

```
0
```

**Output:**

```
NoProceed
```

**Explanation:** The input is 0, which is not a positive integer.

### Example 5 (n = -5)

**Input:**

```
-5
```

**Output:**

```
NoProceed
```

**Explanation:** The input is a negative number.

### Example 6 (n = 1.5)

**Input:**

```
1.5
```

**Output:**

```
NoProceed
```

**Explanation:** The input is not an integer.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/triangular-numbers.git
    cd triangular-numbers
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter a positive integer when prompted to see the result.
