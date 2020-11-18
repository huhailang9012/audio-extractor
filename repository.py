from datetime import datetime
import uuid
import hashlib
from typing import Dict
from database_pool import PostgreSql


def insert(id: str, name: str, format: str, md5: str, local_audio_path: str,
           video_id: str, date_created: str):
    """
    insert into videos
    :return:
    """
    sql = """INSERT INTO audios (id, name, format, md5, local_audio_path, video_id, date_created) 
             VALUES
             (%(id)s, %(name)s, %(format)s, %(md5)s, %(local_audio_path)s, %(video_id)s, %(date_created)s)"""
    params = {'id': id, 'name': name, 'format': format, 'md5': md5, 'local_audio_path': local_audio_path,
              'video_id': video_id, 'date_created': date_created}
    db = PostgreSql()
    db.execute(sql, params)


def select_by_md5(md5: str) -> Dict[str, any]:
    """
    SELECT * FROM audios where md5 = %s;
    :return: audio
    """
    # sql语句 建表
    sql = """SELECT * FROM audios where md5 = %s;"""
    params = (md5,)

    db = PostgreSql()
    audio = db.select_one(sql, params)
    return audio


def select_by_ids(audio_ids: list):
    """
    select count(*) from audios
    :return: record size
    """
    tupVar = tuple(audio_ids)
    # sql语句 建表
    sql = """SELECT * FROM audios where id in %s;"""
    db = PostgreSql()
    result = db.select_by_ids(sql, (tupVar,))
    return result


def storage(local_audio_path: str, name: str, format: str, video_id: str):
    """
    storage videos
    :return:
    """
    id = uuid.uuid1().hex
    with open(local_audio_path, 'rb') as fp:
        data = fp.read()
    file_md5 = hashlib.md5(data).hexdigest()
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    insert(id, name, format, file_md5, local_audio_path, video_id,
           now)
    return id


if __name__ == '__main__':
    audios = list()
    audios.append('8b14b14b2599a5ddf04a4cfecbf850dc')
    audios.append('64efae6ee4b18803b1d29c87a0cab675')
    tupVar = tuple(audios)
    print(select_by_md5('812b492616a209b8855efd9af617855d'))