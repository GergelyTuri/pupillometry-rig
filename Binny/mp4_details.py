import cv2

def get_mp4_details(video_path, file_type):
  try:
    if file_type == 'new':
      mp4_path = video_path.split('DLC')[0] + '.avi'
      
    else:

      mp4_path = video_path.split('.h5')[0] + '_labeled.mp4'
    
    cap = cv2.VideoCapture(mp4_path)

    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Get the number of frames in the video
    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the duration of the video in seconds
    duration = num_frames / fps
    duration_min = int(duration / 60)
    duration_sec = int(duration % 60)

    # Release the capture object to free up memory
    cap.release()

    return fps, num_frames, duration
  except:
    print('Something went wrong while getting details of mp4.')