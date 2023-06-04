from PIL import Image, ImageDraw, ImageFont, ImageOps

import math
from glob import glob
from typing import List, Tuple

def add_watermark_to_images(input_dir:str, text:str, color:Tuple[str])-> List[Image.Image]:
    images_path = glob(input_dir + "*.jpg")
    images_path.sort()
    images_watermarked = []
    for image_path in images_path:
        image = add_watermark_to_image(image_path, text, color)
        images_watermarked.append(image)
    return images_watermarked


def add_watermark_to_image(image_path:str, text:str, color:Tuple[str]=(255, 255, 255, 128))-> Image.Image:
    # Open the image
    image = Image.open(image_path).convert("RGBA")

    # # Create a transparent layer for the watermark
    # watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Calculate the font size based on the image resolution
    font_size = int(image.width / 2)  # Adjust this factor to control the font size

    # Set the font and size for the watermark text
    font = ImageFont.truetype("Arial.ttf", font_size)

    # Calculate the size of the watermark text
    text_width, text_height = font.getsize(text)

    # Calculate the diagonal length of the watermark
    diagonal_length = math.ceil(math.sqrt(text_width**2 + text_height**2))

    # Create a blank diagonal image with the calculated length
    diagonal_image = Image.new("RGBA", (diagonal_length, diagonal_length), (0, 0, 0, 0))

    # Paste the watermark text on the diagonal image
    draw = ImageDraw.Draw(diagonal_image)
    diagonal_position = ((diagonal_length - text_width) // 2, (diagonal_length - text_height) // 2)
    draw.text(diagonal_position, text, font=font, fill=color)

    # Rotate the diagonal image
    rotation_angle = 30
    rotated_diagonal = diagonal_image.rotate(rotation_angle, expand=True)

    # Calculate the position to paste the rotated watermark
    # paste_position = (
    #     (image.width - rotated_diagonal.width) // 2,
    #     (image.height - rotated_diagonal.height) // 2,
    # )

    # Composite the original image with the rotated watermark
    watermarked_image = Image.alpha_composite(image, ImageOps.fit(rotated_diagonal, image.size))

    # Save the watermarked image to the output path
    background = Image.new("RGB", watermarked_image.size, (255, 255, 255))

    background.paste(
        watermarked_image, mask=watermarked_image.split()[3]
    )  # 3 is the alpha channel
    return background
