from flask import Flask, request, render_template, send_file
from rdkit.Chem import PandasTools
from werkzeug.utils import secure_filename
import os, shutil


app = Flask(__name__)

# App
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def abt():
    return render_template("about.html")

@app.route('/contact')
def com():
    return render_template("contact.html")

@app.route('/upload-file', methods=['POST','GET'])
def main():
    shutil.rmtree(os.path.join(app.instance_path, 'files/'), ignore_errors=True)
    def SDF2CSV():           
        if request.method == "POST":
            if request.files:

                #get sdf file
                sdf = request.files["sdffile"]
                os.makedirs(os.path.join(app.instance_path, 'files'), exist_ok=True)
                sdf.save(os.path.join(app.instance_path, 'files', secure_filename(sdf.filename)))

                #extract sdf data to csv
                filename = secure_filename(sdf.filename)
                infile = os.path.join(app.instance_path, 'files/'+filename)
                data = PandasTools.LoadSDF(infile,smilesName='SMILES',molColName='Structure', includeFingerprints=True)
                data = data.to_csv(os.path.join(app.instance_path, 'files/sdfextract.csv'))

    SDF2CSV()
    return render_template("download.html")

@app.route('/download')
def download_csv():
    outfile = os.path.join(app.instance_path, 'files/sdfextract.csv')
    return send_file(outfile, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)