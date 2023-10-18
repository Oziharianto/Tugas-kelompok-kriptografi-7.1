import tkinter as tk

def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        shifted_char = (ord(char) + shift) % 256
        ciphertext += chr(shifted_char)
    return ciphertext

def encrypt_button_clicked():
    plaintext = input_text.get("1.0", "end-1c")  # Dapatkan teks dari input
    shift = int(shift_entry.get())
    ciphertext = caesar_cipher_encrypt(plaintext, shift)
    output_text.delete("1.0", "end")  # Hapus teks sebelumnya dari output
    output_text.insert("1.0", ciphertext)  # Tampilkan ciphertext di kotak hasil

# Buat GUI
window = tk.Tk()
window.title("Aplikasi Enkripsi Caesar Cipher")

input_label = tk.Label(window, text="Masukkan Teks:")
input_label.pack()

input_text = tk.Text(window, height=5, width=40)
input_text.pack()

shift_label = tk.Label(window, text="Jumlah Geser:")
shift_label.pack()

shift_entry = tk.Entry(window)
shift_entry.pack()

encrypt_button = tk.Button(window, text="Enkripsi", command=encrypt_button_clicked)
encrypt_button.pack()

output_label = tk.Label(window, text="Hasil Enkripsi:")
output_label.pack()

output_text = tk.Text(window, height=5, width=40)
output_text.pack()

window.mainloop()