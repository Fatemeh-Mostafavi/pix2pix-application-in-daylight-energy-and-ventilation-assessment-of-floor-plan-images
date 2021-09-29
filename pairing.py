from PIL import Image

# Read the two images
i = 1
for i in range(1, 301):
    image1 = Image.open(f'{i}.jpg')
    # image1.show()
    image2 = Image.open(f'{i}e.jpg')
    # image2.show()
    # resize
    image1 = image1.resize((600, 600))
    image2 = image2.resize((600, 600))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB', (2 * image1_size[0], image1_size[1]), (512, 512, 512))
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (image1_size[0], 0))
    new_image.save(f"maps/ENERGY NEW/{i}.jpg", "JPEG")
    # new_image.show()
