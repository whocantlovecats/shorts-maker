# 🎬 Shorts Maker

Turn your long videos into viral **TikTok/YouTube Shorts** automatically. No coding required!

## ✨ Features

✅ **Automatic Analysis** - AI finds the best moments  
✅ **Smart Scoring** - Rates moments for virality (hook, emotion, payoff)  
✅ **Visual Detection** - Finds scene changes and spikes  
✅ **Auto Cropping** - Converts to 9:16 vertical format  
✅ **Caption Ready** - Burns timestamps for clarity  
✅ **100% FREE** - No subscriptions or hidden costs  

## 🚀 Quick Start

### 1. **Install (5 min)**

**Windows:** Double-click `install.bat`  
**Mac/Linux:** Run `bash install.sh`

Or manually:
```bash
pip install -r requirements.txt
```

### 2. **Get API Key (2 min - FREE)**

1. Go to: https://aistudio.google.com/app/apikeys
2. Click **"Create API Key"** → **"Create API key in new project"**
3. Copy your key
4. Open `config.txt` in this folder
5. Replace `paste_your_api_key_here` with your key
6. Save

### 3. **Run It!**

```bash
python run_shorts_maker.py
```

A window pops up:
- Click **"📁 Browse & Select Video"**
- Click **"▶️ ANALYZE & CREATE SHORTS"**
- Wait 2-5 minutes ☕
- Find shorts in `/output` folder

## 📦 What's Included

- **run_shorts_maker.py** - Main app (just run this!)
- **config.txt** - Your API key goes here
- **requirements.txt** - All dependencies
- **assets/** - Core processing code

## 🔧 How It Works

1. **Transcribe** - Speech to text (timestamps included)
2. **Score Moments** - AI rates each segment 1-10 for virality
3. **Visual Detection** - Finds scene changes + movement
4. **Rank** - Combines text + visual scores
5. **Create Shorts** - Exports top moments as 9:16 vertical videos
6. **Export** - Ready for TikTok/YouTube Shorts

## 💰 Cost

**$0** - Completely free!

- Google AI Studio: Free tier (no credit card)
- FFmpeg: Open source
- MoviePy: Open source
- All other tools: Open source

## ⚡ Requirements

- Python 3.8+
- FFmpeg (installed via installer or manually)
- 4GB RAM (minimum)
- Internet (for first-run setup only)

## 🐛 Troubleshooting

**"Module not found" error?**
```bash
pip install -r requirements.txt
```

**"FFmpeg not found" error?**
- Windows: Install from https://ffmpeg.org/download.html
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

**API key not working?**
- Make sure you copied the FULL key
- Check config.txt has no extra spaces
- Restart the app

## 📝 License

MIT License - Use freely!

## 🎯 Next Steps

- Add your API key to `config.txt`
- Run the app
- Drop a video in
- Get shorts! 🎉
