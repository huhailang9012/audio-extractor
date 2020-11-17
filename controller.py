from fastapi import FastAPI
import extractor as ex


app = FastAPI()


@app.post("/audio/extract")
def audio_extract(video_id: str, local_video_path: str):
    ex.extract(video_id, local_video_path)
    return {"success": True, "code": 0, "msg": "ok"}


# @app.post("/audio/batch")
# def audio_extract(audio_ids: list):
#     ex.extract(file_md5, storage_path)
#     return {"success": True, "code": 0, "msg": "ok"}