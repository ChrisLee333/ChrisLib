import os
import qrcode
from ChrisLib.helper.getOutputPath import getPath

def genQR(url, filename = "QR.png", stdOutput = True):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    if(stdOutput):
        filename = os.path.join(getPath(), filename)
    
    img.save(filename)
