# 📋 Setup Guide

## Prerequisites

- Python 3.8 or higher
- FFmpeg
- Internet connection (initial setup)

## Step 1: Install Python

### Windows
1. Go to https://python.org
2. Download "Windows installer (64-bit)"
3. Run installer
4. **IMPORTANT:** Check "Add Python to PATH"
5. Click "Install Now"

### Mac
```bash
brew install python3
```

### Linux
```bash
sudo apt install python3 python3-pip
```

## Step 2: Install FFmpeg

### Windows
1. Go to https://ffmpeg.org/download.html
2. Download Windows build
3. Extract to `C:\ffmpeg`
4. Add to PATH:
   - Search "Environment Variables"
   - Click "Edit Environment Variables"
   - Add `C:\ffmpeg\bin` to PATH
   - Restart computer

### Mac
```bash
brew install ffmpeg
```

### Linux
```bash
sudo apt install ffmpeg
```

## Step 3: Clone/Download Repository

```bash
git clone https://github.com/whocantlovecats/shorts-maker.git
cd shorts-maker
```

OR download ZIP from GitHub and extract

## Step 4: Install Python Packages

### Windows (Command Prompt)
```bash
install.bat
```

### Mac/Linux (Terminal)
```bash
bash install.sh
```

### Manual (All Systems)
```bash
pip install -r requirements.txt
```

## Step 5: Get API Key

1. Go to https://aistudio.google.com/app/apikeys
2. Sign in with Google account (free)
3. Click **"Create API Key"**
4. Click **"Create API key in new project"**
5. Copy the key (long string like `AIzaSy...`)

## Step 6: Add API Key to Config

1. Open `config.txt` in text editor
2. Find: `API_KEY=paste_your_api_key_here`
3. Replace with: `API_KEY=YOUR_ACTUAL_KEY_HERE`
4. Save file

Example:
```
API_KEY=AIzaSyD_1234567890abcdefghijklmno
```

## Step 7: Run the App!

### Windows
```bash
python run_shorts_maker.py
```

### Mac/Linux
```bash
python3 run_shorts_maker.py
```

A GUI window will appear!

## Troubleshooting

### "Python not found"
- Make sure Python is in PATH
- Restart computer after installation
- Try `python3` instead of `python`

### "FFmpeg not found"
- Install FFmpeg
- Add to PATH
- Restart computer
- Verify: `ffmpeg -version` in terminal

### "Module not found"
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### "API key error"
- Check for typos in config.txt
- Make sure no extra spaces
- Try getting a new key

## Success!

Once app opens with GUI, you're ready to go! 🎉

## Need Help?

Check README.md for more info or visit:
https://github.com/whocantlovecats/shorts-maker
