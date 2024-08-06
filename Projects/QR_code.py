import qrcode as qr
img = qr.make("https://unsplash.com")
img.save("unsplash_qr.png")