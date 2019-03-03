
#First import some modules
import os
import csv

#Set some paths for the files to read in.... one relative and one fixed for testing in VSCode

#fixed path for testing


#csvpath = os.path.join(r"C:\Users\Drew\NUCHI201902DATA1\Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv")

#relative path for release to github
csvpath = os.path.join("Resources","election_data.csv")

#initialize some variables
row_count=0
winning_number_of_votes = 0
voter_id = []
county = []
candidate = []
unique_candidates = []

#create a writable text file for the output results
f= open("PyPoll_results.txt","w+")

#open the csv and read it in
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
            #print(row)
            #count the number of total rows
            row_count = row_count+1
            #get the data appended into lists
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
            current_candidate = row[2]
            #gather the list of unique candidates
            if unique_candidates.count(current_candidate) == 0:
                unique_candidates.append(current_candidate)

    #Print some stuff to the terminal as well as the text file
    print("\nElection Results\n\n")
    print("-------------------\n\n")
    print(f"Total Votes : {row_count}")
    string = "Total Votes : "+ str(row_count)
    print("-------------------")
    f.write("Election Results \r\n\r\n")
    f.write("----------------- \r\n\r\n")
    f.write(string+"\r\n")
    f.write("----------------- \r\n \r\n")

    #use the list of unique candidates to figure out who won
    for person in unique_candidates:
        
        #count the votes
        number_of_votes = candidate.count(person)
        
        #figure out if this person is the winner
        if number_of_votes > winning_number_of_votes:
                winner = person
                winning_number_of_votes = number_of_votes
        
        #who doesn't love a little simple math?
        percent_of_votes = number_of_votes / row_count *100
        percent_of_votes = round(percent_of_votes,5)

        #should probably print the results somewhere - gonna do that now a couple places
        print(f"{person} :  {number_of_votes}  ({percent_of_votes}%)")
        string = str(person) + " :   " + str(number_of_votes) + "   (" + str(percent_of_votes) + "%)"
        f.write(string+"\r\n")

#Ever sleep in at a hotel and then you get woken up by some HOUSEKEEPING?
#Do some housekeeping and print the winner to the terminal and the text file and then close it
print("-------------------\n")
f.write("----------------- \r\n \r\n")
print(f"Winner : {winner}")
string = "Winner  :  " +str(winner)
f.write(string+"\r\n")
f.close