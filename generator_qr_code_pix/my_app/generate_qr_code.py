from pixqrcode import PixQrCode


class GenerateQRCode:
    def __init__(self, name: str, key: str, value_pix: str) -> None:
        self.name = name
        self.key = key
        self.value_pix = value_pix

    def generate(self) -> None:
        pix = PixQrCode(name=self.name, key=self.key, 
                        city='Porto Alegre', amount=self.value_pix)
        
        img_base64 = pix.export_base64()
        print(type(img_base64))           # Deve ser str
        print(img_base64[:100])           # Mostrar os primeiros caracteres

        return img_base64
       # return pix.export_base64()
