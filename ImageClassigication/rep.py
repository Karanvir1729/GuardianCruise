import base64


def jpg_to_data_uri(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        image_binary = image_file.read()

        # Encode the image data as base64
        base64_encoded_image = base64.b64encode(image_binary).decode('utf-8')

        # Construct the data URI
        data_uri = f"data:image/jpeg;base64,{base64_encoded_image}"

    return data_uri


# Example usage:
#image_path = "download (2).jpg"  # Replace with the path to your JPG image
#data_uri = jpg_to_data_uri(image_path)
#print("Data URI:", data_uri)