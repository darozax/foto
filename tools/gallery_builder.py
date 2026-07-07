import os
import json
from PIL import Image, ImageOps

SOURCE = "NOWE"
FULL = "images/full"
THUMBS = "images/thumbs"

THUMB_SIZE = (400, 400)

EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
)


def create_folders():
    os.makedirs(FULL, exist_ok=True)
    os.makedirs(THUMBS, exist_ok=True)


def load_gallery():
    if os.path.exists("gallery.json"):
        with open("gallery.json", "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save_gallery(data):
    with open("gallery.json", "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=2,
            ensure_ascii=False
        )


def process_images():

    gallery = load_gallery()

    existing = {
        item["file"]
        for item in gallery
    }

    added = 0

    for filename in os.listdir(SOURCE):

        if not filename.lower().endswith(EXTENSIONS):
            continue

        if filename in existing:
            continue


        source_file = os.path.join(
            SOURCE,
            filename
        )

        full_file = os.path.join(
            FULL,
            filename
        )

        thumb_file = os.path.join(
            THUMBS,
            os.path.splitext(filename)[0] + ".webp"
        )


        print("Dodaję:", filename)


        with Image.open(source_file) as img:

            img = ImageOps.exif_transpose(img)

            img.save(
                full_file,
                quality=95
            )


            thumb = img.copy()

            thumb.thumbnail(
                THUMB_SIZE
            )

            thumb.save(
                thumb_file,
                "WEBP",
                quality=85
            )


            gallery.append(
                {
                    "file": filename,
                    "thumb": os.path.basename(thumb_file),
                    "title": os.path.splitext(filename)[0]
                }
            )

            added += 1


    save_gallery(gallery)

    print()
    print("======================")
    print("Gotowe!")
    print("Dodano zdjęć:", added)
    print("======================")


if __name__ == "__main__":

    create_folders()
    process_images()
