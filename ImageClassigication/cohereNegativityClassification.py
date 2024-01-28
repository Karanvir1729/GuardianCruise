
import cohere
import os

from cohere.responses.classify import Example

import csv




def add_to_csv(new_data):

# CSV file path
    csv_file_path = "output.csv"

    # Check if the CSV file already exists
    file_exists = False
    try:
        with open(csv_file_path, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        pass

    # Append data to CSV file
    with open(csv_file_path, 'a', newline='') as file:
        fieldnames = ["Time", "Score "]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is created now
        if not file_exists:
            writer.writeheader()

        # Append new data
        writer.writerows(new_data)

    print(f"Data has been appended to {csv_file_path}.")

def get_scores(userScriptLst):
    co = cohere.Client('cOL5L8qHbfPK78SVMkOiKkU8tkZntE6UJL1d7jnk')  # This is your trial API key

    txt_file1 = 'negPosTxtTrain.txt'
    examples = []
    with open(txt_file1, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 2:
                examples.append(Example(parts[0], parts[1]))

    response = co.classify(
        model='embed-english-v3.0',
        inputs=reviews,
        examples=examples)
    scores = [i.labels['"positive"'].confidence - i.labels['"negative"'].confidence for i in response.classifications]
    return scores

reviews = ["I want to drive this fucking car into a tree", "dogs are cute"]
scores = get_scores(reviews)
avj = sum(scores)/len(scores)
problem = "abc"
solution = "xyz"
str = 'Good'
if avj < 0:
    str = 'Bad'
# new_data = [
#     {"Problem": problem, "Solution": solution, "AVJ": avj, "Reviews": reviews, "good/bad": str},
#     # Add more data as needed
# ]
#
# add_to_csv(new_data)
