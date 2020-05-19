
import cv2


def capturarImagen():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Webcam para Frutas")
    img_counter = 0

    while True:
        ret, frame = cam.read()

        if not ret:
            print("Fallo al  grabar imagen")
            cv2.destroyAllWindows()
            break
        cv2.imshow("Webcam para Frutas", frame)
        k = cv2.waitKey(1)

        if k%256 == 27:
            # Presionar ESC 
            print("Pulsar Escape , cerrando...")
            cv2.destroyAllWindows()
            break
        elif k%256 == 32:
            # Presionar SPACE 
            img_name = "./Input/imagenes/opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    return 