import requests
from colorama import init, Fore

from random import choice

from .utils import random_madlibs_url, input_phrases

# Set colorama autoreset as True
init(autoreset=True)

# Define the list for the Inputs
inputs = []

# Parse the JSON
data = requests.get(random_madlibs_url).json()

# Extract the data from JSON
blanks = data["blanks"]
title = data["title"]

values = data["value"]
values.pop()

# Show the data by printing them
print(f"TITLE: {Fore.CYAN} {title}\n")

for blank in blanks:
    inputs.append(
        input(f"{Fore.YELLOW} {choice(input_phrases).format(blank)}: ")
    )

for index in range(len(values) - 1):
   values[index] += inputs[index]

# Print the Paragraph formed
print()
print(Fore.GREEN + "".join(values))
