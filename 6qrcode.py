import qrcode 
data = "HTML.py"
qr = qrcode.QRCode(version = 1,box_size = 12,border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'blue',back_color = 'green')
img.save('HTML.png')
import qrcode 
data = "HTML.py"
qr = qrcode.QRCode(version = 1,box_size = 12,border = 5)
qr.add_data(data)
qr.make(fit = True)
