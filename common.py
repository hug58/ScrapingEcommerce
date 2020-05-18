

import json

_config = None

def config():

	with open("ecommerce.json") as f:
		_config = json.load(f)
	return _config