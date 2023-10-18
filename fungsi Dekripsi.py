import tkinter as tk

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        shifted_char = (ord(char) - shift) % 256
        plaintext += chr(shifted_char)
    return plaintext

def decrypt_button_clicked():
    ciphertext = input_text.get("1.0", "end-1c")  # Dapatkan ciphertext dari input
    shift = int(shift_entry.get())
    plaintext = caesar_cipher_decrypt(ciphertext, shift)
    output_text.delete("1.0", "end")  # Hapus teks sebelumnya dari output
    output_text.insert("1.0", plaintext)  # Tampilkan plaintext di kotak hasil

# Buat GUI
window = tk.Tk()
window.title("Aplikasi Dekripsi Caesar Cipher")

input_label = tk.Label(window, text="Masukkan Ciphertext:")
input_label.pack()

input_text = tk.Text(window, height=5, width=40)
input_text.pack()

shift_label = tk.Label(window, text="Jumlah Geser:")
shift_label.pack()

shift_entry = tk.Entry(window)
shift_entry.pack()

decrypt_button = tk.Button(window, text="Dekripsi", command=decrypt_button_clicked)
decrypt_button.pack()

output_label = tk.Label(window, text="Hasil Dekripsi:")
output_label.pack()

output_text = tk.Text(window, height=5, width=40)
output_text.pack()

window.mainloop()