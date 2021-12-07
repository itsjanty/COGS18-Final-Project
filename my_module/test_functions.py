"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module import*
##
##

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



                 
    
