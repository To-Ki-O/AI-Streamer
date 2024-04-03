import action
import os
import shutil

if __name__ == "__main__":
    video_path = '../video/StreetFighter6.mp4'
    output_video_path = '../video'
    images_path = '../images'
    voice_path = '../voice'
    cap = action.load_video(video_path)
    action.take_images(cap)

    DIR = '../images'
    images_number = sum(os.path.isfile(os.path.join(DIR, name)) for name in os.listdir(DIR))

    comment = action.send_images(images_path, 0)
    action.create_voice(voice_path, comment, 0)
    action.attach_voice(video_path, voice_path, 0)

    for i in range(1, images_number//20):
        comment = action.send_images(images_path, i)
        action.create_voice(voice_path, comment, i)
        action.attach_voice(f"{output_video_path}/output_video{i-1}.mp4", voice_path, i)

    # refresh the images directory
    shutil.rmtree(images_path)
    os.mkdir(images_path)
    # refresh the voice directory
    shutil.rmtree(voice_path)
    os.mkdir(voice_path)
