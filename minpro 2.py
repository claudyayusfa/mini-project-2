"""
Nama        :Claudya Yusfa Ariyani
NIM         :2509116043
MinPro 2
"""

users = {
    "Manager": {"password": "135", "role": "Manager"},
    "Karyawan": {"password": "246", "role": "Karyawan"}
}

kursi_kosong = ["A1", "A2", "A3", "B1", "B2", "B3"]
reservasi_kursi = {}

def create_reservasi():
    try:
        print("Kursi Tersedia", kursi_kosong)
        nama = input("Nama Pemesan: ")
        kursi = input("Pilih Kursi: ")

        if kursi in kursi_kosong:
            reservasi_kursi[kursi] = nama
            kursi_kosong.remove(kursi)
            print(f"{nama} berhasil memesan kursi {kursi}!")
        else:
            print("Kursi tidak tersedia")
    except ValueError:
        print("Input tidak valid!")

from prettytable import PrettyTable
def read_reservasi():
    try:
        if reservasi_kursi:
            tabel = PrettyTable()
            tabel.field_names = ["Kursi", "Nama Pemesan"]
            
            for kursi, nama in reservasi_kursi.items():
                tabel.add_row([kursi, nama])
            print(tabel)
        else:
            print("Belum ada reservasi")
    except ValueError:
        print("Error menampilkan reservasi")

def update_reservasi():
    try:
        read_reservasi()
        kursi_lama = input("Masukkan kursi lama: ")
        
        if kursi_lama in reservasi_kursi:
            kursi_baru = input("Pilih kursi baru: ")
            if kursi_baru in kursi_kosong:
                nama = reservasi_kursi.pop(kursi_lama)
                reservasi_kursi[kursi_baru] = nama
                kursi_kosong.append(kursi_lama)
                kursi_kosong.remove(kursi_baru)
                print(f"Kursi {kursi_lama} diganti ke {kursi_baru}")
            else:
                print("Kursi baru tidak tersedia!")
        else:
            print("Kursi lama tidak ditemukan!")
    except ValueError:
        print("Input tidak valid!")

def delete_reservasi():
    try:
        read_reservasi()
        kursi = input("Masukkan kursi: ")

        if kursi in reservasi_kursi:
            nama = reservasi_kursi.pop(kursi)
            kursi_kosong.append(kursi)
            print(f"Reservasi {kursi} milik {nama} dihapus!")
        else:
            print("Kursi tidak ada")
    except ValueError:
        print("Input tidak valid!")

def menu_manager():
    while True:
        tabel = PrettyTable()
        tabel.field_names = ["No.", "Menu Manager"]
        tabel.add_row(["1.", "Membuat Reservasi Kursi"])
        tabel.add_row(["2.", "Melihat Reservasi Kursi"])
        tabel.add_row(["3.", "Mengubah Rereservasi Kursi"])
        tabel.add_row(["4.", "Menghapus Reservasi Kursi"])
        tabel.add_row(["5.", "keluar"])
        print(tabel)

        pilihan = input("Pilih menu (1-5): ")
        if pilihan == "1":
            create_reservasi()
        elif pilihan == "2":
            read_reservasi()
        elif pilihan == "3":
            update_reservasi()
        elif pilihan == "4":
            delete_reservasi()
        elif pilihan == "5":
            print("Logout sebagai Manager.")
            break
        else:
            print("Menu tidak tersedia!")

def menu_karyawan():
    while True:
        tabel = PrettyTable()
        tabel.field_names = ["No.", "Menu Karyawan"]
        tabel.add_row(["1.", "Membuat Reservasi Kursi"])
        tabel.add_row(["2.", "Melihat Reservasi Kursi"])
        tabel.add_row(["3.", "Keluar"])
        print(tabel)

        pilihan = input("Pilih menu (1-3): ")
        if pilihan == "1":
            create_reservasi()
        elif pilihan == "2":
            read_reservasi()
        elif pilihan == "3":
            print("Logout sebagai karyawan")
            break
        else:
            print("Menu tidak tersedia.")

from getpass import getpass
def login():
    print("\n ────୨ৎ──── LOGIN RESERVASI KURSI BIOSKOP ────୨ৎ────")
    username = input("Username: ")
    password = getpass("Password: ")

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        print(f"Login sebagai {role}")
        if role == "Manager":
            menu_manager()
        elif role == "Karyawan":
            menu_karyawan()
    else:
        print("Username atau password tidak benar!")

while True:
    login()
    ulang = input("Ingin login ulang? (Y/N): ")
    if ulang == "N":
        print("Program selesai.")
        break
