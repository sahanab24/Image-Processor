from PIL import Image,ImageOps

class FlipHorizontal:

	def __init__(self, image):
		self.image = image
		
	def flipHorizontal(self, image):
		return image.transpose(Image.FLIP_TOP_BOTTOM)


