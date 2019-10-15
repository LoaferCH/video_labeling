import cv2
import os
import numpy as np 
import time


def play_video(video_dir, video_name):
    options = '1-overcast 2-cloudy 3-partly 4-clear 5-no 6-garbage'
    keys_to_name = {49:'overcast',50:'cloudy',51:'partly_cloudy',52:'clear',53:'no_sky', 54:'garbage'}

    frame_keep = []
    vs = cv2.VideoCapture(video_dir + '\\' + video_name)
    print('Now playing: ' + video_name)

    frame_number = 0

    
    

    while True:
        print(frame_number)      
        frame = vs.read()[1]
        print('Frame read')
        if frame is None:
            cv2.putText(frame_to_show, options, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
            cv2.imshow('Frame', frame_to_show)
            split_key = cv2.waitKey()
            if split_key in keys_to_name.keys():
                for i in range(len(frame_keep)):
                    cv2.imwrite('./saved_images/' + keys_to_name[split_key]+'/'+video_name + str(frame_number)+str(i)+'.jpg', frame_keep[i])
                frame_keep = []
            break

        frame_to_show = cv2.resize(frame, (1280, 720))
        print('Resize done')
        if frame_number % 30:
            frame_keep.append(frame_to_show)
        cv2.imshow('Frame', frame_to_show)
        
        key = cv2.waitKey(10)
        
        if key == 32:
            cv2.putText(frame_to_show, options, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1)
            cv2.imshow('Frame', frame_to_show)
            split_key = cv2.waitKey()
            if split_key in keys_to_name.keys():
                for i in range(len(frame_keep)):
                    cv2.imwrite('./saved_images/' + keys_to_name[split_key]+'/'+video_name + str(frame_number)+str(i)+'.jpg', frame_keep[i])
                frame_keep = []
        
        frame_number+=1
        frame_number+=1
    vs.release()
    cv2.destroyAllWindows()

def main():
    
    video_dir = input('Write path to folder with videos: \n')

    video_file_names = os.listdir(video_dir)
    print('Found this video files: ', video_file_names)
    
    for video in video_file_names:
        play_video(video_dir, video)

if __name__ == "__main__":
    if not os.path.exists('./saved_images/'):
        os.mkdir('./saved_images/')
        os.mkdir('./saved_images/clear/')
        os.mkdir('./saved_images/overcast/')
        os.mkdir('./saved_images/cloudy')
        os.mkdir('./saved_images/partly_cloudy')
        os.mkdir('./saved_images/no_sky')
    main()

