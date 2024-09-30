from flask import Flask, render_template, request, redirect, url_for
import os
import pickle
from model import generate_output

app = Flask(__name__)

# Configure the upload folder
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    # Save the uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Generate the result using the model
    result = generate_output(filepath)

    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
