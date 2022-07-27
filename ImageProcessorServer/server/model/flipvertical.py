from PIL import Image,ImageOps

class FlipVertical:

	def __init__(self, image):
		self.image = image

	def flipVertical(cls, image):
		return image.transpose(Image.FLIP_LEFT_RIGHT)