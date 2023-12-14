import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# Membaca dan menampilkan gambar
img = mpimg.imread('C:\Kuliah\S V\Pemrograman Web\Portofolio\images\logo.png') #Sesuaikan dengan direktori
plt.imshow(img)
plt.axis('off') # Tidak menampilkan sumbu koordinat
plt.show()
