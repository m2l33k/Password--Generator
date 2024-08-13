# Password--Generator
# Password Generator

A simple Password Generator application built using Python. This app allows users to generate secure, random passwords with customizable options such as length and character types.

## Features

- Generate random passwords with specified length.
- Customize password complexity with options for including uppercase letters, lowercase letters, digits, and special characters.
- Easy-to-use graphical user interface (GUI) built with Tkinter.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/m2l33k/Password--Generator.git
    cd Password--Generator
    ```

2. **Install Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/).

3. **Install Dependencies**: This project uses the `tkinter` library, which is typically included with Python. If you're using a virtual environment or a minimal installation, ensure Tkinter is installed:

    ```bash
    pip install tk
    ```

4. **Run the Application**: Execute the Python script to start the Password Generator:

    ```bash
    python password_generator.py
    ```

## Code Overview

The `password_generator.py` script includes the following key components:

- **Tkinter GUI**: Provides a user-friendly interface for generating passwords.
- **Password Generation Logic**: Uses Python's `random` module to create secure passwords based on user-selected criteria.
- **Customization Options**: Allows users to specify the length of the password and whether to include uppercase letters, lowercase letters, digits, and special characters.


Usage

    Set the desired password length in the input field.
    Select the character types to include in the password by checking the appropriate boxes.
    Click the "Generate Password" button to generate and display the password.


