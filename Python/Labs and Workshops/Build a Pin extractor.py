'''
Project: PIN Extractor from Poems

In this project, I created a program that reads short poems and turns them into secret number codes.

The idea is simple: each line of a poem gives one number. To get that number, the program looks at a specific word in the line and counts how many letters it has. For example, in the first line it looks at the first word, in the second line it looks at the second word, and so on.

If a line is too short and doesn’t have the required word, the program adds a 0 instead. This way, every line always contributes a number.

The program repeats this process for multiple poems and returns a list of codes — one code for each poem.

This project helped me practice breaking text into smaller parts and building results step by step using Python.

#FREECODECAMP WORKSHOP
'''


def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return(secret_codes)
        

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))
