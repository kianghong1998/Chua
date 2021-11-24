#Print all words in a dictionary file that has one word per line
#open file named "dictionary.txt" for reading ('r')
data_file = open ("dictionary.txt", 'r')

for line_str in data_file:
    print (line_str)