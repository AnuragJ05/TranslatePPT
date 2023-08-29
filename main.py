import os
from flask import Flask, send_file, request, render_template
from utils.translate_utils import taranslate_presentation_to_hindi
from config.config import output_ppt_file

app = Flask(__name__)
form_data = None

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = 'uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/translate_presentation',methods=['POST'])
def translate_presentation():
    '''
    translate_presentation translate the presentation from english to hindi
    '''
    taranslate_presentation_to_hindi(app.config['input_presentation_file'], output_ppt_file)

    return "presentation translated successfully"


@app.route('/translate',methods=['POST'])
def translate():
    '''
    translate will render the translate.html
    '''
    input_presentation_file = upload_file()
    app.config['input_presentation_file'] = input_presentation_file
    return render_template("translate.html")

@app.route('/redirect_download')
def redirect_download():
    '''
    redirect_download will redirect the page to download_file.html
    '''
    return render_template("download_file.html")

@app.route('/download_file')
def download_file():
    '''
    download_file will download the file
    '''
    return send_file(output_ppt_file, as_attachment=True)

@app.route('/', methods=["Post", "Get"])
def index():
    '''
    index will open the index page
    '''
    return render_template("index.html")

def upload_file():
    '''
    upload_file will upload the file
    '''
    uploaded_file = request.files['File']
    if uploaded_file:
        filename = uploaded_file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)
        return file_path
    else:
        raise "No file provided."

if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()



