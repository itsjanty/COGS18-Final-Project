#!/usr/bin/env python
# coding: utf-8

# # Project Description

# Write a brief description of your project here. 
# 
# For my project I will be creating a ChatBot based on a video game called Valorant. Valorant is a competitive 5v5 character-based tactical first-person shooter game created by video game developers at Riot Games. When playing the game each player is either put on an attacking or defending side. When attacking the goal is to plant a bomb called the Spike and when defending the goal is to make sure the enemy team is unable to plant and detonate the Spike.
# 
# Before the game begins every player needs to select a character called Agents. Each Agent is given a different set of abilities that they can use throughout the game. Every Agent is given a specific role which plays around the types of abilities they are given. The roles consists of Controllers; Agents who's abilities are able to slow down the enemy team, Duelists; Agents who's abilities are targeted towards self-sifficient fragging, Sentinels; Agents who's abilities are defensive based and Initiators; Agents who's abilities allow their team to contest enemies. The ChatBot I'll be creating allows users to know which role the Agent they input falls under as well as see a list of other Agents who fall under the same category.
# 
# Valorant has been out over a little over a year and has accumulated over 14 million players worldwide and within a span of every 3 months Valorant releases a new Agent for players to play. Valorant currently has 17 different Agents which can be a lot to remember, especially for new players. Thus, my ChatBot will help users identify what role a specific Agent falls under as well as see a list of other Agents that fall within the same role. 
# 
# 
# 
# 
# What type of Valorant Agent are you playing?
# 
# 17 Agents
# 
# 
# 
# 
# Note that projects should be self-sufficient, so make sure to provide enough information and context here for someone to understand what you are doing in your project, and why. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[ ]:


import string

#from my_module.functions import ...
#from my_module.classes import ...


# In[1]:


# Variable used to save Valorant Agent information

agents = {'Brimstone': 'Controller', 'Viper': 'Controller', 'Omen': 'Controller',
          'Astra': 'Controller', 'Phoenix': 'Duelist', 'Reyna': 'Duelist', 'Jett': 'Duelist',
          'Raze': 'Duelist', 'Yoru': 'Duelist', 'Sage': 'Sentinel', 'Cypher': 'Sentinel',
          'Killjoy': 'Sentinel', 'Chamber': 'Sentinel', 'Sova': 'Initiator', 'Breach': 'Initiator',
          'Skye': 'Initiator', 'KAY/O': 'Initiator'}

# From A3: Chatbot, Questions 11, 14 - 16
def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

def string_concatenator(string1, string2, separator):
    output = string1 + separator + string2
    return output

def list_to_string(input_list, separator):
    output = input_list[0]
    for variable in input_list[1]:
        string_concatenator = output + seperator + variable
        output = string_concatenator
    return output

def list_to_string(input_list, seperator):
    output = input_list[0]
    for x in input_list[1:]:
        output = string_concatenator(output, item, separator)
    return output

def end_chat(input_list):
    for x in input_list:
        if x.lower() == 'quit' or x.lower() == 'exit':
            return True
        else:
            return False

def is_in_list(list_one, list_two):
    for element in list_one:
        if element in list_two:
            return True
        return False

    
# Functions I created in order to create the Valorant ChatBot
def start_chat():
    print("Welcome to Valorant! Do you want to know about an Agent or a Role?")

# Reassign Agents Dictionary to 'dict_of_all_agents' that will be used for the Valorant ChatBot
def dict_of_agents():
    dict_of_agents_mass = {}
    dict_of_agents_mass = agents
    return dict_of_agents

# Checks to see if the user input an actual  Role
def check_Role(input_list):
    check_name = ''
    check_name = list_to_string(input_list, ' ')
    if check_name.lower() == 'role':
        return True
    return False

# Checks to see if the user input one of the Roles
def is_a_Role(input_list):
    role_list = {}
    role_list = type_of_roles()
    check_name = ''
    check_name = list_to_string(input_list, ' ')
    for x in role_list.keys():
        if x.lower() == check_name.lower():
            return True
        return False
      
# Checks to see if the user input an Agent
def is_a_Agent(input_list):
    check_name = ''
    check_name = list_to_string(input_list, ' ')
    if check_name.lower == 'agent':
        return True
    return False

# Creates a list of Agent Names
def key_of_agents():
    agent_names = []
    dict_list = dict_of_agents()
    for x in dict_list.keys():
        for y in dict_list[x]:
            agent_names.append(y)
        return agent_names
    
# Gets the Agents Role
def agents_Role(key):
    dict_list = dict_of_agents()
    agent_names = []
    
# Get the Role of the specific Agent
def specific_Agent_Role(role):
    agent_dict = {}
    agent_dict = agents()
    check = ''
    check= list_to_string(role, ' ')
    agents = ''
    for x in agent_dict:
        for y in agent_dict[x]:
            if agent_dict[y].get(x).lower() == check.lower():
                agents = agents + x  
    return agents


def Valorant_ChatBot():
    val_bot = []
    val_bot = key_of_agents()
    val_bot_to_string = list_to_string(val_bot, ' ')
    val_bot = prepare_text(val_bot_to_string)
    start_chat()
    
    # Components that'll be checked in order for the ChatBot to Run
    chat = True
    count = 0
    notice = 0
    feed = False
    agents2 = False
    roles2= False
    
    # Takes the input from the User
    while chat_msg:
        
        # Text to User
        user_input = input('')
        result_output = None
        user_input = prepare_text(user_input)
        
        # Checks to see if the user input a 'Role'
        role = is_a_Role(user_input)
        
        # Checks to see if the user input an 'Agent'
        agent = is_a_Agent(user_input)
        
        # Checks if the user input is one of the roles
        agent_role = specific_Agent_Role(user_input)

    if end_chat(user_input):
        result_output = 'Thank you for using our service!'


# In[11]:


# test it out

# Test the string_concatenator
def test_string_concatenator():
    assert callable(string_concatenator)
    assert isinstance(string_concatenator('hi', 'welcome', ' '), str)
    assert string_concatenator('hi', 'welcome', ' ') == 'hi welcome'

# Test the list_to_string
def test_list_to_string():
    assert callable(list_to_string)
    assert isinstance(list_to_string(['a', 'b'], '<'), str)
    assert list_to_string(['a', 'b'], '<') == 'a<b'

# Test the is_a_Agent Role
def is_a_Agent():
    assert is_a_Agent(['agent']) == True
    assert isinstance(is_a_Agent(['agent']),bool)
    assert callable(is_a_Agent)
    
# Test the agents_Role
def test_agents_Role():
    assert agents_Role(['Jett']) == 'Duelist' 
    assert isinstance(agents_Role(['Jett']),str)
    assert callable(agents_Role)
    
# Test the specific_Agent_Role    
def test_specific_Agent_Role():
    assert specific_Agent_Role(['Controller']) == 'Brimstone, Viper, Omen, Astra'
    assert isinstance(specific_Agent_Role(['Controller']), str)
    assert callable(test_specific_Agent_Role)


# #### Extra Credit (*optional*)
# I learned a little bit of basic Python in High School such as numbers, strings, and if/for statments but never really got a fully hands-on experience like this project. From high school until now I've slowly progressed in my Python skills but up until this day I find it really challenging for me to learn functions in Python. I'm not sure why but functions in tend to be the most difficult aspect for me. This project allowed me to challenged myself and get familiar with functions and how they work. I was able to create different functions and get a hands-on experience. I wasn't able to complete the final project exactly how I would've wanted to due to a family emergency but I feel like coming out of this project I've been able to get a better grasp on functions and how they work compared to just doing assignments.
