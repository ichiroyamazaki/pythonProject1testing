# pythonProject1testing

**pythonProject1testing** is a beginner-level Python project exploring recursive function calls to determine whether an integer is even or odd.

The project demonstrates function definitions, recursion, conditional statements, console input, and output. The current implementation requires a correction to the missing `is_even()` function before it can run successfully.

## Features

- Accepts an integer from the user.
- Demonstrates recursive function calls.
- Uses conditional statements to handle a base case.
- Displays an even-or-odd result when the required functions are correctly implemented.
- Provides a starting point for learning recursion and function relationships in Python.

## Requirements

- Python 3
- A Python-compatible IDE or code editor, such as PyCharm or Visual Studio Code, or a terminal

## Project Structure

```text
pythonProject1testing/
├── main.py
├── README.md
└── pyvenv.cfg
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ichiroyamazaki/pythonProject1testing.git
```

### 2. Open the Project Directory

```bash
cd pythonProject1testing
```

### 3. Run the Program

```bash
python main.py
```

Depending on your system, use:

```bash
python3 main.py
```

**Note:** The current source code will not run successfully because `is_even()` is referenced but not defined.

## How It Is Intended to Work

The program is designed to:

1. Ask the user to enter an integer.
2. Determine whether the number is even or odd.
3. Use recursive function calls to reach a base case.
4. Display the result in the console.

The existing `is_odd(num)` function returns `False` when `num` is zero. Otherwise, it attempts to call `is_even(num - 1)`. The program also calls `is_even(num)` to determine which message to display.

To complete the intended logic, define `is_even()` and ensure that both functions handle their base cases and recursive calls correctly.

## Example of Expected Output

For a corrected implementation, the output should resemble:

```text
Enter a number: 8
8 is an even number.
```

Another example:

```text
Enter a number: 7
7 is an odd number.
```

These examples describe the intended behavior, not the output of the current unmodified source.

## Concepts Demonstrated

- **Functions:** Organizes logic into reusable blocks.
- **Recursion:** Demonstrates a function calling another function as part of a recursive process.
- **Conditional Statements:** Uses `if` and `else` to handle different conditions.
- **Console Input:** Uses `input()` to receive a value from the user.
- **Type Conversion:** Converts the entered value to an integer using `int()`.
- **Console Output:** Displays the result using `print()`.

## Known Issues and Limitations

- The `is_even()` function is referenced but not defined.
- The current implementation raises a `NameError` before it can display the intended result.
- Negative integers are not explicitly handled.
- Non-integer input causes a `ValueError`.
- The intended even-or-odd checking logic needs to be completed and tested.

## Author

**Ichiro Yamazaki**

## License

No license is specified in this repository. Check the repository for licensing information before redistributing or modifying the project.
