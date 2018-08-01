'''
@auhtor: navin106
compare variable
'''
VARA = 36
VARB = 20
if (type(VARA) or type(VARB)) == str:
    print('string involved')
elif int(VARA) > int(VARB):
    print('bigger')
elif int(VARA) == int(VARB):
    print('equal')
elif int(VARA) < int(VARB):
    print('lesser')
