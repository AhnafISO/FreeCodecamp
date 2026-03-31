"""
RPG Character Creator

This project implements a simple character creation system for a role-playing game.
The function `create_character` validates user input and generates a formatted
character sheet based on the provided attributes.

Features:
- Validates the character name:
  • Must be a string
  • Cannot be empty
  • Cannot exceed 10 characters
  • Cannot contain spaces
- Validates character stats (strength, intelligence, charisma):
  • Must all be integers
  • Each stat must be between 1 and 4
  • The total of all stats must equal exactly 7

Output:
- Returns a formatted multi-line string representing the character:
  • First line: character name
  • Next lines: stats (STR, INT, CHA)
  • Each stat is visualized using:
        ● for filled points
        ○ for remaining points (up to 10 total)

Example:
    create_character('ren', 4, 2, 1)

    Output:
    ren
    STR ●●●●○○○○○○
    INT ●●○○○○○○○○
    CHA ●○○○○○○○○○

This project demonstrates input validation, conditional logic, and string
formatting in Python.


Built as part of FreeCodeCamp Python practice
"""



full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):

    if type(name) != str:
        return "The character name should be a string"
    if len(name) == 0:
        return "The character should have a name"
    
    if len(name) > 10:
        return "The character name is too long"
    
    if " " in name:
        return "The character name should not contain spaces"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    if strength < 1 or intelligence <1 or charisma < 1:
        return "All stats should be no less than 1"

    if strength > 4 or intelligence >4 or charisma >4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    lstr = (strength)*full_dot
    lint = (intelligence)*full_dot
    lchar = (charisma)*full_dot

    return f"{name}\nSTR {lstr.ljust(10,empty_dot)}\nINT {lint.ljust(10,empty_dot)}\nCHA {lchar.ljust(10,empty_dot)}" 

print(create_character('ren', 4, 2, 1))