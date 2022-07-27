from flask import Flask,send_file
import os
import urllib.request
from PIL import Image,ImageOps
import io
import base64
import json
import requests
import model
import sys

from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from model.rotatel import RotateLeft
from model.imagetransformationfactory import ImageTransformationFactoryDecider


UPLOAD_FOLDER = '/Users/sahanabarki/Documents/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 3000 * 3000


ALLOWED_EXTENSIONS = set(['png', 'jpeg','tiff', 'bmp','gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def rotateRight(image):
    degree_flippedImage = image.transpose(Image.ROTATE_90)
    return degree_flippedImage


@app.route('/transformations',methods=['GET'])
def getTransformations():
	resp = jsonify({'message' : 'success','code':200,"transformations": ['rotateLeft','rotateRight','flipHorizontal','flipVertical','grayScale','thumbNail','resizeWidthHeight','rotateDegrees']})
	return resp



@app.route('/transformations', methods=['POST'])
def upload_file():
	#check if the file is present in the request
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp

	#fetching the file	
	file = request.files['file']
	
	
	#check if the file selected for uploading
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp

	#check if the file name is present in the given format
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)

		fileExtension = filename.split(".")[-1]
	

		#fetch the image
		img = Image.open(file.stream)

		#fetch the transformations
		for key in request.form:

			# print(key,request.form[key])

			if key=='transformations': 
				transformationsValue = request.form[key]

		transformationsValueArray = transformationsValue.split(',')
		try:
			for i in transformationsValueArray:
				temp1 = ImageTransformationFactoryDecider(img, i)
				img = temp1.applyTransformation(img, i)
		except ValueError as err:
			resp = jsonify({'message' : err.args[0]})
			resp.status_code = 400
			return resp

		rawBytes = io.BytesIO()
		img.save(rawBytes, fileExtension)
		rawBytes.seek(0)
		
		return send_file(rawBytes, mimetype='image/'+fileExtension)
	else:
		resp = jsonify({'message' : 'Allowed file types are  pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp


if __name__ == "__main__":
    app.debug = True
    app.run()