from PIL import Image, ImageDraw, ImageFont

# TODO 0: Import library lain yang dibutuhkan

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open('C:\Users\ferza\OneDrive\Documents\SEMESTER5\PRAKTIKUM PEMROGRAMAN FUNGSIONAL\latModul6\Modul6\Latihan\per1.jpg')

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
direktoriFont = 'C:\Users\ferza\OneDrive\Documents\SEMESTER5\PRAKTIKUM PEMROGRAMAN FUNGSIONAL\latModul6\Modul6\Latihan\fonts/arial.ttf'
font = ImageFont.truetype(direktoriFont, 24)
text = "Ferza Amanda - 202110370311221"
# Use textbbox on the ImageDraw object to get the bounding box
text_bbox = draw.textbbox((0, 0), text, font)

# Extract width and height from the bounding box
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

text_width, text_height = draw.textsize(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill='white')

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save('per1.jpg')

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()