from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Napier"

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
