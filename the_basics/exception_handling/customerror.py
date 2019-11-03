
class YourNameIsMikeError(Exception):
    def __init__(self, message):
        self.message = message

try:
    name = input('What is your name?')

    if (name != 'Mike'):
        raise YourNameIsMikeError(f'Your name is Mike and thats not what you typed in!!! Typed in: {name}')
except YourNameIsMikeError as err:
    print(f'An error occured {err}')
