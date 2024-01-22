import qrcode
from PIL import Image
urls = [
    "https://www.linkedin.com/in/dipro-paul/",
    "https://github.com/DIP-RO"
]
combined_url = '\n'.join(urls)
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
qr.add_data(combined_url)
qr.make(fit=True)
image = qr.make_image(fill_color="blue", back_color="white")
image.save("Dipro.png")