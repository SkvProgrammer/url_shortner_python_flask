from flask import Flask, render_template, request, redirect
import pyshorteners

app = Flask(__name__)

url_mapping = {}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(original_url)
    url_mapping[short_url] = original_url
    return render_template('shorten.html', short_url=short_url)


@app.route('/<short_url>')
def redirect_to_url(short_url):
    if short_url in url_mapping:
        original_url = url_mapping[short_url]
        return redirect(original_url)
    else:
        return "Invalid short URL"


if __name__ == '__main__':
    app.run(debug=True)
