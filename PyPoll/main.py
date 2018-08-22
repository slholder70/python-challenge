import csv

#Assignment of variables for calculations        

vote_ct = 0             #The total number of votes cast
listofcand = []         #A complete list of candidates who received votes
vote_percentlist = []   #The list of percentage of votes each candidate won
votes_per_candlist = [] #The list of total number of votes each candidate won
election_winner = []    #The winner of the election based on popular vote.


# store file path associated with the file

file1 = 'raw_data/election_data_1.csv'

file2 = 'raw_data/election_data_2.csv'

# open the file in "read" mode ('r') and store contents in variables edata1,edata2

#with open(file1, 'r') as text:
#    print (text)
    
#    edata1 = text.read()  #stored file text as edata1
    
#    print(edata1)
    
#print(type(edata1))     #edata1 is a string and not a dataframe

#Method 2 for improved reading of CSV module

with open(file1, newline ='') as edata:
    
    #CSV reader with delimiter and varable holding contents
    
    edata1 = csv.reader(edata, delimiter = ',')
    next(edata1)    #skip header 
    for row in edata1:
        vote_ct += 1
        
        if row[2] not in listofcand:
            listofcand.append(row[2])   #adding new name to listofcand
            votes_per_candlist.append(1)  #adding one vote to the new name added to votes list
            
        else:
            #list_index =  #index to pair listofcand and votes_per_candlist
            #adding vote to candidate in list by indexing the lists
            votes_per_candlist[int(listofcand.index(row[2]))] = int(votes_per_candlist[int(listofcand.index(row[2]))]) + 1 
            
#Repeat steps for file2
            
            
with open(file2, newline ='') as edata:
    
    #CSV reader with delimiter and varable holding contents
    
    edata2 = csv.reader(edata, delimiter = ',')
    next(edata2)    #skip header 
    for row in edata2:
        vote_ct += 1
        
        if row[2] not in listofcand:
            listofcand.append(row[2])   #adding new name to listofcand
            votes_per_candlist.append(1)  #adding one vote to the new name added to votes list
            
        else:
            #list_index =  #index to pair listofcand and votes_per_candlist
            #adding vote to candidate in list by indexing the lists
            votes_per_candlist[int(listofcand.index(row[2]))] = int(votes_per_candlist[int(listofcand.index(row[2]))]) + 1
            

        
         
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

        
        
