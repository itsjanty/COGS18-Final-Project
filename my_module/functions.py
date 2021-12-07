"""A collection of function for doing my project."""

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
