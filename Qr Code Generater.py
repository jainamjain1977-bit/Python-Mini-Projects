import qrcode
data = input("enter your text or link:");
img = qrcode.make(data);
img.save('qr.png');
img.show();
