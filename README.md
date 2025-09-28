# Mini Project 2

# Sistem Reservasi Kursi Bioskop˙✧˖°🍿 ༘ ⋆｡˚
**Nama:** Claudya Yusfa Ariyani  
**NIM:** 2509116043  

# Deskripsi
Fitur utama:
- Login dengan role Manager dan Karyawan.  
- Manager dapat melakukan CRUD (Create, Read, Update, Delete) reservasi.  
- Karyawan hanya dapat membuat dan melihat reservasi.  

# Flowchart
  <img width="2551" height="2200" alt="MinPro 2 drawio" src="https://github.com/user-attachments/assets/e271aa9a-1f20-4ee4-9f3d-73dc1513cfc7" />

# Dokumentasi Screenshot Output

## 1. Login Berhasil
- **Manager**
<img width="2223" height="515" alt="image" src="https://github.com/user-attachments/assets/3d85877f-06f4-4fb3-91ec-a89753cd8ebe" />
Penjelasan: Masukkan Username "Manager" dan Password "135". Huruf kapital, huruf kecil, dan angka diperhatikan dengan benar  agar bisa login sebagai Manager

- **Karyawan**
<img width="2181" height="423" alt="image" src="https://github.com/user-attachments/assets/bcde1d20-ad6f-42cd-a00d-d6d46f99885d" />
Penjelasan: Masukkan Username "Karyawan" dan Password "246". Huruf kapital, huruf kecil, dan angka diperhatikan dengan benar agar bisa login sebagai Karyawan

## 2. Create Reservasi
- **Manager**
<img width="2182" height="620" alt="image" src="https://github.com/user-attachments/assets/4d02af15-f26a-4750-aa52-64a9bc1f5f10" />
Saat pilih Menu, pilih Menu No. 1 yaitu Membuat Reservasi Kursi. Lalu akan menampilkan kursi yang tersedia. Setelah itu, masukkan nama pemesan dan pilih kursi yang tersedia. Dan pemesan berhasil memesan kursi yang tersedia

- **Karyawan**
<img width="2221" height="416" alt="image" src="https://github.com/user-attachments/assets/21ecbb2a-59ab-4fa1-9583-fc45a1290927" />
Saat pilih Menu, pilih Menu No. 1 yaitu Membuat Reservasi Kursi. Lalu akan menampilkan kursi yang tersedia. Setelah itu, masukkan nama pemesan dan pilih kursi yang tersedia. Dan pemesan berhasil memesan kursi yang tersedia


## 3. Read Reservasi
- **Manager**
<img width="2201" height="514" alt="image" src="https://github.com/user-attachments/assets/01de1fa0-38d2-4de7-bd70-7c625c3dd577" />
Pilih Menu 2, yaitu Melihat Reservasi Kursi. Lalu akan ditampilkan Kursi dan Nama Pemesan di dalam tabel

- **Karyawan**
<img width="2211" height="440" alt="image" src="https://github.com/user-attachments/assets/6cb85f7d-e739-4c8e-99fa-4ccd0f2405af" />
Pilih Menu 2, yaitu Melihat Reservasi Kursi. Lalu akan ditampilkan Kursi dan Nama Pemesan di dalam tabel

## 4. Update Reservasi
- **Manager**
<img width="2182" height="623" alt="image" src="https://github.com/user-attachments/assets/1e34f1a7-e8a6-44e5-bc04-eb1602ce536e" />
Pilih Menu 3, yaitu Mengubah Reservasi Kursi. Lalu akan menampilkan Tabel berisi Kursi dan Nama Pemesan. Masukkan kursi lama yang sebelumnya dipesan, lalu pilih kursi baru yang tersedia. Lalu kursi lama diganti ke kursi baru

## 5. Delete Reservasi
- **Manager**
<img width="2208" height="586" alt="image" src="https://github.com/user-attachments/assets/da05378a-089a-47da-94cf-da3feaad2bf4" />
Pilih Menu 4, yaitu Menghapus Reservasi Kursi. Lalu akan muncul Tabel berisi Kursi dan Nama Pemesan. Masukkan kursi yang di dalam Tabel, lalu reservasi milik pemesan berhasil dihapus


## 6. Keluar Program
- **Manager**
<img width="2220" height="514" alt="image" src="https://github.com/user-attachments/assets/d17f83b5-07e8-446f-8247-4d92c05b8a99" />
Pilih Menu 5, yaitu Keluar. Lalu akan Logout sebagai Manager. Jika ingin Login ulang, klik "Y" dan program akan menampilkan Login Username dan Password. Jika tidak ingin Login kembali, klik "N" dan program telah selesai

- **Karyawan**
<img width="2228" height="453" alt="image" src="https://github.com/user-attachments/assets/c9a07f01-09b9-49bb-9216-a87a2aa2f551" />
Pilih Menu 5, yaitu Keluar. Lalu akan Logout sebagai Karyawan. Jika ingin Login ulang, klik "Y" dan program akan menampilkan Login Username dan Password. Jika tidak ingin Login kembali, klik "N" dan program telah selesai

## 7. Error Handling
- Kursi Tidak Ada
  <img width="2204" height="414" alt="image" src="https://github.com/user-attachments/assets/463cbe74-7281-4999-a674-5df64094eb4d" />
  Saat di Menu Manager atau Karyawan, pilih Menu 1. Membuat Reservasi Kursi. Setelah itu, input Nama Pemesan dan Pilih Kursi yang tidak tersedia di program. Lalu akan muncul teks "Kursi tidak tersedia" dan program akan menampilkan Menu Manager atau Karyawan lagi

- Login Salah
  <img width="2156" height="207" alt="image" src="https://github.com/user-attachments/assets/84942498-81d4-4e9d-911d-14ead5a13c37" />
  Saat di Menu Login, jika salah masukkan Username atau Password, program akan menampilkan teks "Username atau password tidak benar!" dan program akan bertanya "Apakah Ingin Login Ulang?." Jika klik "Y", program akan menampilkan Menu Login. Jika klik "N", program telah selesai

- Menu Tidak Tersedia
  <img width="2191" height="869" alt="image" src="https://github.com/user-attachments/assets/fe57acf0-891c-4495-ad93-6b29932c4f3f" />
  Saat memilih Menu Manager atau Menu Karyawan, jika kita mengetik angka Menu yang tidak ada di program, program akan menampilkan teks "Menu tidak tersedia!" dan program akan kembali menampilkan Menu yang tersedia

  



