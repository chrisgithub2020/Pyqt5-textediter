from PIL import Image
from io import BytesIO
import base64


def pil_image_to_base64(pil_image):
    """
    Convert a pillow image to a base64 image
    """
    buf = BytesIO()
    with open(pil_image,'rb') as img_file:
        encoded_string = base64.b64encode(img_file.read())
        encoded_string = encoded_string.decode('utf-8')
    return encoded_string


def base64_to_pil_image(base64_img):
    """
    Converts a base64 image to a pillow image
    """
    return Image.open(BytesIO(base64.b64decode(base64_img)))
