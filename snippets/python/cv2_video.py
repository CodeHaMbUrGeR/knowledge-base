import cv2


def video():
    # cam config
    width = 1280
    height = 720
    video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    video.set(cv2.CAP_PROP_FPS, 30)
    video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

    while True:
        ret, frame = video.read()
        cv2.imshow('my WEBcam', frame)
        # cv2.moveWindow('my WEBcam', 0, 0)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    video.release()
