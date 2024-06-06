# Student Progression Outcome Program

## Overview

This Python program calculates and records student progression outcomes based on their credit marks. The program provides functionalities for entering marks, validating them, categorizing outcomes, displaying results, and generating a histogram. The outcomes include Progress, Progress (module trailer), Do not progress - module retriever, and Exclude.

## Features

1. **Input and Validation**: 
   - Prompts the user to enter credits at pass, defer, and fail.
   - Validates that the entered values are within the expected range and are multiples of 20.
   - Ensures the total credits equal 120.
2. **Progression Outcome Calculation**:
   - Determines the progression outcome based on the entered credits.
3. **Multiple Outcomes Entry**:
   - Allows the user to enter multiple sets of data.
4. **List Extension**:
   - Displays all entered data categorized by progression outcomes.
5. **File Handling**:
   - Saves progression outcomes to a text file.
6. **Histogram**:
   - Generates a graphical histogram to visualize the number of each type of progression outcome.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- `graphics.py` module available in your Python environment (this module is typically part of the Zelle graphics package).

### Code Structure

- **Main Script**: Handles user input, validation, and outcome categorization.
- **List Extension**: Displays all recorded outcomes.
- **File Handling**: Saves the recorded outcomes to a text file.
- **Histogram**: Renders a graphical representation of the outcomes.

## Usage

### Part 1: Input and Validation

The program prompts the user to enter credits for pass, defer, and fail. It validates the input and calculates the progression outcome:

```python
#validation
print("Part 1:")
def get_pass_mark():
  while True:
    try:
      pass_mark = int(input("\nPlease enter your credits at pass: "))
      if 0 <= pass_mark <= 120 and pass_mark % 20 == 0:
        return pass_mark
      else:
        print("Out of range.")
    except ValueError:
      print("Integer required")
# Similar functions for defer and fail marks...
```

### Part 2: List Extension

Displays all recorded outcomes categorized by their types:

```python
print("\nPart 2:")
for i in progress_list:
    print("Progress -", i)
# Similar loops for trailer, retriever, and exclude lists...
```

### Part 3: File Handling

Saves the recorded outcomes to a text file:

```python
print("\nPart3:")
text = open("Progression file.txt", "w")
text.close()
for i in range(len(progress_list)):
    print("Progress -", *progress_list[i])
    with open("Progression file.txt", "a") as text:
        content = f"Progress - {progress_list[i]}\n"
        text.write(content)
        text.close()
# Similar loops for trailer, retriever, and exclude lists...
```

### Histogram

Generates a graphical representation of the outcomes using the `graphics.py` module:

```python
def render_graph(progress, trailer, retriever, exclude, total, additional_text):
    win = GraphWin("Histogram", 600, 600)
    win.setBackground("mint cream")
    # Drawing bars and text...
    win.getMouse()  # Wait for a mouse click to close the window
    win.close()
render_graph(progress, trailer, retriever, exclude, total, additional_text)
```

## Contributing

Feel free to contribute to the project by submitting pull requests. Please ensure your code follows the existing coding style and includes relevant comments and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project is an educational example for managing and visualizing student progression outcomes using Python.

---

**Note**: Ensure you have the `graphics.py` module in your working directory or installed in your Python environment for the histogram functionality to work.

---

Happy Coding!
