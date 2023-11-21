import cv2
import datetime
import time

# 設定連結
video_url = "https://cctv.bote.gov.taipei:8501/MJPEG/157?t=0.4947345277427502"

recording_duration = 15 * 60  # 15分鐘

wait_time = 44 * 60

# 設定影片存儲資料夾
output_folder = "D:\\Project\\Road Motorcycle Helmet Detection\\Test\\videos"

while True:

    current_time = datetime.datetime.now()
    
    if current_time.minute == 0 and current_time.second == 0:
        current_date = current_time.strftime("%Y_%m_%d")
        current_time_str = current_time.strftime("%H_%M_%S")

        # 獲取當前日期和時間
        # 設定影片檔名
        video_filename = f"{current_date}_{current_time_str}.mp4"

        # 設定影片儲存路徑
        output_path = f"{output_folder}/{video_filename}"

        # 創建VideoCapture對象
        cap = cv2.VideoCapture(video_url)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # 創建VideoWriter對象
        fourcc = cv2.VideoWriter_fourcc(*'MTPG')
        out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))
        print("Start recording...")
        # 開始錄製
        start_time = time.time()
        while time.time() - start_time < recording_duration:
            ret, frame = cap.read()
            if not ret:
                print('Cannot receive frame')
                break
            out.write(frame)
            cv2.imshow("Recording", frame)  # 顯示當前捕獲的幀
            if cv2.waitKey(1) & 0XFF == ord(' '): # 等待1毫秒
                break
            
        # 釋放資源
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
        print('Finish recording...' + video_filename)
        time.sleep(wait_time)