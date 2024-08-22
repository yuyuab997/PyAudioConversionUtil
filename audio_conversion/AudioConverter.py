import time

from moviepy.editor import VideoFileClip


def ac_mp4_to_mp3(input_file_path: str, output_file_path: str) -> None:
    # 加载 MP4 文件
    video = VideoFileClip(input_file_path)

    # 提取音频并保存为 MP3
    video.audio.write_audiofile(output_file_path.replace('.mp4', '') + str(int(time.time())) + '.mp3')


