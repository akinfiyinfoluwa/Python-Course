contacts = {
    'number': 4,
    'students': [
          {'name':'Sarah Doofan', 'email':'sarah@gmail.com'},
          {'name':'John Doe', 'email':'john@gmail.com'},
          {'name':'Jane Doe', 'email':'jane@gmail.com'},
          {'name':'Bob Smith', 'email':'bob@gmail.com'},
    ]
}

print('Students Emails:')

for student in contacts['students']:
    print(student['email'])