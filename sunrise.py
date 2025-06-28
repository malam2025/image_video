from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips
import os

# File paths
image_paths = ["sun1.jpg", "sun2.jpg", "sun3.jpg"]
audio_path = "my_audio.mp3"
output_filename = "sun_slideshow_with_audio.mp4"

try:
    # Total video duration
    total_duration = 10  # seconds
    duration_per_image = total_duration / len(image_paths)

    # Create ImageClips
    image_clips = [
        ImageClip(img).set_duration(duration_per_image).resize(height=720)
        for img in image_paths if os.path.exists(img)
    ]

    video_clip = concatenate_videoclips(image_clips, method="compose")

    if os.path.exists(audio_path):
        audio_clip = AudioFileClip(audio_path).subclip(0, total_duration)
        video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(output_filename, fps=24)
    print(f"\n✅ Video created: {output_filename}")

except Exception as e:
    print(f"\n❌ Error: {e}")
