import random

# Task 1: Create a list of at least 15 words (Theme: Programming terms)
words_list = [
    "variable",
    "function",
    "loop",
    "condition",
    "array",
    "dictionary",
    "tuple",
    "string",
    "integer",
    "boolean",
    "class",
    "object",
    "module",
    "exception",
    "algorithm"
]

# Pick one word randomly using random.choice()
word = random.choice(words_list)
guessed_letters = []
wrong_guesses_remaining = 6

print("Welcome to Hangman!")

# Game Loop (Task 2 & Task 3)
while wrong_guesses_remaining > 0:
    print("\n" + "="*40)
    
    # 1. Show the current state of the word
    current_display = ""
    for letter in word:
        if letter in guessed_letters:
            current_display += letter + " "
        else:
            current_display += "_ "
    print(f"Word: {current_display.strip()}")
    
    # 2. Show which letters have been guessed already
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    
    # 3. Show how many wrong guesses remain[cite: 1]
    print(f"Wrong guesses remaining: {wrong_guesses_remaining}")
    
    # 4. Ask for a letter[cite: 1]
    guess = input("Enter a letter: ").lower()
    
    # --- Task 3: Input Validation ---
    # Check if the player enters more than one character or a number/symbol[cite: 1]
    if not guess.isalpha() or len(guess) != 1:
        print("❌ Invalid input! Please enter a single alphabetical letter (no numbers or symbols).")
        continue
        
    # Check if the player enters a letter they have already guessed[cite: 1]
    if guess in guessed_letters:
        print(f"⚠️ You already guessed the letter '{guess}'. Try a different one! (Does not count as a wrong guess)")
        continue
        
    # Add the valid guess to our tracking list
    guessed_letters.append(guess)
    
    # 2. Check if the guessed letter is in the word[cite: 1]
    if guess in word:
        print(f"✅ Good job! '{guess}' is in the word.")
        
        # Check if the player has revealed all letters (win condition)[cite: 1]
        if all(letter in guessed_letters for letter in word):
            print("\n" + "="*40)
            print(f"🎉 Congratulations! You revealed all letters and won the game! The word was: {word}")
            break
    else:
        wrong_guesses_remaining -= 1
        print(f"❌ Wrong letter! '{guess}' is not in the word.")
        
        # Check if the player ran out of wrong guesses (lose condition)[cite: 1]
        if wrong_guesses_remaining == 0:
            print("\n" + "="*40)
            print(f"💀 Game Over! You ran out of wrong guesses. The full word was: {word}")
            break