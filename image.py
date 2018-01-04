from PIL import Image

def generate_bitmap_from_array(arr, x, y):
	image = Image.new('1', (x, y))
	pixel_map = image.load()
	for i in range(x * y):
		pixel_map[int(i / x), i % y] = arr[i]
	return image

def display_and_save(image, name="result.bmp"):
	image.show()
	image.save(name)