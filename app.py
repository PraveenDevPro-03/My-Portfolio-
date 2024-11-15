from flask import Flask,render_template
<<<<<<< HEAD
import os

=======
>>>>>>> 91bf385 (updating resume)
app=Flask(__name__)

@app.route('/')
def home():
    return  render_template('index.html')

if __name__=='__main__':
<<<<<<< HEAD
 app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
=======
    app.run(debug=True,port=5050)
>>>>>>> 91bf385 (updating resume)
