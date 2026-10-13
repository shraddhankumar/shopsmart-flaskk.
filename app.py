from flask import flask
if(__name__) =="__main__":
app.run(debug=True)
@app.route('/')
def hello():
    return"Hello,World!"