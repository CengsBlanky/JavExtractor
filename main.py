import os
import re

import easyocr


def get_image_files(dir: str) -> list[str]:
    image_extensions = {".jpg", "jpeg", ".png", ".bmp", ".webp"}
    return [
        os.path.join(dir, f)
        for f in os.listdir(dir)
        if os.path.splitext(f)[1].lower() in image_extensions
    ]


def readTexts(image: str):
    reader: easyocr.Reader = easyocr.Reader(["en"])
    return reader.readtext(
        image,
        detail=0,
    )


image_dir = "./pictures/"
codeSet: set[str] = set()
pattern = re.compile("[a-zA-Z]{1,}[- ]{0,}[0-9]{1,}")

for image in get_image_files(image_dir):
    for text in readTexts(image):
        match = pattern.search(str(text))
        if match:
            codeSet.add(match.group())

print("match code is", codeSet)

with open("codelist.txt", "w") as file:
    for code in codeSet:
        file.write(code)
        file.write("\n")

print("code write to codelist.txt done!")
