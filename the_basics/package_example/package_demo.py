from space.alien import Alien, greeting_from_aliens
from space.spaceship import craftSound
import space
greeting_from_aliens()
alien = Alien()

craftSound()

print(f'Names: { space.aliennames }')
print(f'Directory {dir(space)}')