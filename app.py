from flask import Flask,request,render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
	page=requests.get("https://api.quotable.io/random")
	js=page.json()
	content = js['content']
	author = js['author']
	tags = js['tags']
	return render_template("home.html",text=content,author_text=author,tag=",".join(tags))

if __name__ == "__main__":
	app.run(debug=True)