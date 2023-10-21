import json
import subprocess

def upload(file_path):
    # Rclone command to upload a file to a remote
    rclone_command = f"rclone --config /home/csuarez/.config/rclone/rclone.conf copy {file_path} storj:crypt"

    # Cargar las claves desde el archivo JSON en el directorio padre
    with open('../keys.json') as f:
        keys = json.load(f)

    # Ejecutar el comando Rclone
    try:
        subprocess.run(
            rclone_command,
            shell=True,
            check=True,
            env={"STORJ_ACCESS_KEY": keys['access_key'], "STORJ_SECRET_KEY": keys['secret_key']}
        )
        print("Archivo subido exitosamente con Rclone")
    except subprocess.CalledProcessError as e:
        print("Error al subir el archivo con Rclone:", e)
