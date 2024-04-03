from openai import OpenAI
import openai
import base64
import requests
from setting import OPENAI_API_KEY
import cv2
import os
from pathlib import Path
import requests
import json
import pyaudio
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips


client = OpenAI()

prompt = """
あなたはストリートファイター６の様子を実況する実況者です
以下の制約を元に今の様子を実況してください

* [[[ 30文字以内 ]]]で実況してください
* テンション高く実況してください
* 白い道着のキャラクターは『リュウ』と呼んでください
* 青いチャイナ服のキャラクターは『チュンリー』と呼んでください
"""


# the function loading a video
def load_video(video_path):
    cap = cv2.VideoCapture(video_path)
    return cap


# the function taking images each 15 frames from the video
def take_images(cap):
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if count % 15 == 0:
                cv2.imwrite(f'../images/frame{count//15}.jpg', frame)
            count += 1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


# the function sending the image to the OpenAI API
def send_images(image_path, count):
    count *= 20
    # encode 5 seconds of video as 20 images
    image_1 = encode_image(f'{image_path}/frame{count}.jpg')
    image_2 = encode_image(f'{image_path}/frame{count+1}.jpg')
    image_3 = encode_image(f'{image_path}/frame{count+2}.jpg')
    image_4 = encode_image(f'{image_path}/frame{count+3}.jpg')
    image_5 = encode_image(f'{image_path}/frame{count+4}.jpg')
    image_6 = encode_image(f'{image_path}/frame{count+5}.jpg')
    image_7 = encode_image(f'{image_path}/frame{count+6}.jpg')
    image_8 = encode_image(f'{image_path}/frame{count+7}.jpg')
    image_9 = encode_image(f'{image_path}/frame{count+8}.jpg')
    image_10 = encode_image(f'{image_path}/frame{count+9}.jpg')
    image_11 = encode_image(f'{image_path}/frame{count+10}.jpg')
    image_12 = encode_image(f'{image_path}/frame{count+11}.jpg')
    image_13 = encode_image(f'{image_path}/frame{count+12}.jpg')
    image_14 = encode_image(f'{image_path}/frame{count+13}.jpg')
    image_15 = encode_image(f'{image_path}/frame{count+14}.jpg')
    image_16 = encode_image(f'{image_path}/frame{count+15}.jpg')
    image_17 = encode_image(f'{image_path}/frame{count+16}.jpg')
    image_18 = encode_image(f'{image_path}/frame{count+17}.jpg')
    image_19 = encode_image(f'{image_path}/frame{count+18}.jpg')
    image_20 = encode_image(f'{image_path}/frame{count+19}.jpg')
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_1}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_2}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_3}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_4}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_5}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_6}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_7}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_8}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_9}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_10}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_11}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_12}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_13}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_14}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_15}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_16}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_17}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_18}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_19}",
                            "detail": "high"
                        },
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_20}",
                            "detail": "high"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content


# the function creating a voice message from the comment by OpenAI API
def create_voice(voice_path, comment, count):
    speech_file_path = f'{voice_path}/speech{count}.mp3'
    response = openai.audio.speech.create(
      model="tts-1",
      voice="echo",
      input=comment
    )
    response.stream_to_file(speech_file_path)


# the function attaching the voice message to the video
def attach_voice(video_path, voice_path, count):
    # 動画ファイルと音声ファイルを読み込む
    video_clip = VideoFileClip(video_path)
    new_audio_clip = AudioFileClip(f"{voice_path}/speech{count}.mp3")

    # 動画の元の音声を取得
    original_audio = video_clip.audio

    # 新しい音声を特定の秒数に合成する
    start_time = count * 5
    end_time = start_time + new_audio_clip.duration
    if end_time > video_clip.duration:
        end_time = video_clip.duration
    elif end_time > start_time + 5:
        end_time = start_time + 5

    # 音声クリップを分割して新しい音声を挿入
    before_new_audio = original_audio.subclip(0, start_time)
    after_new_audio = original_audio.subclip(end_time)

    # 音声クリップを結合
    final_audio = concatenate_audioclips([before_new_audio, new_audio_clip, after_new_audio])

    # 最終的な音声を動画に設定
    video_clip.audio = final_audio

    # 編集した動画をファイルとして出力
    video_clip.write_videofile(f"../video/output_video{count}.mp4")


# encode image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
