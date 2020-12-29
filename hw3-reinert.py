#Author: Jeremy Reinert
#Date: 2/4/2020
#Version: 1.0

#hw3-reinert.py
"""Deals 5 card poker hand from deck of 52 cards a user designated times and then computes, outputs, and graphs the frequency and probability of each poker hand type"""

#Import Modules
import matplotlib.pyplot as plt   # 2D library
import numpy as np
import random 
import seaborn as sns



#Functions
#Init, deal, and print functions
def initialize_deck(suit, face, deck):
    """Initializes card deck from suit and face lists passed as parameters"""
    for f in face:
        for s in suit:
            deck += (f, s),

def print_deck(deck):
    """Prints cards from card deck"""
    number_columns = 4
    count = 0
    
    for face, suit in deck:
        print(f'{face} of {suit}', end=' ')
        count += 1
        
        if count == number_columns:
            print()
            count = 0

def print_hand(hand):
    """Prints formatted hand to console"""
    print('[', end = '')
    for i in hand:
        if hand.index(i) < len(hand) - 1:
            print(f'{i[0]} of {i[1]}, ', end = '')
        else:
            print(f'{i[0]} of {i[1]}', end = '')
    print(']')
    print(' ')    
    
def deal_cards(deck, hand_one):
    """Uses random module shuffle function to shuffle cards and deals 1 hand"""   
    random.shuffle(deck)
    hand_one += deck[0:5]
    
#Hand evaluation functions
def one_pair(hand, face):
    """Searches for a pair in hand passed and returns True if one is found"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 2:
            return True
        
    return False        
    
def two_pairs(hand, face):
    """Counts and returns True if two pairs are found in the hand passed"""
    face_values_in_hand = []
    two_pair = 0
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 2:
            two_pair += 1
    
    if two_pair > 1:
        return True
    
    return False

def three_of_a_kind(hand, face):
    """Counts and returns True if there is a three of a kind in the hand"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 3:
            return True
    
    return False

def four_of_a_kind(hand, face):
    """Counts and returns True if there is a four of a kind in the hand"""
    face_values_in_hand = []
    for i in hand:
        face_values_in_hand.append(i[0])
        
    for value in face:
        if face_values_in_hand.count(value) == 4:
            return True
    
    return False
 
def flush(hand, suit):
    """Counts cards suits and returns True if there are five of a kind in the hand"""
    suits_in_hand = []
    for i in hand:
        suits_in_hand.append(i[1])
        
    for s in suit:
        if suits_in_hand.count(s) == 5:
            return True    
    
    return False

def full_house(hand, face):
    """Calls one_pair and three_of_a_kind functions and returns True if both return True"""
    if one_pair(hand, face) == True and three_of_a_kind(hand, face) == True:
        return True
    
    return False

def straight(hand, face):
    """Evaluates hand for 5 sequential face values and returns True if found"""
    #Init empty lists for function use
    face_values_in_hand = []
    sequences = []
    
    #Append face values to sequences list
    for i in face:
        sequences.append(i)
    sequences.append('Ace')
    
    #Append vace values in hand to face_values_in_hand list
    for i in hand:
        face_values_in_hand.append(i[0])
 
    #Sort face_values_in_hand, init empty hand_face string var, and add element in face_values_in_hand list to hand_face string
    face_values_in_hand = sorted(face_values_in_hand)
    hand_face = ''
    for i in face_values_in_hand:
        hand_face += i    
    
    while len(sequences) > 4:
        #Sort sequences, init empty seq_face string var, set seq_split equal to elements sequence[0:5], and add elements in seq_split to seq_face string
        seq_face = ''
        seq_split = sequences[0:5]
        seq_split = sorted(seq_split)
        for i in seq_split:
            seq_face += i
        
        #Compare seq_face with hand_face and return True if equal -- else, delete element at sequences[0] and loop again
        if seq_face == hand_face:
            return True
        else:
            del sequences[0]
        
    return False

def straight_flush(hand, face, suit):
    """Calls straight and flush functions and returns True if both return True"""
    if straight(hand, face) == True and flush(hand, suit) == True:
        return True
    
    return False

def high_card(hand):
    """Evaluates hand for its highest card and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    high_card = ''
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
                high_card = f'{i[0]} of {i[1]}'
    
    return high_card

def high_card_2(hand):
    """Evaluates hand for its highest card and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    high_card = ''
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
                high_card = i[0]
    
    return high_card

def high_card_val(hand):
    """Evaluates hand for its highest card and returns its value to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    
    return high_card_val

def high_card_val_2(hand):
    """Evaluates hand for its highest card and returns its value to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    
    for i in hand:
        for j in face:
            if i == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    
    return high_card_val

def high_card_straight(hand):
    """Evaluates hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
        
    if 'Ace' in face_values_in_hand and 'Four' in face_values_in_hand:
        high_card_val = 4
        return high_card_val
    
    for i in hand:
        for j in face:
            if i[0] == j[0] and high_card_val < j[1]:
                high_card_val = j[1]
    return high_card_val

def high_card_full_house(hand):
    """Evalutes hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    high_card_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
    
    for i in face_values_in_hand:
        if face_values_in_hand.count(i) == 3:
            for j in face:
                if i == j[0] and high_card_val < j[1]:
                    high_card_val = j[1]
    
    return high_card_val

def high_card_pairs(hand):
    """Evaluates hand for its highest card value and returns it to calling function"""
    face = [('Deuce', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 11), ('Queen', 12), ('King', 13), ('Ace', 14)]
    hand_val = 0
    face_values_in_hand = []
    
    for i in hand:
        face_values_in_hand.append(i[0])
    
    for i in face_values_in_hand:
        for j in face:
            if i == j[0]:
                hand_val += j[1]
    
    return hand_val

def evaluate_hand(hand, face, suit, hand_frequency):
    
    #Init hand_rank var and set to empty string
    hand_rank = ' '
      
    #Evaluate hand for hand value and set hand_rank to value if True returned
    if high_card(hand) != '':
        hand_rank = 'High Card'
    
    if one_pair(hand, face) == True:
        hand_rank = 'One Pair'
    
    if two_pairs(hand, face) == True:
        hand_rank = 'Two Pairs'
    
    if three_of_a_kind(hand, face) == True:
        hand_rank = 'Three of a Kind'
        
    if straight(hand, face) == True:
        hand_rank = 'Straight'
        
    if flush(hand, suit) == True:
        hand_rank = 'Flush'
        
    if full_house(hand, face) == True:
        hand_rank = 'Full House'
        
    if four_of_a_kind(hand, face) == True:
        hand_rank = 'Four of a Kind'
        
    if straight_flush(hand, face, suit) == True:
        hand_rank = 'Straight Flush'
    
    #Append hand rank to list passed as hand_frequency
    hand_frequency.append(hand_rank)               
        
#Init lists containing suits and card faces
suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
face = ['Ace', 'Deuce', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
hand_freq = []

#Req user input for number of times to run simulation and check to ensure that input is an int
number_of_plays = input('How poker hands do you want to deal?')
is_num = False

while is_num == False:
    if number_of_plays.isdigit():
        number_of_plays = int(number_of_plays)
        is_num = True
    else:
        number_of_plays = input('You did not enter a valid number. Please enter the number of times you want to play.')

#Loop through inputted number of times
num_played = 1
while num_played <= number_of_plays:
    #Init empty deck and hand lists
    deck = []
    hand_one = []
    
    #Call initialize_deck function to create deck of cards
    initialize_deck(suit, face, deck)
    
    #Call deal_cards function to deal shuffle deck and two hands of 5 cards
    deal_cards(deck, hand_one)
    
    #Call evaluate hand to determine hand rank and add hand to hand_freq list
    evaluate_hand(hand_one, face, suit, hand_freq)
    
    num_played += 1
        
#Print bar chart of data
hands, frequencies = np.unique(hand_freq, return_counts = True)

print(f'Number of poker hands dealt: {number_of_plays}')
print(f'{"Hand":^15} | {"Frequency":^10} | {"Probability":^12}')
index = 0

while index < len(hands):
    print(f'{hands[index]:<15} | {frequencies[index]:^10,} | {frequencies[index]/len(hand_freq):^12.3%}')
    index += 1

#Remove High Card and Straight Flush from np arrays before printing bar chart

if 'High Card' in hands.tolist():
    hc_i = hands.tolist().index('High Card')
    
    hands = np.delete(hands, hc_i)
    frequencies = np.delete(frequencies, hc_i)

if 'Straight Flush' in hands.tolist():
    sf_i = hands.tolist().index('Straight Flush')
    hands = np.delete(hands, sf_i)
    frequencies = np.delete(frequencies, sf_i)

title = f'Poker Hand Frequency in {len(hand_freq):,} Hands Dealt'
sns.set_style('whitegrid')
axes = sns.barplot(hands, frequencies, palette='bright')
axes.set_title(title)  # set graph title
axes.set(xlabel='Poker Hands', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.20)

for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0  
    text_y = bar.get_height() 
    text = f'{frequency:,}\n{frequency / len(hand_freq):.3%}'
    axes.text(text_x, text_y, text, 
              fontsize=11, ha='center', va='bottom')

plt.show()





