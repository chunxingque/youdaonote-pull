import os
import sys
import json
import logging

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(BASE_DIR)

from core.youDaoNoteApi import YoudaoNoteApi

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_local_media_files(directory):
    api = YoudaoNoteApi()
    error_msg = api.login_by_cookies()
    if error_msg:
        logging.error(f"登录失败: {error_msg}")
        return

    count_audio = 0
    count_scan = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file.endswith('.audio') or file.endswith('.scan'):
                try:
                    with open(file_path, 'rb') as f:
                        data = json.load(f)
                    
                    is_audio = file.endswith('.audio')
                    media_folder = os.path.splitext(file_path)[0] + ('_audio' if is_audio else '_scan')
                    
                    if not os.path.exists(media_folder):
                        os.makedirs(media_folder)
                    
                    if is_audio:
                        records = data.get('recordList', [])
                        for i, record in enumerate(records):
                            record_id = record.get('recordID')
                            if record_id:
                                media_resp = api.get_file_by_id(record_id)
                                if media_resp.status_code == 200:
                                    media_path = os.path.join(media_folder, f"{os.path.splitext(file)[0]}_{i+1}.mp3")
                                    with open(media_path, 'wb') as mf:
                                        mf.write(media_resp.content)
                                    logging.info(f"成功导出音频: {media_path}")
                                    count_audio += 1
                                else:
                                    logging.error(f"下载音频失败 {record_id}")
                    else:
                        images = data.get('imageList', [])
                        for i, img in enumerate(images):
                            img_id = img.get('OriginImageName')
                            if img_id:
                                media_resp = api.get_file_by_id(img_id)
                                if media_resp.status_code == 200:
                                    media_path = os.path.join(media_folder, f"{os.path.splitext(file)[0]}_{i+1}.jpg")
                                    with open(media_path, 'wb') as mf:
                                        mf.write(media_resp.content)
                                    logging.info(f"成功导出图片: {media_path}")
                                    count_scan += 1
                                else:
                                    logging.error(f"下载图片失败 {img_id}")
                except Exception as e:
                    logging.error(f"处理文件 {file_path} 时出错: {e}")

    logging.info(f"转换完成！共成功处理 {count_audio} 个音频文件和 {count_scan} 个扫描图片。")

if __name__ == "__main__":
    notes_dir = os.path.join(BASE_DIR, 'youdaonote')
    convert_local_media_files(notes_dir)
