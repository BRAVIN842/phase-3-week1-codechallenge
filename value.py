def solve(s):
    # Define a function to calculate the value of a substring
    def substring_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)

    vowels = "aeiou"
    consonant_substrings = []
    current_substring = ""

    # Iterate through the characters in the string
    for char in s:
        if char not in vowels:
            current_substring += char
        else:
            # If a vowel is encountered, calculate the value of the current consonant substring
            if current_substring:
                consonant_substrings.append(substring_value(current_substring))
                current_substring = ""

    # Check for the last consonant substring
    if current_substring:
        consonant_substrings.append(substring_value(current_substring))

    # Return the highest value among the consonant substrings
    return max(consonant_substrings, default=0)

# Test cases
print(solve("zodiacs"))   # Output: 26
print(solve("strength"))  # Output: 57
