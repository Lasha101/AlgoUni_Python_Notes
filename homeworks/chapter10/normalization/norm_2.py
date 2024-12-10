# # normalize_random.py
# import numpy as np

# def load_random_numbers_from_file(filename='random_numbers.txt'):
#     """
#     Load an array of random numbers from a file.
    
#     Parameters:
#     filename (str): Name of the file to load the numbers from.
    
#     Returns:
#     np.ndarray: Array of random numbers loaded from the file.
#     """
#     return np.loadtxt(filename)

# def normalize_numbers(numbers):
#     """
#     Normalize an array of numbers to the range 0-1.
    
#     Parameters:
#     numbers (np.ndarray): Array of numbers to normalize.
    
#     Returns:
#     np.ndarray: Array of normalized numbers.
#     """
#     min_val = np.min(numbers)
#     max_val = np.max(numbers)
#     return (numbers - min_val) / (max_val - min_val)

# if __name__ == "__main__":
#     # Load the random numbers from the file
#     random_numbers = load_random_numbers_from_file()
#     # Normalize the random numbers
#     normalized_numbers = normalize_numbers(random_numbers)
#     # Print the normalized numbers
#     print("Normalized numbers:", normalized_numbers)

# normalize_random.py
import numpy as np
from norm_1 import generate_random_numbers

def normalize_numbers(numbers):
    """
    Normalize an array of numbers to the range 0-1.
    
    Parameters:
    numbers (np.ndarray): Array of numbers to normalize.
    
    Returns:
    np.ndarray: Array of normalized numbers.
    """
    min_val = np.min(numbers)
    max_val = np.max(numbers)
    return (numbers - min_val) / (max_val - min_val)

if __name__ == "__main__":
    # Generate random numbers directly
    random_numbers = generate_random_numbers()
    # Normalize the random numbers
    normalized_numbers = normalize_numbers(random_numbers)
    # Print the normalized numbers
    print("Normalized numbers:", normalized_numbers)
