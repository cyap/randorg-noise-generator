from PIL import Image

def generate_bitmap(x=128, y=128, rand_nums=[1 for i in range(128 * 128)]):
	image = Image.new('1', (x, y))
	pixel_map = image.load()
	for i in range(x * y):
		pixel_map[int(i / x), i % y] = rand_nums[i]
	return image


image = generate_bitmap()
image.show()
image.save("result.bmp")