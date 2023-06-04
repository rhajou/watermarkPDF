from pdf2image import convert_from_path


def convert_pdf_images(pdf_path:str, output_directory:str):
    # Convert PDF pages to PIL images
    images = convert_from_path(pdf_path)

    # Iterate over each image
    for i, image in enumerate(images):
        # Save the image in the desired format (e.g., JPEG)
        image_path = f"{output_directory}image_{i}.jpg"
        image.save(image_path, "JPEG")
        print(f"Image {image_path} saved.")
