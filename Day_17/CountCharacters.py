# WAP to find the frequency of character in the given word
# Explanation:
# - We take a word from the user.
# - We create an empty dictionary named count.
# - We loop through each character in the word.
# - If the character is already in the dictionary, we increase its count.
# - Otherwise, we add it to the dictionary with count 1.
# - At the end, we print each character and how many times it appears.
#
# Separate logic using the count() method:
# The count() method counts how many times a specific character appears in a string.
# Example: "banana".count('a') gives 3

word = input("Enter a word: ")

print("\nUsing count() method:")

for ch in set(word):
    print(f"{ch} its count is {word.count(ch)} times")