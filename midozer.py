"""
This module contains the say_hello function.
"""

def say_hello(name):
    """
    Greets the user with a personalized message.

    Parameters:
    - name (str): The name of the person to greet.

    Returns:
    str: A greeting message containing the input name.
    """
    msg = "Hello"
    return f"{msg} {name}"

say_hello("Python")
