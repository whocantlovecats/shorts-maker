"""Transcribe video audio to text with timestamps"""

import os
from faster_whisper import WhisperModel

def transcribe_video(video_path):
    """
    Transcribe video using Faster Whisper (free, local)
    Returns: List of {"time": seconds, "text": "...", "start": s, "end": s}
    """
    try:
        # Use tiny model for speed (runs locally, no API needed)
        model = WhisperModel("tiny", device="cpu", compute_type="int8")
        segments, info = model.transcribe(video_path, language="en")
        
        transcript = []
        for segment in segments:
            transcript.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text,
                "time": segment.start
            })
        
        return transcript
    except Exception as e:
        print(f"Transcription error: {e}")
        return []
