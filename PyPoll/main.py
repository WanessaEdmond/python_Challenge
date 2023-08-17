import csv
#Import file 
with open('/Users/wedmo/OneDrive/Documents/Class/python_Challenge/PyPoll/Resources/election_data.csv') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')

    # skip header line
    headers = next(csv_read)

    #find total row count 
    #row_count = sum(1 for row in csv_read)
    #print(f'The total number of votes cast is {row_count}.')

    # Calculating complete list of candidates who received votes
    row_count =0
    Winner=0
    winning_candidate = '' 
    candidate = []
    candidate_vote = {}
    for row in csv_read:
        row_count +=1
        #print(row[2])

        if row[2] not in candidate:
            candidate.append(row[2])  
            candidate_vote[row[2]]=0
        #adding vote for each candidate 
        candidate_vote[row[2]]=candidate_vote[row[2]]+1

    print(f'The total number of votes is {row_count}.')
    
    # The percentage of votes each candidate won
    for candidate in candidate_vote:
        vote_per_candidate = candidate_vote.get(candidate)
        vote_percentage = float (vote_per_candidate/row_count * 100)
        print(f'{candidate}:{vote_percentage:.3f}% ({vote_per_candidate})')

    # The total number of votes each candidate won

        if vote_per_candidate > Winner:
           Winner=vote_per_candidate
           winning_candidate = candidate
    print (f'The winner is {winning_candidate} with {Winner}')

with open('analysis.txt', 'w') as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('----------------------------\n')
    txt_file.write(f'Total Number of Votes: {row_count}\n')

    txt_file.write(f'{candidate}:{vote_percentage:.3f}% ({vote_per_candidate}\n')


    txt_file.write(f'The winner is {winning_candidate} with {Winner}\n')
    

print('The analysis has been exported to analysis.txt.')