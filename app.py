from flask import Flask, request, render_template
from mains_marks import give_marks  # Import the function from your script
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/tmp'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'html' not in request.files:
        return 'No file part'
    file = request.files['html']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        directory = os.path.join(app.config['UPLOAD_FOLDER'], "Test.html")
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)
        file.save(file_path)
        
        output = give_marks(file_path)
        
        return render_template('result.html', output=output)

@app.route('/upload_url', methods=['POST'])
def upload_url():
    url = request.form.get('url')
    if not url:
        return 'No URL provided'
    
    output = give_marks(url)
    
    return render_template('result.html', output=output)