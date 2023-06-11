import cv2, copy


def draw(path, text = "ОШИБКА"):
    frame = cv2.imread(path)

    right = frame.shape[1]
    text_len = len(text)*70
    print_speed = -1 * int(text_len/90)

    frames = []
    for i in range(right, (right - text_len), print_speed):
        _time = copy.copy(frame)
        frames.append(cv2.putText(_time, text, (i, int(frame.shape[1]/1.3)), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0), 3))

    writer = cv2.VideoWriter(
        'output.mp4',
        cv2.VideoWriter_fourcc(*'mp4v'),  # codec
        30.0,  # fps
        (frame.shape[1], frame.shape[0]),  # width, height
        isColor=len(frame.shape) > 2)
    for frame in frames:
        writer.write(frame)
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    text = input("Какой текст создать: ")
    if text != '':
        draw('img/back100.png', text)
    else:
        draw('img/back100.png')
