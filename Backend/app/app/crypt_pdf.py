from PyPDF2 import PdfReader, PdfWriter
import get_password
import upload
def encrypt_pdf_sha512(input_file, output_file):
    """Encripta un archivo PDF con un algoritmo SHA512.

    Args:
        input_file (str): La ruta al archivo PDF de entrada.
        output_file (str): La ruta al archivo PDF de salida.
    """

    # Obtiene la contraseña
    password = get_password.get_password()

    # Imprime la contraseña
    print(password)

    # Abre el archivo PDF de entrada y crea un archivo de salida encriptado
    reader = PdfReader(input_file)
    writer = PdfWriter()

    # Agrega cada página del PDF a la instancia PdfWriter
    for page in reader.pages:
        writer.add_page(page)

    # Encripta el archivo PDF con la contraseña
    writer.encrypt(password)

    # Guarda el archivo encriptado con el nombre de archivo proporcionado
    with open(output_file, "wb") as f:
        writer.write(f)
    upload.upload(output_file)
