import csv
import os

#Create file path for csv import
path = os.path.join("Resources", "election_data.csv")


#sean recommends making this section a function using 'def'
#Define how to read in the csv
def read_file(path):
    with open(path) as f:
        csvreader = csv.reader(f, delimiter=',')
        header = next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return data

#Define how to count the votes
def vote_count(data):
    candidates = {}
    total_votes = 0
    for row in data:
        candidate = row[2]
        total_votes += 1
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1
    return [candidates, total_votes]

#Define how to calculate the results
def calculate_results(candidates, total_votes):
    winning_votes = 0
    winner = ''
    for candidate, votes in candidates.items():
        if votes > winning_votes:
            winner = candidate
            winning_votes = votes
    print_winner = f'The winner is {winner} with {winning_votes} votes!'
    print_candidates = ''
    for candidate, votes in candidates.items():
        print_candidates = print_candidates+f'{candidate}: {votes} votes ({int(round((votes/total_votes)*100, 2))}%)\n'
    

    results = f'{print_winner}\n-------------------------------------\n{print_candidates}'
    return results

#Define how we want to print this to the console
def printresults(path):
    vote_csv = read_file(path)
    candidates, total_votes = vote_count(vote_csv)
    results = calculate_results(candidates, total_votes)
    print(results)
    #Ask whether we want to save an output file of the results
    save_results = input('Do you want to save the output? (y/n)\n')
    if save_results=='y':
        with open('Pypoll_Results.txt', 'w') as doc:
            doc.write(save_results)

#print results in console
printresults(path)