from PIL import Image,ImageOps

class GrayScale:

    def __init__(self, image):
        self.image = image

    def grayScale(cls, image):
        return ImageOps.grayscale(image)