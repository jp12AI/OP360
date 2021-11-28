#include "/home/user/Desktop/detect_right.py"

def display_result(top_result, frame, labels):
    r"""Display top K result in top right corner"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    size = 0.6
    color = (255, 0, 0)  # Blue color
    thickness = 1

    for idx, (_id, score) in enumerate(top_result):
        # print('{} - {:0.4f}'.format(label, score))
        x = 12
        y = 24 * idx + 24
        cv2.putText(frame, '{} - {:0.4f}'.format(labels[_id], score),
                    (x, y), font, size, color, thickness)

    cv2.imshow('Image Classification', frame)
