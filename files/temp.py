
acronym = input('What acronym do you want to add?')

definition = input('What is the definition')


with open('software_acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')
#write the new acronym ad definition to the file
