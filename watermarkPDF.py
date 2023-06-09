import argparse
import tempfile
from src.images_process import add_watermark_to_images
from glob import glob
from src.pdf_process import convert_pdf_images
import os

colors = {"green": [0, 255, 0], "red": [255, 0, 0], "blue": [0, 0, 255]}

def convert_one_pdf(pdf_file, text, transparency, quality, color,output_path=None ):
    input_file = tempfile.TemporaryDirectory()
    color_tuple = tuple(colors[color]+[int(255*transparency)])
    
    convert_pdf_images(pdf_file, output_directory=input_file.name)
    images_watermarked = add_watermark_to_images(
    input_dir=input_file.name, text=text, color=color_tuple)

    if output_path:
        pdf_path = output_path+"/" + pdf_file.split("/")[-1]
    else:
        pdf_path = pdf_file.split(".pdf")[0] + "_watermark.pdf"
    images_watermarked[0].save(
        pdf_path,
        "PDF",
        resolution=100.0,
        save_all=True,
        optimize=True,
        quality=quality,
        append_images=images_watermarked[1:],
    )
    print(f"PDF {pdf_file} successfully watermarked and saved as {pdf_path}")
    input_file.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_file")
    parser.add_argument("--pdf_folder")
    parser.add_argument("--text")
    parser.add_argument("--quality", default=20)
    parser.add_argument("--transparency", default=0.25)
    parser.add_argument("--color", default="red")
    parser.add_argument("--output_folder")
    
    
    args = parser.parse_args()
    pdf_folder = args.pdf_folder
    output_folder = args.output_folder
    if args.pdf_file:
        convert_one_pdf(args.pdf_file, args.text,  args.transparency, int(args.quality), args.color, args.output_folder )
        
    if args.pdf_folder:
        pdf_files = glob(pdf_folder+ "/*.pdf")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        for pdf_file in pdf_files:
            convert_one_pdf(pdf_file, args.text,  args.transparency, int(args.quality), args.color, output_folder )