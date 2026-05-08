from PIL import Image
import numpy as np

# --------------------------------------------
# Image Preprocessing Function
# --------------------------------------------
def preprocess_image(uploaded_file):

    # Open uploaded file
    image = Image.open(uploaded_file)

    # Convert to grayscale
    image = image.convert("L")

    # Resize image
    image = image.resize((28, 28))

    # Convert to numpy array
    image_array = np.array(image)

    # Normalize
    image_array = image_array / 255.0

    # Reshape for CNN
    image_array = image_array.reshape(
        1,
        28,
        28,
        1
    )

    return image_array