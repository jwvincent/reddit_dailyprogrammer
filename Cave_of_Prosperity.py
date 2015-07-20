#!/usr/bin/python

'''This code is my solution to the reddit/r/dailyprogrammer "The Cave of Prosperity" challenge. https://www.reddit.com/r/dailyprogrammer/comments/3aewlg/20150617_challenge_219_hard_the_cave_of_prosperity/'''

# import itertools
import itertools

# define function
def Cave_of_Prosperity(input_info):
    # Create a list of all the nugget's weights
    nugget_list = [x for x in input_info[2:]]
    # Create a list of all the possible combinations of
    # nuggets (DON'T UNDERSTAND)
    nugget_combinations = [c for i in range(input_info[1]) for c in itertools.combinations(nugget_list, i+1)]
    # Remove the ")," after each combination (DON'T UNDERSTAND)
    nugget_combinations = map(list, nugget_combinations)
    # Set initial max value equal to zero
    max_value = 0
    # Declare a list for the max combination of nuggets
    max_combination = nugget_list
    # Iterate through all of the combinations
    for j, k in enumerate(nugget_combinations):
        # Find value of each combination
        value = sum(k)
        # Test to see if the value of the current combination is greater than
        # the max value and less than the maximum allowable weight.
        if value >= max_value and value <= input_info[0]:
            # Set the new max value
            max_value = value
            # Set the new max combination
            max_combination = nugget_combinations[j]
    # Create the results
    results = [max_value, max_combination]
    # Return the results.
    return "The maximum weight that can be taken form the cave is " + str(results[0]) + "." + "\n" + "This can be acheeved by selecting the following nuggets: " + str(results[1]) + "."
