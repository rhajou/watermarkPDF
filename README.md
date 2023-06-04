# watermarkPDF
## Example: 
![Screenshot](images/pheobe.jpg.png)

![before](https://github.com/rhajou/watermarkPDF/tree/main/images/pheobe.png)

![after](https://github.com/rhajou/watermarkPDF/tree/main/images/pheobe_watermark.png)
## Description
watermarkPDF is a small Python project with the main goal of adding a watermark to your PDF files to provide protection against scams when sending sensitive data. By adding a watermark, such as "Document used for Alex Dupont" or "Use this document for loan with bank XXX," you can deter unauthorized use or replication of your PDF files.

The project uses the `pillow` and `pdf2image` libraries to process the PDF file and add the watermark. Make sure to install these libraries using the following command:

```
pip install pillow==9.2.0 pdf2image==1.16.3
```

Additionally, the project relies on the `poppler` library for PDF processing. Follow the instructions below to install `poppler` on your operating system.

## Installation

### Windows

1. Download the pre-built binaries of `poppler` from the [poppler for Windows](http://blog.alivate.com.au/poppler-windows/) website.
2. Extract the contents of the downloaded zip file.
3. Add the path to the extracted `poppler` folder to the system environment variables. This can be done by following these steps:
   - Right-click on the "Computer" icon on your desktop and select "Properties".
   - Click on "Advanced system settings" on the left-hand side.
   - In the System Properties window, click on the "Environment Variables" button.
   - In the Environment Variables window, under "System variables", scroll down and find the "Path" variable. Select it and click on the "Edit" button.
   - Click on the "New" button and add the path to the extracted `poppler` folder (e.g., `C:\path\to\poppler\bin`). Click "OK" to save the changes.
4. Verify the installation by opening a command prompt and running the following command:

   ```
   pdftoppm -v
   ```

   You should see the version information for `pdftoppm`, which confirms that `poppler` is successfully installed.

### macOS

1. Install `poppler` using [Homebrew](https://brew.sh/), a popular package manager for macOS. Open a terminal and run the following command:

   ```
   brew install poppler
   ```

2. Verify the installation by running the following command:

   ```
   pdftoppm -v
   ```

   You should see the version information for `pdftoppm`, indicating that `poppler` is installed correctly.

### Linux

1. Use your distribution's package manager to install `poppler`. The package name may vary depending on the distribution. Here are a few examples:

   - **Debian/Ubuntu**:

     ```
     sudo apt-get install poppler-utils
     ```

   - **Fedora**:

     ```
     sudo dnf install poppler-utils
     ```

   - **Arch Linux**:

     ```
     sudo pacman -S poppler
     ```

2. Verify the installation by running the following command:

   ```
   pdftoppm -v
   ```

   You should see the version information for `pdftoppm`, indicating that `poppler` is installed correctly.

## Usage

To use the watermarkPDF project, follow these steps:

1. Ensure that you have installed the required libraries and `poppler` as mentioned in the installation instructions.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the following command:

   ```
   python watermarkPDF.py --pdf_file="images/pheobe.pdf" --text="My eyes!"
   ```

   Replace `images/pheobe.pdf` with the filename of your input PDF file and `"My eyes!"` with the desired text for the watermark.

5. After the script executes successfully, you will find the watermarked PDF file in the same directory.

## Acknowledgments
The watermarkPDF project relies on the following open-source libraries:

- [pillow](https://pillow.readthedocs.io/) - A powerful image processing library for Python.
- [pdf2image](https://github.com/Belval/pdf2image) - A Python wrapper for the poppler-utils command-line tools to convert PDF files to images.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it according to your needs.