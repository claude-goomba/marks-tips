from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import urllib.parse
from datetime import datetime

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

class TipsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html().encode())
        elif self.path == '/add':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_add_form().encode())
        elif self.path == '/api/tips':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            tips = load_tips()
            self.wfile.write(json.dumps(tips).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_POST(self):
        if self.path == '/add':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            
            title = params.get('title', [''])[0]
            content = params.get('content', [''])[0]
            password = params.get('password', [''])[0]
            
            if password == POST_PASSWORD and title and content:
                tips = load_tips()
                new_tip = {
                    'id': len(tips) + 1,
                    'title': title,
                    'content': content,
                    'date': datetime.now().strftime('%Y-%m-%d %H:%M')
                }
                tips.append(new_tip)
                save_tips(tips)
                
                self.send_response(303)
                self.send_header('Location', '/?success=1')
                self.end_headers()
            else:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                error = "Incorrect password!" if password != POST_PASSWORD else "Please fill all fields!"
                self.wfile.write(self.get_add_form(error=error).encode())
    
    def get_html(self):
        tips = load_tips()
        tips.reverse()  # Show newest first
        
        success = 'success' in self.path
        
        tips_html = ''
        if tips:
            for tip in tips:
                tips_html += f'''
                <div class="tip-card">
                    <div class="tip-title">{tip['title']}</div>
                    <div class="tip-content">{tip['content']}</div>
                    <div class="tip-date">Posted on: {tip['date']}</div>
                </div>
                '''
        else:
            tips_html = '''
            <div class="no-tips">
                No tips yet. Be the first to share a tip!
            </div>
            '''
        
        return f'''<!DOCTYPE html>
<html>
<head>
    <title>Mark's Tips</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }}
        
        h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        
        .subtitle {{
            margin-top: 10px;
            opacity: 0.9;
        }}
        
        .tip-card {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}
        
        .tip-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        }}
        
        .tip-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .tip-content {{
            color: #666;
            line-height: 1.6;
            white-space: pre-wrap;
        }}
        
        .tip-date {{
            color: #999;
            font-size: 0.9em;
            margin-top: 10px;
        }}
        
        .add-tip-btn {{
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-bottom: 20px;
            transition: background 0.3s;
            text-decoration: none;
            display: inline-block;
        }}
        
        .add-tip-btn:hover {{
            background: #5a67d8;
        }}
        
        .success {{
            background: #48bb78;
            color: white;
            padding: 10px 20px;
            border-radius: 6px;
            margin-bottom: 20px;
            text-align: center;
        }}
        
        .tip-count {{
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-style: italic;
        }}
        
        .no-tips {{
            text-align: center;
            color: #999;
            padding: 40px;
            background: white;
            border-radius: 8px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Mark's Tips</h1>
        <div class="subtitle">Helpful tips and tricks by Mark</div>
    </div>
    
    {'<div class="success">Tip posted successfully!</div>' if success else ''}
    
    <a href="/add" class="add-tip-btn">+ Add New Tip</a>
    
    <div class="tip-count">Total Tips: {len(tips)}</div>
    
    {tips_html}
    
</body>
</html>'''
    
    def get_add_form(self, error=None):
        return f'''<!DOCTYPE html>
<html>
<head>
    <title>Add Tip - Mark's Tips</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 30px;
        }}
        
        h1 {{
            margin: 0;
            font-size: 2.5em;
        }}
        
        .form-container {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        input, textarea {{
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }}
        
        textarea {{
            min-height: 150px;
            resize: vertical;
        }}
        
        .form-buttons {{
            display: flex;
            gap: 10px;
        }}
        
        .submit-btn {{
            background: #48bb78;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }}
        
        .cancel-btn {{
            background: #e53e3e;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            text-decoration: none;
            display: inline-block;
        }}
        
        .error {{
            background: #fed7d7;
            color: #c53030;
            padding: 10px;
            border-radius: 4px;
            margin-bottom: 15px;
        }}
        
        .password-hint {{
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Add a New Tip</h1>
    </div>
    
    <div class="form-container">
        {'<div class="error">' + error + '</div>' if error else ''}
        
        <form method="POST" action="/add">
            <input type="text" name="title" placeholder="Tip Title" required>
            <textarea name="content" placeholder="Write your tip here..." required></textarea>
            <input type="password" name="password" placeholder="Password" required>
            <div class="password-hint">Enter the password to post tips</div>
            
            <div class="form-buttons">
                <button type="submit" class="submit-btn">Post Tip</button>
                <a href="/" class="cancel-btn">Cancel</a>
            </div>
        </form>
    </div>
</body>
</html>'''

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), TipsHandler)
    print("\n✨ Mark's Tips Application")
    print("📝 View tips at: http://localhost:8080")
    print("🔐 Password for posting: skous59")
    print("\nPress Ctrl+C to stop the server\n")
    server.serve_forever()