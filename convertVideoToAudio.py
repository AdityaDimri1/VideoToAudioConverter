import moviepy.editor
video=moviepy.editor.VideoFileClip('vi.mp4')
audio=video.audio
audio.write_audiofile('vi.mp3')