# Mark's Groovy Tips ☮️

A far out web application for sharing tips and tricks with a groovy 60s vibe!

## 🌈 Three Groovy Ways to View Tips

### 1. Static Groovy Site (index.html) ✨ RECOMMENDED ✨
- **Generated static HTML with all tips included**
- Psychedelic 60s design with animations
- No server needed - just open in browser!
- Perfect for GitHub Pages hosting
- Generated with: `python3 generate_site.py`

### 2. Public Viewer (public_viewer.py)
- **No password required** - Anyone can view tips
- Auto-refreshes every 30 seconds
- Run with: `python3 public_viewer.py`
- Access at: http://localhost:8081

### 3. Full Application (simple_tips.py)
- View tips + password-protected posting
- Only Mark can post new tips (password: skous59)
- Run with: `python3 simple_tips.py`
- Access at: http://localhost:8080

## ✨ Groovy Features

- 🌸 Psychedelic 60s design with floating flowers
- ☮️ Peace signs and rainbow text effects
- 🎨 Lava lamp animations and wavy underlines
- 💾 Tips stored in JSON format
- 🔄 Static site generator creates beautiful HTML
- 📡 API endpoint at `/api/tips`

## 🚀 Quick Start

### For Groovy Viewing (Recommended):
```bash
python3 generate_site.py
# Then open index.html in your browser
```

### For Live Viewing (No Password Needed):
```bash
python3 public_viewer.py
# Then open http://localhost:8081
```

### For Mark (To Post Tips):
```bash
python3 simple_tips.py
# Then open http://localhost:8080
```

## 🔄 How the Static Site Generator Works

1. **Add Tips**: Use `simple_tips.py` to add tips (saves to `tips.json`)
2. **Generate Site**: Run `python3 generate_site.py` to create groovy HTML
3. **Share**: The `index.html` file contains ALL tips in beautiful 60s style
4. **No Server Needed**: Just open `index.html` in any browser!

## 🌟 Perfect for GitHub Pages

The generated `index.html` works perfectly with GitHub Pages:
1. Enable Pages in your repository settings
2. Set source to "Deploy from a branch" 
3. Choose "main" branch and "/ (root)"
4. Your groovy site will be live!

## 🔐 Password

The posting password is: `skous59`

Only people with this password can post new tips.

## 🎨 60s Design Elements

- Psychedelic background animations
- Rainbow gradient text effects
- Floating flower decorations
- Lava lamp animations
- Peace signs and groovy fonts
- Wavy underlines and tilted cards
- Far out color scheme

**Keep on truckin'! ✌️**