import hashlib
from itertools import permutations, chain, product
def generate_all_passwords(word_list):
    """
    Generate all possible combinations of words from the list, including capitalization variations.
    """
    all_combinations = chain.from_iterable(
        permutations(word_list, r) for r in range(1, len(word_list) + 1)
    )
    for combination in all_combinations:
        for caps_variation in product([str.lower, str.capitalize], repeat=len(combination)):
            yield "".join(caps_func(word) for caps_func, word in zip(caps_variation, combination))
def md5_hash(password):
    """
    Compute the MD5 hash of a password.
    """
    return hashlib.md5(password.encode()).hexdigest()
def main():
    target_hash = "f1b1dc7749cbb0f581e4717e36d3475b"
    word_list = ["la", "los", "angeles", "beach", "venice", "sunny", "days", "and", "sandy", "beaches", "california", "dreamin", "cute", "snowball", "cat", "white", "starbucks", "coffee", "morning", "routine", "desert", "oasis", "music", "magic", "coachella", "festival", "vibes", "calvin", "harris", "marshmello", "miami", "florida", "20", "yo", "party", "endless", "dancing"]
    print("Starting password generation and hash checking...")
    for password in generate_all_passwords(word_list):
        hashed_password = md5_hash(password)
        if hashed_password == target_hash:
            print(f"\nPassword found: {password}")
            return
    print("\nExhausted all possibilities without finding a match.")

if __name__ == "__main__":
    main()
