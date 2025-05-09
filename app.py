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
    df = pd.read_csv('static/data.csv')
    
    plt.figure(figsize=(5,5))
    plt.hist(df['value'], bins=5, edgecolor='black')
    plt.title('vecums')
    plt.xlabel('Vecums')
    plt.ylabel('Skaits')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close()
    
    df_table = pd.read_csv('static/table_data.csv')
    table_data = list(zip(df_table['Ilgums'], df_table['skaits']))
    
    df_horizontal = pd.read_csv('static/horizontal_data.csv')
    horizontal_data = {col: val for col, val in zip(df_horizontal.columns[1:], df_horizontal.iloc[0, 1:])}
    return render_template('data.html', plot_url=plot_url, value_counts=table_data, horizontal_data=horizontal_data)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

