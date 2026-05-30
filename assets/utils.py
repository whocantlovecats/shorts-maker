"""Utility functions"""

import os
from pathlib import Path

def ensure_folders():
    """Create necessary folders"""
    Path('videos').mkdir(exist_ok=True)
    Path('output').mkdir(exist_ok=True)
    Path('assets').mkdir(exist_ok=True)

def get_video_files():
    """Get all video files in videos folder"""
    video_exts = ('.mp4', '.avi', '.mov', '.mkv')
    videos = []
    for file in os.listdir('videos'):
        if file.lower().endswith(video_exts):
            videos.append(file)
    return videos
