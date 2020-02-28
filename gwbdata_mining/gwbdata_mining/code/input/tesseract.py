# -*- coding: utf-8 -*-


def to_text(path):
    """Wraps Tesseract OCR"""
    import subprocess
    from distutils import spawn

    import os
    p = os.environ["ProgramFiles"]
    ImageMagick = os.path.join(p + "\ImageMagick-6.9.10-Q8" + "\convert.exe" )

    # Check for dependencies. Needs Tesseract and Imagemagick installed.
    if not spawn.find_executable("tesseract"):
        raise EnvironmentError("tesseract not installed.")
    #if not spawn.find_executable("convert"):
        #raise EnvironmentError("imagemagick not installed.")

    # convert = "convert -density 350 %s -depth 8 tiff:-" % (path)
    convert = [
        ImageMagick,
        "-density",
        "300",
        path,
        "-depth",
        "8",
        "-alpha",
        "off",
        "png:-",
    ]
    p1 = subprocess.Popen(convert, stdout=subprocess.PIPE)

    tess = ["tesseract", "stdin", "stdout"]
    p2 = subprocess.Popen(tess, stdin=p1.stdout, stdout=subprocess.PIPE)

    out, err = p2.communicate()

    extracted_str = out

    return extracted_str
