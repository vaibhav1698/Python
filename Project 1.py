#!/usr/bin/env python
# coding: utf-8

# In[25]:


'''
This is a simple game where an initial list is displayed.

The user who is playing this can then input the position they want to add
their own value followed by the value

'''

game_list = [0, 1, 2, 3, 4, 5]


# In[26]:


'''
This function is used to display the current game list
'''

def display_game(game_list):
    
    print("Here is the current list: ")
    
    print(game_list)


# In[27]:


'''

This function asks the user to enter their desired position where 
they want to make changes in the game list

'''


def position_choice():
    
    choice = 'Wrong'
    
    while choice not in ['0', '1', '2', '3', '4', '5']:
        
        choice = input("Select a position (0-6): ")
        
        if choice not in ['0', '1', '2', '3', '4', '5']:
            print("Sorry, invalid position choice")
            
    return int(choice)


# In[28]:


'''

This function asks the user the value which they want to send in the game list

'''
def replacement_choice(game_list,position):
    
    user_value = input("Enter the desired value you want to enter in the game list")
    
    game_list[position] = user_value
    
    return game_list


# In[29]:


'''
This function asks the user if they want to continue the game or not

'''
def game_on_or_off():
    
    choice = 'Wrong'
    
    while choice not in ['Y', 'N', 'y', 'n']:
        
        choice = input("Do you want to keep playing? (Y or N): ")
        
        if choice not in ['Y', 'N', 'y', 'n']:
            
            print("Sorry, invalid choice, please choose Y or N")
            
            
    if choice == "Y" or choice == "y":
        
        return True
    
    else:
        
        return False


# In[30]:


'''
This is the main game code where all the above functions come together

'''

game_play = True

game_list = [0, 1, 2, 3, 4, 5]


while game_play:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_play = game_on_or_off()


# In[ ]:




