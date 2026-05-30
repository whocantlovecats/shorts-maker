"""Score moments for virality using AI"""

import google.generativeai as genai

def score_moments(transcript, api_key):
    """
    Score transcript chunks for virality
    Returns: List of {"start": s, "end": s, "text": "...", "score": 1-10}
    """
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')
        
        moments = []
        
        # Group transcript into 30-60 second chunks
        chunk_size = 10  # ~10 segments per chunk
        for i in range(0, len(transcript), chunk_size):
            chunk = transcript[i:i+chunk_size]
            if not chunk:
                continue
            
            text = " ".join([seg["text"] for seg in chunk])
            start = chunk[0]["start"]
            end = chunk[-1]["end"]
            
            # Ask AI to score
            prompt = f"""Rate this video moment from 1-10 for short-form virality (TikTok/YouTube Shorts). 
Consider: hook quality, emotional impact, pacing, clarity, retention. 
Just respond with a number 1-10, nothing else.

Text: {text}"""
            
            try:
                response = model.generate_content(prompt)
                score = int(response.text.strip())
                score = max(1, min(10, score))  # Clamp 1-10
            except:
                score = 5  # Default if parsing fails
            
            moments.append({
                "start": start,
                "end": end,
                "text": text,
                "score": score
            })
        
        # Sort by score, keep top 5
        moments = sorted(moments, key=lambda x: x["score"], reverse=True)[:5]
        return moments
    
    except Exception as e:
        print(f"Scoring error: {e}")
        return []
