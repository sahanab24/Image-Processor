from PIL import Image,ImageOps

class RotateDegrees:

    def __init__(self, image):
        self.image = image

    def rotateDegrees(cls, image,degrees):
        return image.rotate(degrees)