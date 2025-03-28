from flask import Flask, render_template
import sys
import matplotlib

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/data")
def data():
    return render_template('data.html')

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

    
