def find_acronym():
    look_up = input('What Software Acronym would you like to look up?')

    found = False
    with open('software_acronyms.txt') as file:
        for line in file:
            if look_up in line:
                print(line)
                found = True
                break
    if not found:
        print('The acronym does not exist')
def add_acronym():
    acronym = input('What Software Acronym would you like to add?')
    definition = input('What is the definition of the acronym?')
    with open('software_acronyms.txt', 'a') as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    choice = input('Do you want to find(F) or add(A) an acronym?')
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()
        print('Acronym Added')

main()
