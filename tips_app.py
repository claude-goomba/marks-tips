from flask import Flask, render_template_string, request, redirect, url_for, session, jsonify
import json
import os
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

TIPS_FILE = 'tips.json'
POST_PASSWORD = 'skous59'

def load_tips():
    if os.path.exists(TIPS_FILE):
        with open(TIPS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tips(tips):
    with open(TIPS_FILE, 'w') as f:
        json.dump(tips, f, indent=2)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mark's Tips</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }
        
        h1 {
            margin: 0;
            font-size: 2.5em;
        }
        
        .subtitle {
            margin-top: 10px;
            opacity: 0.9;
        }
        
        .tip-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }
        
        .tip-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }
        
        .tip-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }
        
        .tip-content {
            color: #666;
            line-height: 1.6;
            white-space: pre-wrap;
        }
        
        .tip-date {
            color: #999;
            font-size: 0.9em;
            margin-top: 10px;
        }
        
        .add-tip-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 20px;
            transition: background 0.3s;
        }
        
        .add-tip-btn:hover {
            background: #5a67d8;
        }
        
        .form-container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }
        
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        textarea {
            min-height: 150px;
            resize: vertical;
        }
        
        .form-buttons {
            display: flex;
            gap: 10px;
        }
        
        .submit-btn {
            background: #48bb78;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        
        .cancel-btn {
            background: #e53e3e;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        
        .error {
            color: #e53e3e;
            margin-bottom: 10px;
        }
        
        .success {
            color: #48bb78;
            margin-bottom: 10px;
        }
        
        .no-tips {
            text-align: center;
            color: #999;
            padding: 40px;
            background: white;
            border-radius: 8px;
        }
        
        .tip-count {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Mark's Tips</h1>
        <div class="subtitle">Helpful tips and tricks by Mark</div>
    </div>
    
    {% if not show_form %}
        <button class="add-tip-btn" onclick="window.location.href='{{ url_for('add_tip') }}'">
            + Add New Tip
        </button>
    {% endif %}
    
    {% if show_form %}
        <div class="form-container">
            <h2>Add a New Tip</h2>
            {% if error %}
                <div class="error">{{ error }}</div>
            {% endif %}
            <form method="POST" action="{{ url_for('add_tip') }}">
                <input type="text" name="title" placeholder="Tip Title" required>
                <textarea name="content" placeholder="Write your tip here..." required></textarea>
                <input type="password" name="password" placeholder="Password" required>
                <div class="form-buttons">
                    <button type="submit" class="submit-btn">Post Tip</button>
                    <button type="button" class="cancel-btn" onclick="window.location.href='{{ url_for('index') }}'">Cancel</button>
                </div>
            </form>
        </div>
    {% endif %}
    
    {% if success %}
        <div class="success">Tip posted successfully!</div>
    {% endif %}
    
    <div class="tip-count">Total Tips: {{ tips|length }}</div>
    
    {% if tips %}
        {% for tip in tips %}
            <div class="tip-card">
                <div class="tip-title">{{ tip.title }}</div>
                <div class="tip-content">{{ tip.content }}</div>
                <div class="tip-date">Posted on: {{ tip.date }}</div>
            </div>
        {% endfor %}
    {% else %}
        <div class="no-tips">
            No tips yet. Be the first to share a tip!
        </div>
    {% endif %}
</body>
</html>
'''

@app.route('/')
def index():
    tips = load_tips()
    tips.reverse()  # Show newest first
    return render_template_string(HTML_TEMPLATE, tips=tips, show_form=False, success=request.args.get('success'))

@app.route('/add', methods=['GET', 'POST'])
def add_tip():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        password = request.form.get('password', '')
        
        if password != POST_PASSWORD:
            tips = load_tips()
            return render_template_string(HTML_TEMPLATE, tips=tips, show_form=True, error="Incorrect password!")
        
        if title and content:
            tips = load_tips()
            new_tip = {
                'id': len(tips) + 1,
                'title': title,
                'content': content,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M')
            }
            tips.append(new_tip)
            save_tips(tips)
            return redirect(url_for('index', success=1))
    
    tips = load_tips()
    return render_template_string(HTML_TEMPLATE, tips=tips, show_form=True)

@app.route('/api/tips')
def api_tips():
    tips = load_tips()
    return jsonify(tips)

if __name__ == '__main__':
    print("\n✨ Mark's Tips Application")
    print("📝 View tips at: http://localhost:5000")
    print("🔐 Password for posting: skous59")
    print("\nPress Ctrl+C to stop the server\n")
    app.run(debug=True, port=5000)