import pyqrcode

val = 'Akash'
qr = pyqrcode.create(val)
qr.png('a.png' , scale=8)

val = 'Sumit'
qr = pyqrcode.create(val)
qr.png('b.png' , scale=8)

val = 'Lakshay'
qr = pyqrcode.create(val)
qr.png('c.png' , scale=8)

val = 'Ravi'
qr = pyqrcode.create(val)
qr.png('d.png',scale=8)