#!/bin/bash

echo "🎬 Installing Shorts Maker..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Install from https://python.org"
    exit 1
fi

# Check FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  FFmpeg not found. Install: brew install ffmpeg (Mac) or apt install ffmpeg (Linux)"
    exit 1
fi

# Install Python packages
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

echo ""
echo "✅ Installation complete!"
echo ""
echo "📝 Next steps:"
echo "1. Get API key: https://aistudio.google.com/app/apikeys"
echo "2. Edit config.txt and paste your key"
echo "3. Run: python3 run_shorts_maker.py"
echo ""
