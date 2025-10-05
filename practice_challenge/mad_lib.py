# Mad Libs Generator with Conditional Statements

# Step 1: Ask the user for adjectives
adj1 = input("Enter an adjective (e.g., beautiful, sunny): ")
adj2 = input("Enter another adjective (e.g., funny, scary): ")
adj3 = input("Enter a third adjective (e.g., majestic, lazy): ")
adj4 = input("Enter one last adjective (e.g., wild, crazy): ")

# Step 2: Build the story with user words
story = f"On a {adj1} day, I went to the zoo. "
story += f"I saw a {adj2} monkey swinging from the trees. "
story += f"Then, I spotted a {adj3} lion lounging in the sun. "
story += f"What a {adj4} experience!"

# Step 3: Add conditional variation
if adj4.lower() == "crazy":
    story += " The zookeeper even asked me to calm down because I was laughing so hard!"
elif adj4.lower() == "boring":
    story += " Honestly, I expected more excitement at the zoo."
else:
    story += " I’ll never forget this adventure!"

# Step 4: Print the final story
print("\n--- Your Mad Libs Story ---")
print(story)