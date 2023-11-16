from flask import request, jsonify
from app import app, db
from app.models import Post

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

# Get all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    formatted_posts = [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
    return jsonify({'posts': formatted_posts})

# Get a specific post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify({'id': post.id, 'title': post.title, 'content': post.content})

# Update a post by ID
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'})

# Delete a post by ID
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'})
