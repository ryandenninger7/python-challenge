import os
import csv

#Obtain file path and read in CSV
file_path = "Resources/election_data.csv"
PyPoll_results = "PyPoll_results.txt"

with open(file_path, encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header_row = next(csv_reader)  # Skip the header row
    #initialize variables
    total_votes = 0
    candidates_votes = {}
    most_votes = 0
    winner = ""
    #parse through csv
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        try:
            if candidate_name in candidates_votes:
                candidates_votes[candidate_name] += 1
            else:
                candidates_votes[candidate_name] = 1
        except (ValueError, IndexError):
            continue
    winner = max(candidates_votes, key=candidates_votes.get)
    #print out results into the terminal
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    for candidate, votes in candidates_votes.items():
            percentage = (votes / total_votes) * 100
            formatted_percentage = "{:.3f}%".format(percentage)
            print(f"{candidate}: {formatted_percentage} ({votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")
    #store results in a text file
    with open(PyPoll_results, 'w') as output_file:
        output_file.write("Election Results\n")
        output_file.write(f"-------------------------\n")
        output_file.write(f"Total Votes: {total_votes}\n")
        output_file.write(f"-------------------------\n")
        for candidate, votes in candidates_votes.items():
            percentage = (votes / total_votes) * 100
            formatted_percentage = "{:.3f}%".format(percentage)
            output_file.write(f"{candidate}: {formatted_percentage} ({votes})\n")
        output_file.write(f"-------------------------\n")
        output_file.write(f"Winner: {winner}\n")
        output_file.write(f"-------------------------\n")
    