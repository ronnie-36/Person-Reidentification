from flask import Flask, jsonify, request, render_template,redirect, url_for
import os
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import reid_2vid
import reid_vidimg
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/reid1/', methods = ['GET', 'POST']) 
@cross_origin()
def reid1(): 
    if(request.method == 'GET'): 
        videopath1 = request.args.get('file1')
        imagepath1 = request.args.get('file2')
        print('started')
        object=reid_vidimg.Videoreid()
        out=object.video_reid(videopath1,imagepath1) 
        if(out[1]==True):
            return render_template('result.html',res='{}'.format(out[0]))
        else:
            return render_template('result0.html',res='{}'.format(out[0]))       
@app.route('/reid2/', methods = ['GET', 'POST']) 
@cross_origin()
def reid2(): 
    if(request.method == 'GET'): 
      videopath1 = request.args.get('file1')
      videopath2 = request.args.get('file2')
      print('started')
      object=reid_2vid.Videoreid()
      out=object.video_reid(videopath1,videopath2) 
      if(len(out[1])==0):
            return render_template('result0.html',res='{}'.format(out[0]))
      else:
            return render_template('result.html',res='{}'.format(out[0]))

if __name__ == '__main__': 
  
    app.run(debug = True) 