'''
Enum - Suporte a enumerações
'''

# Exemplo de enum
#def move(direction):
    #if direction != 'right' and direction != 'left':
        #raise ValueError('cannot move in this direction')

    #return f'Moving {direction}'

#if __name__ == "__main__":
    #print(move('right'))
    #print(move('left'))
    #print(move('qualquer lugar'))

# para não precisar ta adicionando coisas no if sempre que aparecer uma nova direção
# utiliza-se o enum

from enum import Enum, auto

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()

def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('canoot move in this direction')

    return f'moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)