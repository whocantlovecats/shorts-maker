#!/usr/bin/env python3
"""
Shorts Maker - Auto-analyze videos and create viral short-form content
Dead simple GUI - just drag, analyze, done!
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import threading

# Add assets folder to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'assets'))

try:
    from transcriber import transcribe_video
    from scorer import score_moments
    from detector import detect_visual_spikes
    from editor import cut_and_export_shorts
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure you've run: pip install -r requirements.txt")
    sys.exit(1)


class ShortsMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Shorts Maker - Auto Viral Clips")
        self.root.geometry("600x500")
        self.root.configure(bg="#1a1a1a")
        
        # Load config
        self.api_key = self.load_api_key()
        
        # Main UI
        self.setup_ui()
        self.video_path = None
    
    def load_api_key(self):
        """Load API key from config.txt"""
        config_path = "config.txt"
        
        if not os.path.exists(config_path):
            messagebox.showerror("Error", "config.txt not found!")
            return None
        
        try:
            with open(config_path, 'r') as f:
                for line in f:
                    if line.startswith('API_KEY='):
                        key = line.split('=', 1)[1].strip()
                        if key and key != "paste_your_key_here":
                            return key
            
            messagebox.showerror(
                "No API Key Found",
                "Please edit config.txt and add your API key from:\n"
                "https://aistudio.google.com/app/apikeys"
            )
            return None
        except Exception as e:
            messagebox.showerror("Config Error", f"Can't read config.txt: {e}")
            return None
    
    def setup_ui(self):
        """Create simple GUI"""
        # Title
        title = tk.Label(
            self.root,
            text="🎬 SHORTS MAKER",
            font=("Arial", 24, "bold"),
            fg="#00ff41",
            bg="#1a1a1a"
        )
        title.pack(pady=20)
        
        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Drop your video → Find viral moments → Auto-cut shorts",
            font=("Arial", 11),
            fg="#888",
            bg="#1a1a1a"
        )
        subtitle.pack(pady=5)
        
        # Video selection button
        self.select_btn = tk.Button(
            self.root,
            text="📁 SELECT VIDEO",
            font=("Arial", 14, "bold"),
            bg="#00ff41",
            fg="#000",
            padx=40,
            pady=15,
            command=self.select_video,
            cursor="hand2"
        )
        self.select_btn.pack(pady=20)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="No video selected",
            font=("Arial", 10),
            fg="#888",
            bg="#1a1a1a"
        )
        self.status_label.pack(pady=10)
        
        # Analyze button
        self.analyze_btn = tk.Button(
            self.root,
            text="▶️ ANALYZE & CREATE SHORTS",
            font=("Arial", 14, "bold"),
            bg="#ff6b35",
            fg="#fff",
            padx=40,
            pady=15,
            command=self.analyze_video,
            cursor="hand2",
            state="disabled"
        )
        self.analyze_btn.pack(pady=20)
        
        # Progress label
        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10),
            fg="#00ff41",
            bg="#1a1a1a"
        )
        self.progress_label.pack(pady=10)
        
        # Info box
        info = tk.Label(
            self.root,
            text="💡 Tips:\n"
                 "• Videos 5-30 min work best\n"
                 "• Clear audio = better results\n"
                 "• Processing takes 2-5 minutes\n"
                 "• Check /output folder for results",
            font=("Arial", 9),
            fg="#666",
            bg="#1a1a1a",
            justify="left"
        )
        info.pack(pady=20, padx=20)
    
    def select_video(self):
        """Pick a video file"""
        file = filedialog.askopenfilename(
            title="Select video",
            filetypes=[
                ("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"),
                ("All files", "*.*")
            ]
        )
        
        if file:
            self.video_path = file
            filename = os.path.basename(file)
            self.status_label.config(
                text=f"✅ Selected: {filename}",
                fg="#00ff41"
            )
            self.analyze_btn.config(state="normal")
    
    def analyze_video(self):
        """Run analysis in background thread"""
        if not self.video_path:
            messagebox.showwarning("No video", "Select a video first!")
            return
        
        if not self.api_key:
            messagebox.showerror(
                "No API Key",
                "API key not set. Edit config.txt with your key from:\n"
                "https://aistudio.google.com/app/apikeys"
            )
            return
        
        # Disable button during processing
        self.analyze_btn.config(state="disabled")
        self.select_btn.config(state="disabled")
        
        # Run in thread so UI doesn't freeze
        thread = threading.Thread(
            target=self.process_video,
            args=(self.video_path, self.api_key)
        )
        thread.daemon = True
        thread.start()
    
    def process_video(self, video_path, api_key):
        """Actual processing happens here"""
        try:
            self.update_progress("🎬 Transcribing audio...")
            transcript = transcribe_video(video_path)
            
            self.update_progress("🧠 Scoring moments with AI...")
            scored_moments = score_moments(transcript, api_key)
            
            self.update_progress("👁️ Detecting visual spikes...")
            visual_scores = detect_visual_spikes(video_path)
            
            self.update_progress("✂️ Cutting and exporting shorts...")
            output_files = cut_and_export_shorts(
                video_path,
                scored_moments,
                visual_scores
            )
            
            self.update_progress("✅ DONE! Check /output folder")
            messagebox.showinfo(
                "Success!",
                f"Created {len(output_files)} shorts!\n\n"
                f"Location: {os.path.abspath('output')}"
            )
            
        except Exception as e:
            self.update_progress(f"❌ Error: {str(e)[:50]}")
            messagebox.showerror("Error", f"Processing failed:\n{str(e)}")
        
        finally:
            self.analyze_btn.config(state="normal")
            self.select_btn.config(state="normal")
    
    def update_progress(self, message):
        """Update progress label safely"""
        self.root.after(0, lambda: self.progress_label.config(text=message))


if __name__ == "__main__":
    root = tk.Tk()
    app = ShortsMakerApp(root)
    root.mainloop()
