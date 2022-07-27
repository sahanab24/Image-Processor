from PIL import Image,ImageOps

from model.rotatel import RotateLeft
from model.rotater import RotateRight
from model.fliphorizontal import FlipHorizontal
from model.flipvertical import FlipVertical
from model.grayscale import GrayScale
from model.thumbnail import ThumbNail
from model.resizewidthheight import ResizeWidthHeight
from model.rotatedegrees import RotateDegrees
from flask import Flask, request, redirect, jsonify

class ImageTransformationFactoryDecider:

    def __init__(self, image, transformation):
        self.image = image
        self.transformation = transformation

    def applyTransformation(cls, image, transformation):

        if transformation == "rotateLeft":
            classObject = RotateLeft(image)
            return classObject.rotateLeft(image)

        elif transformation == "rotateRight":
            classObject = RotateRight(image)
            return classObject.rotateRight(image)

        elif  transformation == "flipHorizontal":
            classObject = FlipHorizontal(image)
            return classObject.flipHorizontal(image)

        elif transformation == "flipVertical":
            classObject = FlipVertical(image)
            return classObject.flipVertical(image)

        elif transformation == "grayScale":
            classObject = GrayScale(image)
            return classObject.grayScale(image)

        elif transformation == "thumbNail":
            classObject = ThumbNail(image)
            return classObject.thumbNail(image)

        elif "resizeWidthHeight" in transformation:

            size = transformation.split("_")

            try:
                int(size[1])
                int(size[2])
            except ValueError:
                raise ValueError("Please provide the integer values for resizeWidthHeight")

            if int(size[1]) > 3000 or int(size[2]) > 3000 or int(size[1]) < 10 or int(size[2]) < 10:
                raise ValueError("The resizeWidthHeight value should be in the range of 3000x3000 and 10x10")

            size = transformation.split("_")
            classObject = ResizeWidthHeight(image)
            return classObject.resizeWidthHeight(image,int(size[1]),int(size[2]))

        elif "rotateDegrees" in transformation :
            try:
                int(transformation.split("_")[1])
            except ValueError:
                raise ValueError("Please provide the integer value for rotateDegrees")

            degree = int(transformation.split("_")[1])
            classObject = RotateDegrees(image)
            return classObject.rotateDegrees(image,degree)
        else:
            raise ValueError("The transformation list is invalid")



