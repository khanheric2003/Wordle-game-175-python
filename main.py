#----------------------------------------------------
# Assignment 2: wordle 175
# 
# Author of code: Khanh Bui
# Collaboration: Discord
#----------------------------------------------------
# Task 3: This function used to open word5Dict.txt file and read it then insert the words into scrabble5.txt

from Wordle175 import ScrabbleDict
from clean import open_file
import random
'''
    This function will represent for the whole game to play, it get random word from the list, take user's input, checking whether the word 
    correct or not, check for its duplicate and all display it in game function
    Inputs: word from word5Dict.txt, ScrabbleDict, open_file from clean and user's input
    Returns: chosen random word, boolean of self.game_continue, 
'''   
class Game:
    def __init__(self,size,file_name):
        self.size = size
        self.dictionary = ScrabbleDict(5, file_name)
        self.trials = 6
        self.word_list = []

        # chosen random word from dicionary create in Wordle175
        
        self.previous_accepted_word = []
        self.game_continue = True 
    '''
        This function will get random word from the word dictionary 
        Inputs: word from word_dictionary
        Returns: chosen random word
    '''   
    def get_random_word(self):
        self.random_num = random.randint(0,len(self.dictionary.word_dictionary)+ 1)
        for word in self.dictionary.word_dictionary:
            self.word_list.append(self.dictionary.word_dictionary[word])
        self.random_word = self.word_list[self.random_num]  
        return self.random_word      


    '''
        This function will represent for the whole game. It ask for input from player, checking condition and display
        Inputs: user's input, self.dictionary, check_word function
        Returns: bool whether game continue true or false
    '''   
    def game(self):
        # Ask the user for input while game continue == True
        while self.game_continue == True:  
            player_guess = input("Attempt %i: Please enter a 5 five-letter word: " % (self.trials))
            while len(player_guess) < 5: # Situation where the length of input shorter than 5
                print("%s is too short" % (player_guess.upper())) 
                player_guess = input("Attempt %i: Please enter a 5 five-letter word: " % (self.trials))
            while len(player_guess) > 5:  # Situation where the length of input longer than 5
                print("%s is too long" % (player_guess.upper()))
                player_guess = input("Attempt %i: Please enter a 5 five-letter word: " % (self.trials))
            player_guess = player_guess.lower()
            if self.dictionary.check(player_guess) != True: # not the word inside dictionary situation
                print("%s is not a recognized word" % (player_guess.upper()))
                player_guess = input("Attempt %i: Please enter a 5 five-letter word: " % (self.trials))
            elif player_guess in self.previous_accepted_word:  # re-enter the previous answer situation
                print("%s was already entered" % (player_guess.upper()))                
            else: 
                # Modifying the display for the game   
                self.check_word(player_guess,self.random_word) 
                if len(self.green) == 0:
                    self.green = " "       
                if len(self.yellow) == 0:
                    self.yellow = " "  
                if len(self.red) == 0:
                    self.red = " "  
                                      
                # Displaying for lose cases and win cases word input 
                if player_guess != self.random_word: # Word in list but not correct one
                    self.trials = self.trials - 1                                                        
                    print("%s - Green = {%s} - Yellow = {%s} - Red = {%s} " %(player_guess.upper(),', '.join(str(x) for x in sorted(self.green)),
                                                                                            ', '.join(str(x) for x in sorted(self.yellow)),
                                                                                            ', '.join(str(x) for x in sorted(self.red))))
                    self.previous_accepted_word.append(player_guess)

                    if self.trials == 0:
                        print("Sorry you lose. The Word is %s" % (self.random_word))
                        return self.game_continue == False
                else: # guessed the word situation
                    self.previous_accepted_word.append(player_guess)
                                             
                    print("%s - Green = {%s} - Yellow = {%s} - Red = {%s} " %(player_guess.upper(),', '.join(str(x) for x in sorted(self.green)),
                                                                                            ', '.join(str(x) for x in sorted(self.yellow)),
                                                                                            ', '.join(str(x) for x in sorted(self.red))))                      
                    print("Found in %i attempts. Well done. The Word is %s" % (self.trials,player_guess))
                    return self.game_continue == False
    '''
        This function will check the the similarity level and put them into 3 seperate set, green case is occured when correct letter and correct order,
        yellow case is occured when correct letter but wrong order, red cases means wrong word and also wrong order
        Inputs: user's input and chosen random word
        Returns: green case set, yellow case set, red case set
    '''                        
    def check_word(self,user_answer, random_word):
        self.user_answer = user_answer
        self.random_word = random_word
        
        self.green = set()
        self.red = set()
        self.yellow = set()
        user_word_letter_list = []
        
        random_word_letter_list = []
        duplicates = {}
        duplicate_count = 1
        # put each letter of the two input into list                
        for letter in self.user_answer:
            user_word_letter_list.append(letter)
        for letter in self.random_word:
            random_word_letter_list.append(letter)
            

        # duplicate
        # for value in duplicates.values():
        for letter in self.user_answer: # Find the dupplicate and put into dictionary
            if letter in duplicates:
                duplicates[letter] += 1
            else:
                duplicates[letter] = 1
        for key, value in duplicates.items():
            if value > 1: # Checking whether the input contain duplicate word or not
                for duplicate in range(duplicates[key]): 
                    for index in range(len(user_word_letter_list)): 
                        if key == user_word_letter_list[index]:
                            user_word_letter_list[index] = key + str(duplicate_count)
                            duplicate_count += 1

         # Green case
        for letter in user_word_letter_list:
            user_letter_index = user_word_letter_list.index(letter)
            for index in range(5): # Remove the number behind the letter
                letter = letter.removesuffix(str(index))

            if letter == random_word_letter_list[user_letter_index]:
                match_letter =  user_word_letter_list.pop(user_letter_index)
                user_word_letter_list.insert(user_letter_index,"*") # Replace the pop word with "*"
                self.green.add(match_letter.upper())      

        # Yellow case 
        for letter in user_word_letter_list:   
            if letter == "*":
                user_word_letter_list.remove("*") # Remove the "*"            
            elif letter in random_word_letter_list:
                letter_index = user_word_letter_list.index(letter)
                for index in range(5):
                    letter = letter.removesuffix(str(index))       
                exist_letter = user_word_letter_list.pop(letter_index)
                self.yellow.add(exist_letter.upper())          
        # Red case - Append the rest of the word
        for letter in user_word_letter_list:
            if letter == "*":
                user_word_letter_list.remove("*") 
            else:
                self.red.add(letter.upper())
         

        return self.green,self.red,self.yellow
                
    '''
        This function will run the whole game on main.py 
        Inputs: Game class above
        Returns: N/A
    '''       
def main():
    open_file()
    game = Game(5,"scrabble5.txt")
    random_word = game.get_random_word()
    while game.game() == True:
        game.game()   

if __name__ == "__main__":  
    main()