from PIL import Image



class RotateLeft:

    def __init__(self, image):
        self.image = image

    def rotateLeft(cls, image):
        degree_flippedImage = image.transpose(Image.ROTATE_270)
        return degree_flippedImage