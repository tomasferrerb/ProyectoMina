import os, time, sys


from flask import Flask
from flask import request
from flask import render_template
#import stringComparisonfrom flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    os.system('vcgencmd display_power 0') #Turn off HDMI signal
    return render_template('index.html')    
#return 'Hello world'
@app.route('/', methods=['POST'])
def index_post():
    text1 = request.form['txtmensaje']
    clr = request.form['color']
    command='./../monitor.py --message \''+text1+'\' --color '+clr+' --time 7 &'
    os.system(command)
    os.system('vcgencmd display_power 1') # Turn ON HDMI signal
    out= 'Tu mensaje: \" <strong>'+text1+'</strong> \" Ha sido desplegado'
    time.sleep(5)
    os.system('vcgencmd display_power 0')
    return out

#text2 = request.form['text2']
#    plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
#    if plagiarismPercent > 50 :
 #       return "<h1>Plagiarism Detected !</h1>"
  #  else :
   #     return "<h1>No Plagiarism Detected !</h1>"

if __name__ == '__main__':
	
    app.run(debug=True, host='10.42.92.197')

