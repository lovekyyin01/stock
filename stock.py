from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = {}
    if request.method == 'POST':
        stock_no = request.form['stock_no']
        symbol = stock_no + '.HK'
        info = yf.Ticker(symbol).info
        stock_data = {
            'stock_no': stock_no,
            'name': info.get('longName', 'N/A'),
            'price': info.get('regularMarketPrice', 'N/A'),
            'amount': info.get('regularMarketVolume', 'N/A')
        }
    return render_template('table.html', stock_data=stock_data)

if __name__ == '__main__':
    app.run(debug=True)