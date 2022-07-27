from PIL import Image,ImageOps

class ResizeWidthHeight:

    def __init__(self, image):
        self.image = image

    def resizeWidthHeight(cls, image,width,height):
        return image.resize((width,height))