# generate_random.py
import numpy as np

def generate_random_numbers(count=10):
    """
    Generate an array of random integers between 1 and 99 using NumPy.
    
    Parameters:
    count (int): Number of random integers to generate.
    
    Returns:
    np.ndarray: Array of generated random integers.
    """
    return np.random.randint(1, 100, size=count)

def save_random_numbers_to_file(numbers, filename='random_numbers.txt'):
    """
    Save an array of random numbers to a file.
    
    Parameters:
    numbers (np.ndarray): Array of random numbers to save.
    filename (str): Name of the file to save the numbers in.
    """
    np.savetxt(filename, numbers, fmt='%d')

if __name__ == "__main__":
    # Generate random numbers
    random_numbers = generate_random_numbers()
    # Save the random numbers to a file
    save_random_numbers_to_file(random_numbers)
    print(f"Random numbers saved to {random_numbers}")
