"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int = 0):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layer_numbers: int = 0):
	"""Calculate the bake preparation time
	
	:param layer_numbers: int - number of layers to be prepared
	:return: int - time (in minutes) required to prepare all layers

	Function that takes the amount of layers the lasagna has and returns
	how many minutes will it take to prepare based on the `PREPARATION_TIME`
	"""

	return PREPARATION_TIME * layer_numbers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
	"""Calculate the total time remaining for finishing the lasagna

	:param number_of_layers: int - number of lasagna layers to be prepared
	:param elapsed_bake_time: int - number of minutes the lasagna has already been in the oven
	:return: int - total of remaining minutes to finish the recipe

	Function that takes the amount of layers to be prepared and the actual minutes the lasagna
	has been in the oven as arguments and returns how many minutes the lasagna still needs to
	be completely cooked
	"""

	return bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)
