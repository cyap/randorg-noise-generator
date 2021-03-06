import image
import request

# Should actually be in a config file
API_KEY = "00000000-0000-0000-0000-000000000000"
LIMIT = 10000


def generate_random_bitmap(x, y):
	n = x * y
	rand_arr = []

	while n > 0:
		requested_numbers = min(LIMIT, n)
		n -= requested_numbers

		params = {
			'apiKey': API_KEY,
			'n': requested_numbers, 
			'min': 0,
			'max': 1,
			'replacement':"true"
		}

		try:
			response = request.make_randorg_request("generateIntegers", params)
			rand_arr.extend(response['result']['random']['data'])
		except:
			raise RuntimeError(response)

	return image.generate_bitmap_from_array(rand_arr, x, y)

def main():
	if request.check_quota() < 0:
		raise RuntimeError("Request quota exceeded")
	bmp = generate_random_bitmap(128, 128)
	image.display_and_save(bmp)

if __name__ == '__main__':
	main()