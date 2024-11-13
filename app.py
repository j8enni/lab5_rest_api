# app.py
from flask import Flask, render_template, request
import parser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        books = parser.get_books(query)  # Парсим книги по запросу
        return render_template('form.html', books=books)
    return render_template('form.html', books=None)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
