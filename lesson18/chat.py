from functions import grade

fname = input('What is your first name?:')
lname = input('What is your last name?:')

print(f'Thank you, {fname} {lname}!')
course = input('What is the course you are enrolled in?:')
p = int(input('How many points did you get in this class?:'))
print(f'Your final grade for this class is a {str(grade(p))}.')

