
#First import some modules
import os
import csv

#Set some paths for the files to read in.... one relative and one fixed for testing in VSCode

#fixed path for testing

#csvpath = os.path.join(r"C:\Users\Drew\NUCHI201902DATA1\Homework\03-Python\Instructions\PyBank\Resources\budget_data.csv")

#relative path for release to github

csvpath = os.path.join("Resources","budget_data.csv")

#create a writable text file for results output
f= open("PyBank_results.txt","w+")

#declare/initialize some variables
row_count=0
total_profit = 0
change_list = []
csv_dictionary = {"month": [], "profit" : []}

#open the csv and read in the lines
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
 

    # Read each row of data after the header
    for row in csvreader:
            #print(row)
            row_count = row_count+1
            total_profit = total_profit + int(row[1])
            csv_dictionary["month"].append(row[0])
            csv_dictionary["profit"].append(row[1])

#convert the dictionary elements for profit into a list and grab the length
profit_list = csv_dictionary["profit"]
profit_list_length = len(profit_list)


#loooooooooooooooooooop doggggggggggg

for i in range(0,profit_list_length):
        #skip the first change calculation since theres no back data to use to determine the variance
        if i == 0:
            next
        #special case for the last month, so nothing goes out of range... the minus 1 is needed because the lists are slightly different sizes (by 1)
        elif i == profit_list_length-1:
            prev = profit_list[i-1]
            current = profit_list[i]
            nxt = 0
            change = int(current) - int(prev)
            change_list.append(int(change))
        #calculate the variances from month to month and append them into a list ---- this is where most of the work is being done
        else:
            prev = profit_list[i-1]
            current = profit_list[i]
            nxt = profit_list[i+1]
            change = int(current) - int(prev)
            change_list.append(int(change))

#do some math stuff
average_change = sum(change_list) / len(change_list)       
average_change = round(average_change,2)

#find the min and max values
max_profit = max(change_list)
min_profit = min(change_list)

#figure out which month the values occurred in.....again the +1 is necessary because the list sizes are 1 off
max_profit_index = change_list.index(max(change_list))+1
min_profit_index = change_list.index(min(change_list))+1
max_profit_month = csv_dictionary["month"][max_profit_index]
min_profit_month = csv_dictionary["month"][min_profit_index]

#print the results to the terminal
print("\n\nFinancial Analysis")
print("----------------------------\n")
print(f"Number of Months:  {row_count}")
print(f"Total Profit:  ${total_profit}")
print(f"Average Change:  ${average_change}")
print(f"Greatest Increase in Profits:  {max_profit_month} (${max_profit})")
print(f"Greatest Decrease in Profits:  {min_profit_month} (${min_profit})")

#write the results to the text file and close it
f.write("Financial Analysis \r\n\r\n")
f.write("----------------- \r\n\r\n")
string = "Number of Months:   " + str(row_count)
f.write(string+"\r\n")
string = "Total Profit:   " + str(total_profit)
f.write(string+"\r\n")
string = "Average Change:   " + str(average_change)
f.write(string+"\r\n")
string = "Greatest Increase in Profits:   " + str(max_profit_month) + "  ($"  + str(max_profit) +")"
f.write(string+"\r\n")
string = "Greatest Decrease in Profits:   " + str(min_profit_month) + "  ($"  + str(min_profit) +")"
f.write(string+"\r\n")    
f.write("----------------- \r\n \r\n")
f.close
