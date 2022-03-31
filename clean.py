#----------------------------------------------------
# Assignment 2: wordle 175
# 
# Author of code: Khanh Bui
# Collaboration: 
#----------------------------------------------------
# Task 1: This function used to open word5Dict.txt file and read it then insert the words into scrabble5.txt

'''
    This function will open the word5Dict.txt file, fixed it so it have word for each line and write it on scrabble5.txt
    Inputs: word from word5Dict.txt
    Returns: word written on scrabble5.txt
'''   
def open_file(): 
    words = []
    with open('word5Dict.txt','r') as f:
        for line in f:
            for word in line.split("#"):
                if(word!='\n'):
                    words.append(word.strip())
    file = open('scrabble5.txt','w')
    for word in words:
        file.write(word+'\n')
    f.close()
    file.close()