from PIL import Image,ImageOps

class ThumbNail:

    def __init__(self, image):
        self.image = image

    def thumbNail(cls, image):
        image.thumbnail((200,200))
        return image