# 🎯 Number Guessing Game (Python)

A simple Python-based game where the computer randomly selects a number between 1 and 100, and the player has to guess it in 6 attempts or fewer. The game provides helpful hints to guide the player towards the correct answer.

---

## 📌 Features

- Generates a random number between 1 and 100.
- Player has **6 attempts** to guess the number.
- Provides feedback after each guess:
  - `"Your number is Smaller ...."` if guess is too low.
  - `"Your number is Bigger  ..."` if guess is too high.
  - `"Congratulations!"` when the guess is correct.
- Handles invalid inputs (non-numeric values).
- Displays the total number of attempts taken upon a correct guess or game over.

---

## 🧠 How It Works

1. A random number is generated using Python's `random` module.
2. The user is prompted to enter a guess.
3. After each guess:
   - The game tells the user if their guess is too high or too low.
   - The number of attempts is counted.
4. The game ends either when:
   - The user correctly guesses the number, or
   - The user runs out of 6 attempts.

---

## 💡 Example Gameplay



Welcome to the Number guessing game!
I selected a number from 0 to 100, now you have to guess it under 6 turns....
Enter a number to guess: 25
Your number is Smaller ....

Enter a number to guess: 50
Your number is Bigger  ...

Enter a number to guess: 40
Congratulations! You guessed the 40 in 3 attempts.

`

---

## 🚀 Getting Started

1. Make sure Python is installed on your system.
2. Clone this repository or copy the Python file.
3. Run the script using:

bash
python guess_game.py
`

---

## 🛠️ Tech Used

* **Python 3**
* **random module** (for number generation)
* **Exception handling** (for user input)

---

## ✅ Improvements You Can Add

* Track high scores or store the best attempt count.
* Allow the user to play again after a round ends.
* Add difficulty levels (Easy, Medium, Hard).
* Create a GUI using Tkinter for a graphical interface.

---

## 📂 Author

**Ahmad**
GitHub: [Ahmad2627](https://github.com/Ahmad2627)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
