#!/usr/bin/python

"""Input parser for the Cave of Properity program."""

# Define function
def text_parser(arg):
    # Remove any white space
    working_data = arg.replace(" ", "")
    # Split by new line ("\n")
    data = working_data.split("\n")
    # Return cleaned data
    return data
