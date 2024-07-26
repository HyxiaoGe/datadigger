from flask import Flask, jsonify, request

from datadigger.rss.rss_gpt import fetch_xml

app = Flask(__name__)


@app.route('/articles')
def get_articles():
    platform = request.args.get("platform", None)
    if platform:
        articles = fetch_xml(platform)
        return jsonify([article.to_dict() for article in articles])
    else:
        return 'platform must be provided'


if __name__ == '__main__':
    app.run(debug=True)
