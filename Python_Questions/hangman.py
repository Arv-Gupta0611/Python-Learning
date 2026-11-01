import random

l = [
    "Variable",
    "Function",
    "Loop",
    "Condition",
    "Array",
    "Dictionary",
    "Tuple",
    "String",
    "Integer",
    "Boolean",
    "Class",
    "Object",
    "Module",
    "Exception",
    "Algorithm"
]
word=random.choice(l).lower()
guessed_letters=[]
wrong_guesses_remaining = 6

print("Welcome to Hangman!")
while wrong_guesses_remaining>0:
    print("\n" + "="*40)
    current_display = ""
    for letter in word:
        if letter in guessed_letters:
            current_display += letter + " "
        else:
            current_display += "_ "
    print(f"Word: {current_display.strip()}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Wrong guesses remaining: {wrong_guesses_remaining}")
    guess = input("Enter a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input! Please enter a single alphabetical letter (no numbers or symbols).")
        continue
    if guess in guessed_letters:
        print(f"You already guessed the letter '{guess}'. Try a different one! (Does not count as a wrong guess)")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print(f"Good job! '{guess}' is in the word.")
        if all(letter in guessed_letters for letter in word):
            print("\n" + "="*40)
            print(f"Congratulations! You revealed all letters and won the game! The word was: {word}")
            break
    else:
        wrong_guesses_remaining -= 1
        print(f"Wrong letter! '{guess}' is not in the word.")
        if wrong_guesses_remaining == 0:
            print("\n" + "="*40)
            print(f"Game Over! You ran out of wrong guesses. The full word was: {word}")
            break