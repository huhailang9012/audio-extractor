import os
import os.path
from repository import select_by_md5, storage
import hashlib


audio_dir = "/data/files/audios/"


def extract(video_id: str, local_video_path: str):
    audio_name, audio_extension, local_audio_path = convert_one(local_video_path)
    with open(local_audio_path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    audio = select_by_md5(file_md5)
    if audio is None:
        audio_id = storage(local_audio_path, audio_name, audio_extension, video_id)
        return audio_id, local_audio_path
    else:
        return audio.id, audio.local_audio_path


def convert_one(video) :
    """:param video
       ffmpeg -i 3.mp4 -vn -y -acodec copy 3.aac
       ffmpeg -i 2018.mp4 -codec copy -bsf: h264_mp4toannexb -f h264 tmp.264
       ffmpeg -i killer.mp4 -an -vcodec copy out.h264
    """
    print('*' * 15 + 'Start to run:')
    ffmpeg_cmd = 'ffmpeg -i {} -vn -y -acodec copy {}'
    video_name = os.path.basename(video)
    audio_prefix = video_name.split('.')[0]
    audio_extension = 'aac'
    audio_name = audio_prefix + '.' + audio_extension
    audio_path = os.path.join(audio_dir, audio_name)
    cmd = ffmpeg_cmd.format(video, audio_path)
    os.system(cmd)

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


if __name__ == '__main__':
    print(extract('8b14b14b2599a5ddf04a4cfecbf850dc', 'E:/docker_data/files/videos/7b14b14b2599a5ddf04a4cfecbf850dc.mp4'))