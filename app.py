from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "ajay": "password123",
    "admin": "admin123"
}

questions = []  # Simple in-memory storage

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('community.html', questions=questions)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        q = {
            "question": request.form['question'],
            "description": request.form['description'],
            "tags": request.form['tags'],
            "status": "Open",
            "comments": 0
        }
        questions.append(q)
        return redirect(url_for('dashboard'))
    return render_template('ask.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', error="Invalid username or password.")

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/dashboard-stats')
def dashboard_stats():
    total_questions = len(questions)
    replies = sum(1 for q in questions if q.get('comments', 0) > 0)
    categories = {}

    for q in questions:
        tag = q.get("tags", "General").
