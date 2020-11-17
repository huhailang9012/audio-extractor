import os
import os.path
# import configparser


# ini_path = r"/data/config/Audio-Extracting.ini"
# cp = configparser.ConfigParser()
# cp.read(ini_path)
# video_dir = cp.get("dir","video_dir")
# audio_dir = cp.get("dir","audio_dir")
from storage import count_by_md5, storage

audio_dir = "E:/docker_data/files/audios"


def extract(video_id: str, storage_path: str):

    count = count_by_md5(video_id)
    if count == 0:
        audio_name, audio_extension, audio_path = convert_one(storage_path)
        storage(audio_path, audio_name, audio_extension, video_id)


def convert_one(video) :
    """:param videos: 所有视频的路径列表
       ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
       ffmpeg -i 2018.mp4 -codec copy -bsf: h264_mp4toannexb -f h264 tmp.264
       ffmpeg -i killer.mp4 -an -vcodec copy out.h264
    """
    print('*' * 15 + 'Start to run:')
    # 分离音频的执行命令,{}{}分别为原始视频与输出后保存的路径名
    ffmpeg_cmd = 'ffmpeg -i {} -vn -y -acodec copy {}'
    video_name = os.path.basename(video)
    audio_prefix = video_name.split('.')[0]
    audio_extension = 'aac'
    audio_name = audio_prefix + '.' + audio_extension
    audio_path = os.path.join(audio_dir, audio_name)
    # 最终执行提取音频的指令
    cmd = ffmpeg_cmd.format(video, audio_path)
    os.system(cmd)

    print('Successfully')
    return audio_name, audio_extension, audio_path


def convert_many(videos):
    """:param videos: 所有视频的路径列表
       ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
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

