"""Detect visual peaks and spikes"""

import cv2
import numpy as np

def detect_visual_peaks(video_path, moments):
    """
    Add bonus points for visual spikes (scene changes, faces, movement)
    Returns: Updated moments list with adjusted scores
    """
    try:
        cap = cv2.VideoCapture(video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        prev_frame = None
        changes = []
        
        # Sample every 5 frames for speed
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            if frame_count % 5 == 0:
                if prev_frame is not None:
                    # Calculate scene change magnitude
                    diff = cv2.absdiff(cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY), 
                                       cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
                    change = np.mean(diff)
                    changes.append({
                        "time": frame_count / fps,
                        "magnitude": change
                    })
                prev_frame = frame.copy()
            
            frame_count += 1
        
        cap.release()
        
        # Bonus points if moment contains visual spike
        for moment in moments:
            bonus = 0
            for change in changes:
                if moment["start"] <= change["time"] <= moment["end"]:
                    if change["magnitude"] > 50:  # Significant change
                        bonus += 1
            
            moment["score"] = min(10, moment["score"] + bonus)
        
        return moments
    
    except Exception as e:
        print(f"Visual detection error: {e}")
        return moments
