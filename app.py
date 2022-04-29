import sys, os
import subprocess
from flask import Flask, flash, request, redirect, render_template, send_file, url_for, send_from_directory
from werkzeug.utils import secure_filename

import uuid

app=Flask(__name__)

app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, 'uploads')
app.config["UPLOAD_FILENAME"] = 'video.mp4'
app.config["DOWNLOAD_FILENAME"] = 'test.txt'
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            file_id = str(uuid.uuid4().hex)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file_id)
            os.makedirs(path)
            file.save(os.path.join(path, app.config["UPLOAD_FILENAME"]))

            subprocess.Popen(['python', 'track.py', '--uuid', file_id]).wait()

            return file_id

    return render_template("index.html")


@app.route('/uploads/<name>')
def download_file(name):
    folder = os.path.join(app.config["UPLOAD_FOLDER"], name)
    return send_from_directory(folder, app.config['DOWNLOAD_FILENAME'])


@app.route('/download', methods=['GET'])
def return_file():
    obj = request.args.get('obj')
    loc = os.path.join("static", obj)
    print(loc)
    try:
        return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    print('to upload files navigate to http://127.0.0.1:5000/')
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
