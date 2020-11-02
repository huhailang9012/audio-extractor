import os
import os.path
import configparser
from django.shortcuts import render

ini_path = r"/data/config/ae.ini"
cp = configparser.ConfigParser()
cp.read(ini_path)
video_dir = cp.get("dir","video_dir")
audio_dir = cp.get("dir","audio_dir")

def index(request):
    videos = []
    get_path(video_dir, videos)
    convert(videos)
    return render(request,'ok')

def get_path(file_dir, all_files):
    """
    :param file_dir: 文件所在目录
    :param all_files: 存放文件地址的列表
    :return: 返回所有的文件列表
    """
    files = os.listdir(file_dir)
    for file_name in files:
        file_path = os.path.join(file_dir, file_name)
        all_files.append(file_path)
    return all_files


def convert(videos):
    """:param videos: 所有视频的路径列表
    """
    """ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
       ffmpeg -i 2018.mp4 -codec copy -bsf: h264_mp4toannexb -f h264 tmp.264
       ffmpeg -i killer.mp4 -an -vcodec copy out.h264
    """
    print('*' * 15 + 'Start to run:')
    # 分离音频的执行命令,{}{}分别为原始视频与输出后保存的路径名
    ffmpeg_cmd = 'ffmpeg -i {} -vn -y -acodec copy {}'
    for path in videos:
        video_name = os.path.basename(path)
        audio_prefix = video_name.split('.')[0]
        audio_extension = '.aac'
        audio_name = audio_prefix + audio_extension
        audio_path = os.path.join(audio_dir, audio_name)
        # 最终执行提取音频的指令
        cmd = ffmpeg_cmd.format(path, audio_path)
        os.system(cmd)

    print('End #################')

