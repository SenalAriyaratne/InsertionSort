
# Insertion Sort Implementation

This repository contains a Python implementation of the Insertion Sort algorithm. It includes three main files:

- `__init__.py`: Initialization file for the module.
- `InsertionSort.py`: Contains the `InsertionSort` class which implements the Insertion Sort algorithm.
- `main.py`: Example usage of the `InsertionSort` class and testing of the sorting functionality.

## Files

### `__init__.py`

This file initializes the Python modulee.

### `InsertionSort.py`

This file contains the `InsertionSort` class with methods to sort an array using the Insertion Sort algorithm and print the array.

### `main.py`

This file demonstrates the usage of the `InsertionSort` class. It includes:
- Creating an instance of the `InsertionSort` class with a sample array.
- Printing the original array.
- Sorting the array.
- Printing the sorted array.
- Comparing the sorted array with a correctly sorted array to verify the sorting.

## How to Run

1. Clone the repository:
   ```sh
   git clone https://github.com/SenalAriyaratne/InsertionSort.git
   cd insertion-sort
   ```

2. Make sure you have Python installed on your system. This code is compatible with Python 3.

3. Run the `main.py` file to see the Insertion Sort in action:
   ```sh
   python main.py
   ```

## Example

The `main.py` file will output the following:

```
Original array:
[34, 8, 64, 51, 32, 21, 45, 73, 17, 3, 99, 45, 67, 28, 73, 58, 82, 10, 1, 87, 42, 16, 70, 25, 93, 12, 37, 48]
Sorted array:
[1, 3, 8, 10, 12, 16, 17, 21, 25, 28, 32, 34, 37, 42, 45, 45, 48, 51, 58, 64, 67, 70, 73, 73, 82, 87, 93, 99]
Correct sorted array:
[1, 3, 8, 10, 12, 16, 17, 21, 25, 28, 32, 34, 37, 42, 45, 45, 48, 51, 58, 64, 67, 70, 73, 73, 82, 87, 93, 99]
Test passed: The array is sorted correctly.
```

## License

This project is licensed under the MIT License.
