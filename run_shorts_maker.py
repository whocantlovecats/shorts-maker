#!/usr/bin/env python3
"""
Shorts Maker - Turn long videos into viral shorts automatically
No coding required - just run this file!
"""

import os
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from pathlib import Path

# Check if assets folder exists
if not os.path.exists('assets'):
    os.makedirs('assets')

try:
    from assets.transcriber import transcribe_video
    from assets.scorer import score_moments
    from assets.detector import detect_visual_peaks
    from assets.editor import create_shorts
except ImportError:
    print("❌ Missing files! Creating them...")
    # Will create empty stubs
    pass

class ShortsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Shorts Maker")
        self.root.geometry("600x500")
        self.root.config(bg="#1e1e1e")
        
        self.video_path = tk.StringVar()
        self.api_key = self.load_api_key()
        
        self.setup_ui()
    
    def load_api_key(self):
        """Load API key from config.txt"""
        try:
            with open('config.txt', 'r') as f:
                for line in f:
                    if line.startswith('API_KEY='):
                        key = line.split('=')[1].strip()
                        if key != 'paste_your_api_key_here':
                            return key
        except:
            pass
        return None
    
    def setup_ui(self):
        """Create the user interface"""
        # Title
        title = tk.Label(self.root, text="🎬 Shorts Maker", font=("Arial", 24, "bold"), fg="#00ff88", bg="#1e1e1e")
        title.pack(pady=20)
        
        # Info
        info = tk.Label(self.root, text="Turn your videos into viral shorts automatically!", font=("Arial", 12), fg="#aaa", bg="#1e1e1e")
        info.pack()
        
        # API Key Status
        if self.api_key:
            key_status = tk.Label(self.root, text="✅ API Key loaded", font=("Arial", 10), fg="#00ff88", bg="#1e1e1e")
        else:
            key_status = tk.Label(self.root, text="⚠️  No API key found in config.txt", font=("Arial", 10), fg="#ff6b6b", bg="#1e1e1e")
        key_status.pack(pady=5)
        
        # Setup button
        setup_btn = tk.Button(self.root, text="🔑 Setup API Key", command=self.setup_api_key, bg="#ff6b6b", fg="white", font=("Arial", 11, "bold"), width=25)
        setup_btn.pack(pady=10)
        
        # Video selection
        select_btn = tk.Button(self.root, text="📁 Browse & Select Video", command=self.select_video, bg="#4a9eff", fg="white", font=("Arial", 12, "bold"), width=25, height=2)
        select_btn.pack(pady=20)
        
        # Selected video display
        self.video_label = tk.Label(self.root, text="No video selected", font=("Arial", 10), fg="#aaa", bg="#2a2a2a", wraplength=500, justify="left")
        self.video_label.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Process button
        self.process_btn = tk.Button(self.root, text="▶️ ANALYZE & CREATE SHORTS", command=self.process_video, bg="#00ff88", fg="#000", font=("Arial", 12, "bold"), width=25, height=2)
        self.process_btn.pack(pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode='indeterminate')
        self.progress.pack(pady=10, padx=20, fill="x")
        
        # Status label
        self.status_label = tk.Label(self.root, text="Ready!", font=("Arial", 10), fg="#aaa", bg="#1e1e1e")
        self.status_label.pack(pady=5)
    
    def setup_api_key(self):
        """Guide user to setup API key"""
        messagebox.showinfo("Setup API Key", 
            "1. Go to: https://aistudio.google.com/app/apikeys\n"
            "2. Click 'Create API Key'\n"
            "3. Copy the key\n"
            "4. Open config.txt in this folder\n"
            "5. Replace 'paste_your_api_key_here' with your key\n"
            "6. Save and restart this app\n\n"
            "It's completely FREE - no credit card needed!")
    
    def select_video(self):
        """Let user select a video file"""
        file = filedialog.askopenfilename(
            title="Select a video",
            filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*")]
        )
        if file:
            self.video_path.set(file)
            self.video_label.config(text=f"Selected: {os.path.basename(file)}")
    
    def process_video(self):
        """Process the video in background thread"""
        if not self.video_path.get():
            messagebox.showerror("Error", "Please select a video first!")
            return
        
        if not self.api_key:
            messagebox.showerror("Error", "Please setup your API key first!")
            return
        
        self.process_btn.config(state="disabled")
        self.progress.start()
        self.status_label.config(text="Processing... (this may take a few minutes)")
        
        thread = threading.Thread(target=self._process_thread)
        thread.start()
    
    def _process_thread(self):
        """Background processing thread"""
        try:
            video_file = self.video_path.get()
            
            # Create output folder
            os.makedirs('output', exist_ok=True)
            
            self.status_label.config(text="📝 Transcribing audio...")
            self.root.update()
            
            # Step 1: Transcribe
            transcript = transcribe_video(video_file)
            
            self.status_label.config(text="🎯 Scoring moments...")
            self.root.update()
            
            # Step 2: Score
            moments = score_moments(transcript, self.api_key)
            
            self.status_label.config(text="👁️ Detecting visual peaks...")
            self.root.update()
            
            # Step 3: Detect visuals
            moments = detect_visual_peaks(video_file, moments)
            
            self.status_label.config(text="✂️ Creating shorts...")
            self.root.update()
            
            # Step 4: Create shorts
            shorts_created = create_shorts(video_file, moments)
            
            self.status_label.config(text=f"✅ Done! Created {shorts_created} shorts")
            messagebox.showinfo("Success!", f"Created {shorts_created} shorts!\n\nFind them in: ./output")
            
        except Exception as e:
            self.status_label.config(text="❌ Error occurred")
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
        finally:
            self.progress.stop()
            self.process_btn.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShortsApp(root)
    root.mainloop()
