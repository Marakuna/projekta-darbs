from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__, static_folder='static')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/data")
def data():
    # Read CSV data
    df = pd.read_csv('static/data.csv')
    
    # Create histogram
    plt.figure(figsize=(8,4))
    plt.hist(df['value'], bins=20, edgecolor='black')
    plt.title('Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True, alpha=0.3)
    
    
    
    # Save plot to base64 string
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    
    return render_template('data.html', plot_url=plot_url)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

