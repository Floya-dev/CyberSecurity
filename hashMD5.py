import random
import hashlib
from itertools import permutations, chain

def generate_all_passwords(word_list):
    """
    Generate all possible combinations of words from the list, with random capitalization.
    """
    # Generate all permutations of word combinations
    all_combinations = chain.from_iterable(
        permutations(word_list, r) for r in range(1, len(word_list) + 1)
    )

    for combination in all_combinations:
        # Generate all capitalization variations for a given combination
        num_variations = 2 ** len(combination)
        for i in range(num_variations):
            password = ""
            for index, word in enumerate(combination):
                if (i >> index) & 1:  # Randomly capitalize words
                    password += word.capitalize()
                else:
                    password += word.lower()
            yield password

def md5_hash(password):
    """
    Create an MD5 hash of the given password.
    """
    return hashlib.md5(password.encode()).hexdigest()

def main():
    # Define the target hash
    target_hash = "f1b1dc7749cbb0f581e4717e36d3475b"

    # Example word list
    word_list = ["apple", "banana", "cherry", "date", "elderberry"]

    # Generate and test all possible passwords
    for password in generate_all_passwords(word_list):
        hashed_password = md5_hash(password)

        # Check if the hash matches the target
        if hashed_password == target_hash:
            print(f"Password found: {password}")
            return

        print(f"Tried password: {password} -> {hashed_password}")

    print("Exhausted all possibilities without finding a match.")

if __name__ == "__main__":
    main()