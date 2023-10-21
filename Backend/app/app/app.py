from flask import Flask, request, jsonify
import os
import crypt_pdf
from werkzeug.utils import secure_filename
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in {'pdf', 'png', 'txt'}

# Establece la carpeta de carga
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ...

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # Determine the file type and route it to the appropriate handler
        file_extension = file.filename.rsplit('.', 1)[1]
        if file_extension == 'pdf':
            # Handle PDF file
            if file:
                filename = secure_filename(file.filename)
                uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(uploaded_file_path)
                crypt_pdf.encrypt_pdf_sha512(uploaded_file_path, 'output.pdf')
                os.remove(uploaded_file_path)
            return jsonify({'message': 'PDF file uploaded and processed'})
        elif file_extension == 'png':
            # Handle PNG file
            # Implementa la lógica de crypt_png.py aquí
            return jsonify({'message': 'PNG file uploaded and processed'})
        elif file_extension == 'txt':
            # Handle TXT file
            # Implementa la lógica de crypt_txt.py aquí
            return jsonify({'message': 'TXT file uploaded and processed'})
        else:
            return jsonify({'error': 'Unsupported file type'}), 400
    else:
        return jsonify({'error': 'Invalid file type'}), 400
if __name__ == '__main__':
    app.run(debug=True)
