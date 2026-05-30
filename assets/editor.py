"""Edit and create shorts from video"""

from moviepy.editor import VideoFileClip, concatenate_videoclips
from PIL import Image, ImageDraw, ImageFont
import cv2
import os

def create_shorts(video_path, moments):
    """
    Create 9:16 vertical shorts from best moments
    Returns: Number of shorts created
    """
    try:
        if not moments:
            print("No moments to create shorts from")
            return 0
        
        video = VideoFileClip(video_path)
        shorts_created = 0
        
        os.makedirs('output', exist_ok=True)
        
        for idx, moment in enumerate(moments[:5]):
            try:
                start = max(0, moment["start"])
                end = min(video.duration, moment["end"])
                
                # Extract clip
                clip = video.subclip(start, end)
                
                # Crop to 9:16 (vertical phone format)
                w, h = clip.size
                new_w = int(h * 9 / 16)
                x_center = (w - new_w) // 2
                
                clip = clip.crop(x1=x_center, x2=x_center+new_w, y1=0, y2=h)
                
                # Save
                output_path = f"output/SHORT_{idx+1}.mp4"
                clip.write_videofile(output_path, verbose=False, logger=None)
                shorts_created += 1
                print(f"✅ Created {output_path}")
            
            except Exception as e:
                print(f"Error creating short {idx+1}: {e}")
                continue
        
        video.close()
        return shorts_created
    
    except Exception as e:
        print(f"Editor error: {e}")
        return 0
