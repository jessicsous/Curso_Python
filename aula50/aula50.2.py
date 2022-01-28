import json

d1 = {
    'pessoa 1' : {
        'nome' : 'Luiz',
        'idade' : '25',
    },
    'pessoa 2' : {
        'nome' : 'rose',
        'idade' : '30',
    },
}

d1_json = json.dumbs(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.with(d1_jason)
