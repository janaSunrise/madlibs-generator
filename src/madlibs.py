import requests
from colorama import init, Fore

from random import choice

init(autoreset=True)

# Define the Input Variables
min_length = 5
max_length = 20

random_madlibs_url = f"https://madlibz.herokuapp.com/api/random?minlength={min_length}&maxlength={max_length}"

# Define the input phrases
input_phrases = [
    "Enter a {}",
    "Tell me a {}",
    "May I have a {}",
    "Can you think of a {}",
    "I would like to know a {}",
    "Do you know a {}"
]

# Define the list for the Inputs
inputs = []

# Parse the JSON
data = requests.get(random_madlibs_url).json()

blanks = data["blanks"]
title = data["title"]

values = data["value"]
values.pop()

print(f"TITLE: {Fore.CYAN} {title}\n")

for blank in blanks:
    inputs.append(
        input(f"{Fore.YELLOW} {choice(input_phrases).format(blank)}: ")
    )

for index in range(len(values) - 1):
   values[index] += inputs[index]

print()
print(Fore.GREEN + "".join(values))
