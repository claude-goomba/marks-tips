import json
import os
from datetime import datetime

def load_tips():
    if os.path.exists('tips.json'):
        with open('tips.json', 'r') as f:
            return json.load(f)
    return []

def generate_60s_site():
    tips = load_tips()
    tips.reverse()  # Newest first
    
    tips_html = ''
    for i, tip in enumerate(tips):
        # Alternate colors for groovy effect
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F']
        color = colors[i % len(colors)]
        
        tips_html += f'''
        <div class="tip-card" style="border-color: {color};">
            <div class="tip-number" style="background: {color};">#{tip.get('id', i+1)}</div>
            <h2 class="tip-title">{tip.get('title', 'Untitled')}</h2>
            <div class="tip-content">{tip.get('content', '').replace(chr(10), '<br>')}</div>
            <div class="tip-footer">
                <span class="tip-date">✿ {tip.get('date', 'Unknown date')} ✿</span>
            </div>
        </div>
        '''
    
    if not tips_html:
        tips_html = '''
        <div class="tip-card">
            <h2 class="tip-title">No tips yet!</h2>
            <div class="tip-content">Stay groovy, tips are coming soon!</div>
        </div>
        '''
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mark's Groovy Tips - Peace, Love & Knowledge</title>
    <link href="https://fonts.googleapis.com/css2?family=Righteous&family=Kalam:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background: #2C3E50;
            font-family: 'Kalam', cursive;
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }}
        
        /* Psychedelic background pattern */
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 50%, rgba(255, 107, 107, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(78, 205, 196, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(247, 220, 111, 0.3) 0%, transparent 50%),
                radial-gradient(circle at 80% 10%, rgba(152, 216, 200, 0.3) 0%, transparent 50%);
            animation: psychedelic 20s ease-in-out infinite;
            z-index: -1;
        }}
        
        @keyframes psychedelic {{
            0%, 100% {{ transform: scale(1) rotate(0deg); }}
            25% {{ transform: scale(1.1) rotate(90deg); }}
            50% {{ transform: scale(1) rotate(180deg); }}
            75% {{ transform: scale(1.1) rotate(270deg); }}
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            position: relative;
            z-index: 1;
        }}
        
        /* Groovy header */
        .header {{
            text-align: center;
            padding: 40px 20px;
            margin-bottom: 40px;
            position: relative;
        }}
        
        .main-title {{
            font-family: 'Righteous', cursive;
            font-size: 4em;
            margin: 0;
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #FFA07A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 3px 3px 0px rgba(0,0,0,0.1);
            animation: rainbow 5s ease-in-out infinite;
            position: relative;
        }}
        
        @keyframes rainbow {{
            0%, 100% {{ filter: hue-rotate(0deg); }}
            50% {{ filter: hue-rotate(180deg); }}
        }}
        
        .subtitle {{
            font-size: 1.5em;
            color: #F7DC6F;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        /* Peace signs decoration */
        .peace-sign {{
            display: inline-block;
            font-size: 2em;
            animation: spin 4s linear infinite;
            color: #F7DC6F;
        }}
        
        @keyframes spin {{
            from {{ transform: rotate(0deg); }}
            to {{ transform: rotate(360deg); }}
        }}
        
        /* Tip cards with 60s style */
        .tip-card {{
            background: #FDFEFE;
            border-radius: 20px;
            padding: 30px;
            margin-bottom: 30px;
            position: relative;
            border: 4px solid #FF6B6B;
            box-shadow: 
                5px 5px 0px rgba(0,0,0,0.1),
                10px 10px 20px rgba(0,0,0,0.2);
            transform: rotate(-1deg);
            transition: all 0.3s ease;
        }}
        
        .tip-card:nth-child(even) {{
            transform: rotate(1deg);
        }}
        
        .tip-card:hover {{
            transform: rotate(0deg) scale(1.02);
            box-shadow: 
                8px 8px 0px rgba(0,0,0,0.1),
                15px 15px 30px rgba(0,0,0,0.3);
        }}
        
        .tip-number {{
            position: absolute;
            top: -20px;
            right: 20px;
            background: #FF6B6B;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Righteous', cursive;
            font-size: 1.5em;
            transform: rotate(15deg);
            box-shadow: 3px 3px 10px rgba(0,0,0,0.2);
        }}
        
        .tip-title {{
            font-family: 'Righteous', cursive;
            font-size: 2em;
            color: #2C3E50;
            margin: 0 0 20px 0;
            text-decoration: underline;
            text-decoration-style: wavy;
            text-decoration-color: #4ECDC4;
        }}
        
        .tip-content {{
            font-size: 1.2em;
            line-height: 1.8;
            color: #34495E;
            background: linear-gradient(to right, transparent 0%, rgba(255,255,255,0.5) 50%, transparent 100%);
            padding: 10px;
            border-radius: 10px;
        }}
        
        .tip-footer {{
            margin-top: 20px;
            text-align: center;
            color: #7F8C8D;
            font-style: italic;
        }}
        
        .tip-date {{
            font-size: 1em;
            padding: 5px 15px;
            background: rgba(247, 220, 111, 0.3);
            border-radius: 20px;
            display: inline-block;
        }}
        
        /* Flower power decorations */
        .flower {{
            position: fixed;
            font-size: 2em;
            animation: float 10s infinite ease-in-out;
            z-index: 0;
            opacity: 0.5;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(180deg); }}
        }}
        
        /* Footer */
        .footer {{
            text-align: center;
            padding: 40px 20px;
            color: #F7DC6F;
            font-size: 1.2em;
        }}
        
        .footer a {{
            color: #4ECDC4;
            text-decoration: none;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .main-title {{
                font-size: 3em;
            }}
            
            .tip-card {{
                padding: 20px;
                margin-bottom: 20px;
            }}
            
            .tip-title {{
                font-size: 1.5em;
            }}
        }}
        
        /* Loading animation */
        .tips-container {{
            animation: fadeIn 1s ease-in;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        /* Counter */
        .tip-counter {{
            text-align: center;
            font-family: 'Righteous', cursive;
            font-size: 1.5em;
            color: #F7DC6F;
            margin: 30px 0;
            padding: 15px;
            background: rgba(0,0,0,0.2);
            border-radius: 50px;
            display: inline-block;
            width: 100%;
        }}
        
        /* Lava lamp effect */
        .lava-lamp {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 80px;
            height: 150px;
            background: linear-gradient(to bottom, #FF6B6B, #4ECDC4);
            border-radius: 40px;
            opacity: 0.3;
            animation: lava 8s ease-in-out infinite;
        }}
        
        @keyframes lava {{
            0%, 100% {{ transform: scaleY(1); }}
            50% {{ transform: scaleY(1.2); }}
        }}
    </style>
</head>
<body>
    <!-- Floating flowers -->
    <div class="flower" style="top: 10%; left: 10%;">🌻</div>
    <div class="flower" style="top: 20%; right: 15%; animation-delay: 2s;">🌸</div>
    <div class="flower" style="top: 60%; left: 5%; animation-delay: 4s;">🌺</div>
    <div class="flower" style="top: 80%; right: 10%; animation-delay: 6s;">🌼</div>
    <div class="flower" style="top: 40%; right: 5%; animation-delay: 8s;">🌷</div>
    
    <div class="container">
        <div class="header">
            <div class="peace-sign">☮</div>
            <h1 class="main-title">Mark's Groovy Tips</h1>
            <div class="peace-sign">☮</div>
            <p class="subtitle">✨ Peace, Love & Knowledge ✨</p>
            <p class="subtitle">Far out tips for hip cats!</p>
        </div>
        
        <div class="tip-counter">
            🎯 Total Groovy Tips: {len(tips)} 🎯
        </div>
        
        <div class="tips-container">
            {tips_html}
        </div>
        
        <div class="footer">
            <p>Keep on truckin'! ✌️</p>
            <p>Made with 💜 in the spirit of the 60s</p>
            <p>Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
        </div>
    </div>
    
    <div class="lava-lamp"></div>
</body>
</html>'''
    
    # Write the HTML file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✨ Groovy site generated! ✨")
    print(f"📝 Total tips: {len(tips)}")
    print("🌈 Open index.html to see your far out tips page!")

if __name__ == '__main__':
    generate_60s_site()