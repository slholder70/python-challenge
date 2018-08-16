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

with open(file1, newline ='') as edata1:
    
    #CSV reader with delimiter and varable holding contents
    
    csvreader = csv.reader(edata1, delimiter = ',')
    print(csvreader)
    
    for row in csvreader:
        print(row)
        
         
print("Election Results")            
print("----------------------------")
print("Total Votes:")
print("Rogers:")
print("Gomez:")
print("Brentwood:")
print("Higgins:")
print("----------------------------")
print("Winner:")
print("----------------------------")

        
        
