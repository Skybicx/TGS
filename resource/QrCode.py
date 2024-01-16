import qrcode

def Create(data: str):
    image = qrcode.make(data)
    image.save("qrcode.png")