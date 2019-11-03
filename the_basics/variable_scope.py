from math import pi

alien='Hariry alien'

def saywelcome():
    # global alien
    alien='Rocklike alien'
    def goodbye():
        print(f'Goodbye my friend {alien}')

    print(f'Hello my friend {alien}')
    goodbye()

saywelcome()
print(f'From global scope {alien} pi value { pi }')
