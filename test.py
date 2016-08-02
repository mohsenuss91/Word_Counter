from flask import Flask, request, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return render_template('index.html')
 
@app.route("/index", methods=['POST'])
def index(): 
    return render_template('index.html', text=request.form['text'])
 
 
if __name__ == "__main__":
    app.run(debug=True)