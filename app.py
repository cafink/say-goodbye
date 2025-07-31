from flask import Flask, render_template
from classes.save import Save

save = Save("saves/0.celeste (175 save)")
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", save=save)


if __name__ == "__main__":
    app.run(debug=True)
