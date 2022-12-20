import itertools

# Create a list of the digits 0 through 9
digits = [str(i) for i in range(10)]

# Open a file for writing
with open("combinations.txt", "w") as f:
  # Use the itertools library to generate all the combinations of the digits
  for combination in itertools.permutations(digits, len(digits)):
    # Join the digits together to form a word
    word = "".join(combination)
    # Write the word to the file
    f.write(word + "\n")