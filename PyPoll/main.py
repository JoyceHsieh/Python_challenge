import os
import csv


voter_csv=os.path.join('election_data.csv')

vote_count = {}
vote_per = {}
vote_total = 0

with open(voter_csv, newline="") as csvfile:
    voterreader=csv.reader(csvfile, delimiter=",")

    next (voterreader) #skip the heading
    
    for row in voterreader:
        vote_total +=1
        
        if row[2] in vote_count:
            vote_count[row[2]] +=1  #plus value
        else:
            vote_count[row[2]] = 1  # add the new key, value start from 1

print(vote_count)
print(vote_total)

winner_count=0

for candidate in vote_count:
    vote_per[candidate]= (vote_count[candidate]/vote_total)*100   #key=value

    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner= candidate

print(vote_per)

#print result out
print(f'''Election Results
-------------------------
Total Votes: {vote_total}
-------------------------''')

for candidate, votes in vote_count.items():
    print(f'''{candidate}: {vote_per[candidate]:.3f}% ({votes})''')

print(f'''-------------------------
Winner: {winner}
-------------------------''')


# store the result in the txt.file
results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:
    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------\n''')
    
    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_per[candidate]:.3f}% ({votes})\n')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')