import argparse
import tempfile
from src.images_process import add_watermark_to_images

from src.pdf_process import convert_pdf_images

colors = {"green": [0, 255, 0], "red": [255, 0, 0], "blue": [0, 0, 255]}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_file")
    parser.add_argument("--text")
    parser.add_argument("--quality", default=10)
    parser.add_argument("--transparency", default=0.25)
    parser.add_argument("--color", default="green")

    args = parser.parse_args()
    input_file = tempfile.TemporaryDirectory()
    color_tuple = tuple(colors[args.color]+[int(255*args.transparency)])
    convert_pdf_images(args.pdf_file, output_directory=input_file.name)
    images_watermarked = add_watermark_to_images(
        input_dir=input_file.name, text=args.text, color=color_tuple)
    

    pdf_path = args.pdf_file.split(".pdf")[0] + "_watermark.pdf"
    images_watermarked[0].save(
        pdf_path,
        "PDF",
        resolution=100.0,
        save_all=True,
        optimize=True,
        quality=args.quality,
        append_images=images_watermarked[1:],
    )
    # , append_images=images_watermarked[1:]
    print(f"PDF {args.pdf_file} successfully watermarked and saved as {pdf_path}")
    input_file.cleanup()
