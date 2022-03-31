from Wordle175 import ScrabbleDict
#----------------------------------------------------
# Assignment 2: wordle 175
# 
# Author of code: Khanh Bui
# Collaboration: Discord
#----------------------------------------------------

# Task 4,5: This task process getMaskedWords(self, template), getConstrainedWords(self, template,letters) and create statistic of the letter appearance 
# inside word list
# Input: ScrabbleDict from Wordle175
# Ouput: N/A 

'''
    This function will count the frequency the letter appear in the word list, calculate the percentage and calculate the star (represent for percentage)
    for each of the letter
    Inputs: ScrabbleDict from  Wordle175 py
    Returns: The percentage of each letter appear in word list, its frequency and its star
'''   
def stat():
    game = ScrabbleDict(5,"scrabble5.txt")
    repeated_letter_dict = {}
    repeated_letter_dict_percentage = {}
    star_dict = { }
    total_letter = game.get_word_size() * game.get_size()

    # Count word frequency inside dictionary
    for word in game.word_dictionary:
        for letter in word:
            if letter in repeated_letter_dict:
                repeated_letter_dict[letter] += 1
            else:
                repeated_letter_dict[letter] = 1
    for key in repeated_letter_dict:
        repeated_letter_dict_percentage[key] = round(((repeated_letter_dict[key] / total_letter) * 100),2) # go through
    for key in repeated_letter_dict_percentage:
        if round(repeated_letter_dict_percentage[key]) == 0:
            star_dict[key] = " "
        else:
            for value in range(round(repeated_letter_dict_percentage[key])): 
                star = round(value)  *  "*"
                star_dict[key] = star

    
    return repeated_letter_dict_percentage, star_dict, repeated_letter_dict

'''
    This function will ask the user for template input, ask for additional letter and display possible word, statistic of the letter (the
    percentage the letter would lilely appear from all of the word) 
    Inputs: template input, additional letter, ScrabbleDict
    Returns: N/A
'''   
def main(): 
    game = ScrabbleDict(5,"scrabble5.txt")
    template_player_input = input("Please enter the template of the word <ENTER>: ")
    template_player_input = template_player_input.lower()
    possible_list = game.getMaskedWords(template_player_input)
    while len(possible_list) == 0 or len(template_player_input) != 5:        
        print("*****Please enter a valid template******")
        player_input = input("Please enter the template of the word <ENTER>: ")
        possible_list = game.getMaskedWords(template_player_input)
    print("--For the next step, you can choose whether add additional letters or leave it blank for the previous possible word-- ")
    player_letters_input = input("Please enter additional letter <ENTER>: ")
    while player_letters_input.strip().isdigit() == True and player_letters_input < 5:
        print("*****Invalid additional letters - PLease type again*****")
        player_letters_input = input("Please enter additional letter <ENTER>: ")

    if player_letters_input == "":
        print("****The possible word according to your template****")
        for word in possible_list:
            print(word)
    else:
        contrained_list = game.getConstrainedWords(template_player_input,player_letters_input)
        print("****The possible word according to your template****")
        for word in contrained_list:
            print(word)


    # Displaying statistic of the game
    letter_percentage_dict, star_dict, repeated_letter_dict = stat()
    sorted_letter = sorted(letter_percentage_dict.keys(), key=lambda x:x.lower())
    print("****DISPLAYING STATISTIC OF EACH LETTER****")
    for key in sorted_letter:
        letter_percentage_dict[key] = round(letter_percentage_dict[key],2)
        print("%s: %6s %7s %-10s" % (key.upper(),repeated_letter_dict[key],str(letter_percentage_dict[key]) + "%",star_dict[key]))
if __name__ == "__main__":  
    main()