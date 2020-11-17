import psycopg2
from datetime import datetime
import uuid
import hashlib


def insert(self, id: str, name: str, format: str, md5: str, local_audio_path: str,
           video_id: str, date_created: str):
    """
    insert into videos
    :return:
    """
    # connect
    conn = psycopg2.connect(database="video_spider", user="postgres", password="123456", host="127.0.0.1",
                            port="5432")
    # cursor
    cursor = conn.cursor()
    sql = """INSERT INTO audios (id, name, format, md5, local_audio_path, video_id, date_created) 
             VALUES
             (%(id)s, %(name)s, %(format)s, %(md5)s, %(local_audio_path)s, %(video_id)s, %(date_created)s)"""
    params = {'id': id, 'name': name, 'format': format, 'md5': md5, 'local_audio_path': local_audio_path,
              'video_id': video_id, 'date_created': date_created}
    # 执行语句
    cursor.execute(sql, params)
    print("successfully")
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    conn.close()


def count_by_md5(video_id: str) -> int:
    """
    select count(*) from audios
    :return: record size
    """
    # connect
    conn = psycopg2.connect(database="audio_extracting", user="postgres", password="123456", host="127.0.0.1", port="5432")
    # cursor
    cursor = conn.cursor()
    # sql语句 建表
    sql = """SELECT COUNT(*) FROM audios where video_id = %s;"""
    params = (video_id,)
    # 执行语句
    cursor.execute(sql, params)
    # 抓取
    row = cursor.fetchone()
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    cursor.close()
    conn.close()
    return row[0]


def select_by_ids(audio_ids: list):
    """
    select count(*) from audios
    :return: record size
    """
    # connect
    conn = psycopg2.connect(database="audio_extracting", user="postgres", password="123456", host="127.0.0.1", port="5432")
    # cursor
    cursor = conn.cursor()
    # sql语句 建表
    sql = """SELECT * FROM audios where audio_id in %s;"""
    params = (audio_ids,)
    # 执行语句
    cursor.execute(sql, params)
    # 抓取
    row = cursor.fetchall()
    # 事物提交
    conn.commit()
    # 关闭数据库连接
    cursor.close()
    conn.close()
    return row[0]


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
    return file_md5