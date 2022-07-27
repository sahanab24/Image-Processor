from PIL import Image



class RotateRight:

	def __init__(self,image):
		self.image = image

	def rotateRight(cls,image):
		return image.transpose(Image.ROTATE_90)