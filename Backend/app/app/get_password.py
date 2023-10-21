import json

def get_password():
    # Abre el archivo key.json
    with open('../key.json', 'r') as file:
        data = json.load(file)

    # Obtiene la contraseña del archivo key.json
    password = data['password']

    return password

# Obtiene la contraseña
password = get_password()
