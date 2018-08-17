import csv

# store file path associated with the file

file1 = 'raw_data/election_data_1.csv'

file2 = 'raw_data/election_data_2.csv'

# open the file in "read" mode ('r') and store contents in variables edata1, #  edata2

#with open(file1, 'r') as text:
#    print (text)
    
#    edata1 = text.read()  #stored file text as edata1
    
#    print(edata1)
    
#print(type(edata1))     #edata1 is a string and not a dataframe

#Method 2 for improved reading of CSV module

with open(file2, newline ='') as edata:
    
    #CSV reader with delimiter and varable holding contents
    
    edata1 = csv.reader(edata, delimiter = ',')
#   print(csvreader)
    
    for row in edata1:
        mylist1 = row[0]
        
print(mylist1)
#Assignment of variables for calculations        
#The total number of votes cast
vote_ct = 0
#A complete list of candidates who received votes
listofcand = []
#The list of percentage of votes each candidate won
vote_percentlist = []
#The list of total number of votes each candidate won
votes_per_candlist = []
#The winner of the election based on popular vote.
election_winner = []
        
         
print("Election Results")            
print("----------------------------")
print("Total Votes:")
print("----------------------------")
print("Rogers:")
print("Gomez:")
print("Brentwood:")
print("Higgins:")
print("----------------------------")
print("Winner:")
print("----------------------------")

        
        
