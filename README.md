# Mark's Tips Application

A web application for sharing tips and tricks, with separate interfaces for posting and viewing.

## Two Versions Available

### 1. Public Viewer (public_viewer.py)
- **No password required** - Anyone can view tips
- Auto-refreshes every 30 seconds
- Perfect for sharing with others
- Run with: `python3 public_viewer.py`
- Access at: http://localhost:8081

### 2. Full Application (simple_tips.py)
- View tips + password-protected posting
- Only Mark can post new tips (password: skous59)
- Run with: `python3 simple_tips.py`
- Access at: http://localhost:8080

## Features

- 📖 View all tips posted by Mark
- 🔐 Password-protected tip posting
- 🎨 Clean, modern interface
- 💾 Tips stored in JSON format
- 🔄 Newest tips appear first
- 📡 API endpoint at `/api/tips`

## Quick Start

### For Viewers (No Password Needed):
```bash
python3 public_viewer.py
```
Then open http://localhost:8081

### For Mark (To Post Tips):
```bash
python3 simple_tips.py
```
Then open http://localhost:8080

## How It Works

1. **Tips Storage**: All tips are saved in `tips.json`
2. **Public Access**: Anyone can run `public_viewer.py` to see tips
3. **Posting Access**: Only people with the password can post via `simple_tips.py`

## Password

The posting password is: `skous59`

Only people with this password can post new tips.