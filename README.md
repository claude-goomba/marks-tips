# Mark's Tips Application

A simple web application for sharing tips and tricks, with password-protected posting.

## Features

- View all tips posted by Mark
- Password-protected tip posting (password: skous59)
- Clean, modern interface
- Tips are stored locally in JSON format
- Newest tips appear first

## Installation

1. Install Flask:
```bash
pip install flask
```

2. Run the application:
```bash
python tips_app.py
```

3. Open your browser to http://localhost:5000

## Usage

- **View Tips**: Just visit the homepage to see all tips
- **Add Tips**: Click "Add New Tip" and enter the password (skous59)
- **API Access**: Get tips as JSON at http://localhost:5000/api/tips

## Password

The posting password is: `skous59`

Only people with this password can post new tips.