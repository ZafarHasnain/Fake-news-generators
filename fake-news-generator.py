# import random

# subjects = [
#     "Shahid Afridi",
#     "Shoaib Akhtar",
#     "Shoaib Malik",
#     "Cafe Islamabad",
#     "Badshahi Killa",
#     "Yaadgar Lahore",
#     "Railway Station",
# ]

# actions = [
#     "celebrates",
#     "dances",
#     "dines",
#     "launches",
#     "attends a meeting",
#     "hosts a party",
# ]

# things_places = [
#     "at Jahangir Villa",
#     "in the Railway Station",
#     "in Orange Train",
#     "at Bus Stand",
#     "at Niazi Express",
#     "in a PSL match",
#     "where a big party took place",
# ]

# while True:
#     # pick random words
#     sub = random.choice(subjects)
#     action = random.choice(actions)
#     place = random.choice(things_places)

#     # create headline
#     headline = f"Breaking News: {sub} {action} {place}"
#     print("\n" + headline)

#     # ask user
#     user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()

#     if user_input == "no":
#         print("Exiting... Goodbye!")
#         break



# #upgraded version with more features
# import random
# from datetime import datetime

# subjects = [
#     "Shahid Afridi",
#     "Shoaib Akhtar",
#     "Shoaib Malik",
#     "Cafe Islamabad",
#     "Badshahi Killa",
#     "Yaadgar Lahore",
#     "Railway Station",
# ]

# actions = [
#     "celebrates",
#     "dances",
#     "dines",
#     "launches",
#     "attends a meeting",
#     "hosts a party",
# ]

# things_places = [
#     "at Jahangir Villa",
#     "in the Railway Station",
#     "in Orange Train",
#     "at Bus Stand",
#     "at Niazi Express",
#     "in a PSL match",
#     "where a big party took place",
# ]

# # file to save headlines
# file_name = "headlines.txt"

# def generate_headline():
#     sub = random.choice(subjects)
#     action = random.choice(actions)
#     place = random.choice(things_places)
#     time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     headline = f"[{time_stamp}] Breaking News: {sub} {action} {place}"
#     return headline

# while True:
#     # ask how many headlines user wants
#     try:
#         count = int(input("\nHow many headlines do you want? (e.g. 1, 3, 5): "))
#     except ValueError:
#         print("Please enter a valid number!")
#         continue

#     headlines = []
#     for _ in range(count):
#         h = generate_headline()
#         print("\n" + h)
#         headlines.append(h)

#     # save to file
#     with open(file_name, "a", encoding="utf-8") as f:
#         for h in headlines:
#             f.write(h + "\n")

#     print(f"\n✅ {count} headline(s) saved to {file_name}")

#     # ask user
#     user_input = input("\nDo you want more headlines? (yes/no): ").strip().lower()
#     if user_input == "no":
#         print("Exiting... Goodbye dost! 👋")
#         break



#upgraded version with best features
#Final Social Media Style Code

import random
from datetime import datetime

subjects = [
    "Shahid Afridi",
    "Shoaib Akhtar",
    "Shoaib Malik",
    "Cafe Islamabad",
    "Badshahi Killa",
    "Yaadgar Lahore",
    "Railway Station",
]

actions = [
    "celebrates 🎉",
    "dances 💃",
    "dines 🍽️",
    "launches 🚀",
    "attends a meeting 📋",
    "hosts a party 🎊",
]

things_places = [
    "at Jahangir Villa 🏠",
    "in the Railway Station 🚉",
    "in Orange Train 🚆",
    "at Bus Stand 🚌",
    "at Niazi Express 🏢",
    "in a PSL match 🏏",
    "where a big party took place 🎶",
]

hashtags = [
    "#TrendingNow",
    "#Viral",
    "#JustIn",
    "#BreakingNews",
    "#LOL",
    "#Pakistan",
    "#NewsUpdate",
]

file_name = "headlines.txt"

def generate_headline():
    sub = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(things_places)
    hashtag = random.choice(hashtags)
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    headline = f"[{time_stamp}] 🚨 Breaking News: {sub} {action} {place} {hashtag}"
    return headline

while True:
    try:
        count = int(input("\nHow many headlines do you want? (e.g. 1, 3, 5): "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    headlines = []
    for _ in range(count):
        h = generate_headline()
        print("\n" + h)
        headlines.append(h)

    # save to file
    with open(file_name, "a", encoding="utf-8") as f:
        for h in headlines:
            f.write(h + "\n")

    print(f"\n✅ {count} headline(s) saved to {file_name}")

    user_input = input("\nDo you want more headlines? (yes/no): ").strip().lower()
    if user_input == "no":
        print("👋 Exiting... Goodbye dost!")
        break



