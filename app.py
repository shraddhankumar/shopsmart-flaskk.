from flask import flask, render template 

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
    @app.route("/search")
    
if(__name__) =="__main__":
gitapp.run(debug=True)
