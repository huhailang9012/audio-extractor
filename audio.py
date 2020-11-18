
class Audio(object):

    def __init__(self, id: str, name: str, md5: str, video_id: str, local_audio_path: str,
                 format: str, date_created: str):
        self.id = id
        self.name = name
        self.md5 = md5
        self.video_id = video_id
        self.local_audio_path = local_audio_path
        self.format = format
        self.date_created = date_created