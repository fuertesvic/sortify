from PIL import Image
from PIL.PngImagePlugin import PngInfo,PngImageFile
import piexif
import os

def write_tag_in_metadata(file, tag):
    """Gets an image file PNG/JPG (need the full path) and adds a tag into metadata"""
    img_format = os.path.splitext(file)[1]
    
    if 'png' in img_format:
        image = Image.open(file)
        
        # Create a PngInfo object to store metadata
        metadata = PngInfo()

        # Add metadata (you can add any key-value pairs you want)
        metadata.add_text("keywords",tag)

        # Save the image with the new metadata
        image.save(file, pnginfo=metadata)

    if 'jpg' in img_format:
        img = Image.open(file)
        
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Try to load EXIF data if available
        exif_data = img.info.get("exif", None)

        # If EXIF data is missing, create a minimal EXIF dictionary with only the Exif section
        if exif_data is None:
            exif_dict = {
                "Exif": {}  # Only add the Exif section
            }
        else:
            exif_dict = piexif.load(exif_data)

        # Add custom data to the UserComment field (tag 0x9286)
        exif_dict['Exif'][piexif.ExifIFD.UserComment] = tag.encode('utf-8')

        # Convert the EXIF data dictionary into a format suitable for writing
        exif_bytes = piexif.dump(exif_dict)

        # Save the image with the new EXIF metadata
        img.save(file, exif=exif_bytes)

# Method for reading metadata
def read_tag_in_metadata(file):
    """Gets an image file PNG/JPG (need the full path) and reads the metadata tags"""
    img_format = os.path.splitext(file)[1]
    
    if 'jpg' in img_format:
        img = Image.open(file)

        # Try to load EXIF data if available
        exif_data = img.info.get("exif", None)

        if exif_data:
            exif_dict = piexif.load(exif_data)

            # Extract the UserComment field (tag 0x9286)
            user_comment = exif_dict.get("Exif", {}).get(piexif.ExifIFD.UserComment, None)

            if user_comment:
                # Decode UserComment from bytes to string (UTF-8)
                return user_comment.decode('utf-8')
            else:
                return "UserComment field not found."
        else:
            return "No EXIF data found."
    
    elif 'png' in img_format:
        # Open the PNG image
        image = Image.open(file)

    # Read the metadata from the PNG image
    if isinstance(image, PngImageFile):
        metadata = image.text  # Get the metadata dictionary
        keywords = metadata.get('keywords', None)
        
        if keywords:
            return keywords
        else:
            return "No 'keywords' metadata found."

# write_tag_in_metadata('assets/pokemon/1.png','mylittletest')
# print(read_tag_from_metadata('assets/pokemon/1.png'))
