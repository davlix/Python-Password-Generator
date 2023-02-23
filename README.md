# Python Password Generator
 Python Complex Password Generator

Program ini meminta input dari pengguna untuk panjang password yang diinginkan dan kriteria kompleksitas seperti penggunaan huruf besar, huruf kecil, angka, dan simbol. Program menggunakan fungsi generate_password() untuk menghasilkan password acak yang memenuhi kriteria yang diminta. Fungsi ini memastikan bahwa password memenuhi kriteria kompleksitas dengan menggunakan fungsi is_password_strong(), yang memerik.

FEATURE :

1.Meminta pengguna untuk memilih jenis karakter yang ingin digunakan dalam password, misalnya hanya huruf besar, huruf kecil, atau angka.

2.Memeriksa kekuatan password yang dihasilkan dengan menggunakan library seperti zxcvbn untuk mengukur kompleksitas password berdasarkan kekuatan dan estimasi waktu untuk membobolnya.

3.Menggunakan metode hashing seperti SHA-256 untuk mengenkripsi password dan menjaga keamanan password tersebut.

4.Menambahkan kriteria khusus seperti jumlah huruf besar, jumlah huruf kecil, jumlah angka, dan jumlah simbol yang harus ada dalam password yang dihasilkan.

5.Membatasi pengulangan karakter yang sama dalam password, sehingga password yang dihasilkan lebih acak dan sulit ditebak.

6.Menambahkan opsi untuk menghasilkan multiple password sekaligus dan menyimpannya dalam file teks dengan nama yang ditentukan oleh pengguna.

7.Memperhatikan memori dan waktu eksekusi dengan menggunakan penggunaan algoritma yang lebih efisien untuk menghasilkan password yang lebih kompleks.

Beberapa dari fitur tambahan ini dapat membantu meningkatkan keamanan password yang dihasilkan dan memungkinkan pengguna untuk memilih opsi yang paling cocok untuk kebutuhan mereka.
