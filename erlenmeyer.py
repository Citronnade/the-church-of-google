from flask import Flask, render_template, request
import webapp
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("home.html")

@app.route("/data/", methods=['POST'])
def data():
    form = request.form
    question = form['query']
    answer = webapp.main(question)
    return render_template("data.html", text=answer)
    
if __name__ == '__main__':
    app.debug = True
    app.run()
