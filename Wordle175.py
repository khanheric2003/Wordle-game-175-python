from clean import open_file

#----------------------------------------------------
# Assignment 2: wordle 175
# 
# Author of code: Khanh Bui
# Collaboration: Discord
#----------------------------------------------------

# Task 2: This class used to open word5Dict.txt file and read it then insert the words into scrabble5.txt
# Input: words from word5Dict.txt file
# Ouput: word added to scrabble5.txt, bool of whether the word inside the word list or not, 
class ScrabbleDict:
    def __init__(self,size,file_name):
        self.size = size
        self.file_name = file_name
        open_file()
        self.word = open(self.file_name,"r")
        self.word_dictionary = {}
        
        for word in self.word:
            if len(word) != self.size:
                first_word = word[:5]
                value = word.removesuffix(first_word)
                self.word_dictionary[first_word] = value.strip()
            else:
                self.word_dictionary[word] = word
        
    '''
        This function will check whether the word is inside the dictionary or not 
        Inputs: input word and word list
        Returns: bool of whether the word inside the word list or not
    '''   
    def check(self,word): # worked
        self.word = word
        if self.word in self.word_dictionary.keys():   
            return True
        else: 
            return False
    '''
        This function will return the length of the word dictionary
        Inputs: self.word_dictionary
        Returns: length of the word inside the word dictionary 
    '''   
    def get_size(self): # worked
        return len(self.word_dictionary)
    '''
        This function will find the word that start with input letter,
        group the word into list based on their first letter and,then the list will be put in the dictionary
        the key will be the first letter and the value would be every word with that first letter
        Inputs: input letter, the word dictionary
        Returns: sorted list with the inputted first letter
    '''           
    def get_word(self,letter): # worked
        self.letter = letter
        sorted_list = []
        for key in self.word_dictionary:
            word_first_letter = key[0]
            if letter == word_first_letter:
                sorted_list.append(key)
        sorted_list.sort(key=lambda x:x[:-2])
        return sorted_list
    '''
        This function return the size of each word
        Inputs: self.size( the orriginal size of each word which is 5)
        Returns: self.size
    '''           

    def get_word_size(self):
        return self.size
    '''
        This function will find the possible word based from the template the user provided
        Inputs: template of the word, word list used to scan through 
        Returns: possible word list
    '''   
    # Task 4 part
    def getMaskedWords(self, template): # Worked
        # Decleare variable
        self.template = template.lower()
        self.template_list = []
        self.non_wild_card = []
        self.possible_list = []       
        self.possible_word_dict = {}        
        for letter in self.template:
            if letter != "*":
                self.non_wild_card.append(letter)
            self.template_list.append(letter)

        for word in self.word_dictionary:
            similarity_level = 0
            dictionary_word_list = []
            for letter in word:
                dictionary_word_list.append(letter)
            for index in range(len(dictionary_word_list)):
                if dictionary_word_list[index] == self.template_list[index]:
                    similarity_level = similarity_level +1
                    self.possible_word_dict[word] = similarity_level
        for key in self.possible_word_dict:
            if self.possible_word_dict[key] == len(self.non_wild_card):
                self.possible_list.append(key)

        return self.possible_list

    '''
        This function will find a new possible list of word base on the possible word list from the function above and additional input letter
        from the user 
        Inputs: possible_list, template, user's input
        Returns: a contrained word list
    '''   
    def getConstrainedWords(self, template,letters):
        self.template = template
        self.letters = letters
        constrained_words = []
        for word in self.possible_list:
            for letter in  word:
                if self.letters == letter:
                    constrained_words.append(word)
        return constrained_words        

    '''
        This function will be used to check whether the class ScrabbleDict's function work or not
        Inputs: ScrabbleDict class
        Returns: N/A
    '''   
def main():

    # Create ScrabbleDcit object
    game = ScrabbleDict(5,"scrabble5.txt") 

    # Test 1
    # Test whether word aahed is in the dictionary or not
    print(game.check("aahed")) # Return True since the wprd aahed is in the dictionary

    # Test 2
    # Test what is the total word insise the dictionary
    print(game.get_size()) # return the result as 8913 (the total number inside the dictionary)

    # Test 3
    # Test whether the sorted list function work or not 
    print(game.get_word("a")) # Return the the sorted list of all the word that have first letter "a"

    # Test 4
    # Test whether the function return the correct size 
    print(game.get_word_size())
    
    #Task 4: Test task4 template word tiger and add additional letter "i" with getMaskedWords and getConstrainedWords
    template = "T**ER"
    
    letters = "i"

    print(game.getMaskedWords(template)) 

    print(game.getConstrainedWords(template,letters))


if __name__ == "__main__":  
    main()



        



