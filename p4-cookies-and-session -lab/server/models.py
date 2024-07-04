from flask import Flask, session, jsonify, request

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your secret key

# Dummy data for articles
articles = {
    1: {"id": 1, "title": "Article 1", "content": "Content of Article 1"},
    2: {"id": 2, "title": "Article 2", "content": "Content of Article 2"},
    3: {"id": 3, "title": "Article 3", "content": "Content of Article 3"},
    4: {"id": 4, "title": "Article 4", "content": "Content of Article 4"},
}

@app.route('/articles/<int:id>', methods=['GET'])
def get_article(id):
    # Set the initial value of page_views if it doesn't exist
    session['page_views'] = session.get('page_views', 0) + 1
    
    if session['page_views'] <= 3:
        article = articles.get(id)
        if article:
            return jsonify(article), 200
        else:
            return jsonify({'message': 'Article not found'}), 404
    else:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

@app.route('/clear', methods=['GET'])
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'}), 200

if __name__ == '__main__':
    app.run(debug=True)
