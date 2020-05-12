
from page_object import Ecommerce

def main():

	url = """https://articulo.mercadolibre.com.ve/MLV-472349148-case-externo-25-disco-duro-sata-laptop-usb-30-portatil-alu-_JM?quantity=1#reco_item_pos=1&reco_backend=l7-l7-pp-ngrams-seller-dummy&reco_backend_type=low_level&reco_client=vip-seller_items-above&reco_id=e555f2f4-3e92-44d4-a577-de1c376331e1"""

	mercado_libre = Ecommerce("mercadolibre",url)
	
	print("\nProduct:",mercado_libre.name)

	print("Price:",mercado_libre.price)
	print("Image:",mercado_libre.image)

	url_2 = """https://articulo.mercadolibre.com.ve/MLV-545569914-laptop-acer-intel-i5-39ghz-8gb-512gb-ssd-nvidia-2gb-video-_JM?quantity=1&variation=45958098574"""

	mercado_libre2 = Ecommerce("mercadolibre",url_2)
	
	print("\nProduct:",mercado_libre2.name)

	print("Price:",mercado_libre2.price)
	print("Image:",mercado_libre2.image)



if __name__ == '__main__':
	main()