import os
import glob
from flask import Flask,render_template,request
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import pickle
import pandas as pd
kpp = Flask(__name__)

@kpp.route('/', methods=['GET'])
def hello_world():
	return render_template('index.html')

@kpp.route('/',methods=['GET', 'POST'])
def savefile():
    dfile=request.files["dfile"]
    filename = secure_filename(dfile.filename)
    UPLOAD_FOLDER = './dataset/'
    dfile.save(os.path.join(UPLOAD_FOLDER, filename)) 
    filename='testing.pkl'
    loaded_model=pickle.load(open(filename,'rb'))   
    tumors=pd.read_excel('D:/college/inal year/ml/lask application/dataset/test_set.xlsx')
    prediction=loaded_model.predict(tumors)
    
    return render_template('index.html',pre=prediction)
if __name__=='__main__':
    kpp.run(port=1200, debug=True)