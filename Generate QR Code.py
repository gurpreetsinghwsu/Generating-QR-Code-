#This is a simple python script to use qr code and can redirect them to any website
import qrcode
img = qrcode.make("https://cybersasecurity.com/")
img.save("Cyberasa security.jpg")