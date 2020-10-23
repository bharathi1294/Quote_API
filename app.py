from flask import Flask,request,render_template
from flask_cors import cross_origin
import requests

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	page=requests.get("https://api.quotable.io/random")
	js=page.json()
	content = js['content']
	author = js['author']
	tags = js['tags']
	return render_template("home.html",text=content,author_text=author,tag=",".join(tags))

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
