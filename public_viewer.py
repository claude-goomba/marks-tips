from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

TIPS_FILE = 'tips.json'

def load_tips():
    if os.path.exists(TIPS_FILE):
        with open(TIPS_FILE, 'r') as f:
            return json.load(f)
    return []

class PublicViewerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(self.get_html().encode())
        elif self.path == '/api/tips':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            tips = load_tips()
            self.wfile.write(json.dumps(tips).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def get_html(self):
        tips = load_tips()
        tips.reverse()  # Show newest first
        
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
                No tips yet. Check back soon!
            </div>
            '''
        
        return f'''<!DOCTYPE html>
<html>
<head>
    <title>Mark's Tips - Public Viewer</title>
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
        
        .info-box {{
            background: #e6f7ff;
            border: 1px solid #91d5ff;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 20px;
            text-align: center;
        }}
        
        .refresh-btn {{
            background: #40a9ff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
            margin-top: 10px;
        }}
        
        .refresh-btn:hover {{
            background: #1890ff;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Mark's Tips</h1>
        <div class="subtitle">Helpful tips and tricks by Mark (Public View)</div>
    </div>
    
    <div class="info-box">
        This is the public viewer - anyone can see tips here!<br>
        <button class="refresh-btn" onclick="location.reload()">🔄 Refresh</button>
    </div>
    
    <div class="tip-count">Total Tips: {len(tips)}</div>
    
    {tips_html}
    
    <script>
        // Auto-refresh every 30 seconds
        setTimeout(() => location.reload(), 30000);
    </script>
</body>
</html>'''

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8081), PublicViewerHandler)
    print("\n📖 Mark's Tips - Public Viewer")
    print("👀 View tips at: http://localhost:8081")
    print("🔄 Auto-refreshes every 30 seconds")
    print("\nPress Ctrl+C to stop the server\n")
    server.serve_forever()