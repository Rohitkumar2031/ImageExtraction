# -*- coding: utf-8 -*-
def to_text(path):
    """Wrapper around Poppler pdftotext"""
    import subprocess
    from distutils import spawn  # py2 compat

    if spawn.find_executable("pdftotext"):  # shutil.which('pdftotext'):
        out, err = subprocess.Popen(
            ["pdftotext", "-layout", "-enc", "UTF-8", path, "-"], stdout=subprocess.PIPE
        ).communicate()
        return out
    else:
        raise EnvironmentError(
            "pdftotext not installed. Can be downloaded from https://poppler.freedesktop.org/"
        )

if __name__ == "__main__":
    print(to_text(r"C:\Users\user\Desktop\ImageExtraction\gwbdata_mining\gwbdata_mining\code\bills\hike_gwb.pdf"))
