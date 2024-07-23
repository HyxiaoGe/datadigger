from flask import Flask, jsonify

from datadigger.rss.rss_gpt import fetch_xml

app = Flask(__name__)


@app.route('/articles')
def get_articles():
    articles = fetch_xml()
    return jsonify([article.to_dict() for article in articles])


if __name__ == '__main__':
    app.run(debug=True)
