from tkinter import*
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {} # Global variable


# --------------------------------------------------------------------------------
# Step 2 create new flash cards.
# 1. Read the data from the french_words.csv file in the data folder.
# 2. Pick a random French word/translation and put the word into the flashcard.
# Every time you press the ❌ or ✅ buttons, it should generate a new random word to display. e.g.

# To protect your program crash, we need the program to read from words_to_learn.csv

try:
    # data = pandas.read_csv("data/french_words.csv")
    data = pandas.read_csv("data/words_to_learn.csv") # Every time when we run the app, it's always going to give me all the words that I've yet to learn. It's not go back to the original word

except FileNotFoundError: # In case that we cannot find that file, we will use the original file
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records") # We will get a list of each column value.
    print(to_learn)



# Create a function when you press button

def next_card():
    global current_card # To make current_class to be a global variable and keep it in empty dictionary because we will use current_card to flip_card function. Current_card is in the next_card function.
    global flip_timer
    window.after_cancel(flip_timer) # Every time we go to a new card when we click buttons, we're going to validate this timer. So we have to cancel 3s time to flip.
    current_card = random.choice(to_learn) # random for list
    eng_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black") # Change text on canvas and fill means to change the color.
    canvas.itemconfig(card_word, text=eng_word, fill="black")
    # Flip a card and change the card_back image to be a card_front image when you click the button.
    canvas.itemconfig(card_background, image=card_front_image)
    # After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
    flip_timer = window.after(3000, func=flip_card) # We have to set up a new flip_timer so taht it waits for again three seconds.



# -----------------------------------------------------------------------------------------------
# Step 3 - Flip the Cards!
# 1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.

# 2. The card image should change to the card_back.png and the text colour should change to white.
# The title of the card should change to "English" from "French".


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")  # Change text on canvas
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") # Get the value(English)
    canvas.itemconfig(card_background, image=card_back_image) # Flip image from card_front image to be a card_back image

# ------------------------------------------------------------------------------------------------

# When the user presses on the ✅ button, it means that they know the current word on the flashcard
# and that word should be removed from the list of words that might come up.

def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn) # In order to keep hold of the word that I still need to learn. If we don't save it to new file, it will go back to french_word.csv. Change to_learn list to be a dataframe
    data.to_csv("data/words_to_learn.csv", index=False) # If we don't want to add the index number in front of your data in csv file, we use index=False.
    next_card()  # Call next_card function to be a particular method.



# -------------------------------------------------------------------------------------------------

# Step 1 create the user interface (UI) with Tkinter

# Set up the window.
window = Tk() # It means to refer to tk class.
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 1. After a delay of 3s (3000ms), the card should flip and display the English translation for the current word.
flip_timer = window.after(3000, func=flip_card)


# Add image and text on image canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR) # To make the background same as window
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic")) # Create text on canvas and fix it on x and y of canvas.
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2) # it means that it starts from column o and end at column 1.


# Button
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_know)
known_button.grid(column=1, row=1)



# ----------------------------------------------------------------------------------------------
# Call function before mainloop because we want them to see French and word.

next_card()


# -------------------------------------------------------------------------------





window.mainloop()


