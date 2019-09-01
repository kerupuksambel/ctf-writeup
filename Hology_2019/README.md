## Easy Dian
Pada soal tersebut, diberikan suatu file binary 64-bit yang berisi program yang berisi flag. Saat program direverse dengan Ghidra, muncul tampilan berikut.
![enter image description here](https://github.com/kerupuksambel/ctf-writeup/raw/master/Hology_2019/dian/Dian_1.png)

Saat ditampilkan ke bentuk grafik, terdapat tampilan berikut.
![enter image description here](https://github.com/kerupuksambel/ctf-writeup/raw/master/Hology_2019/dian/Dian_2.png)

Pada grafik, ada komparasi berkali-kali pada stack yang berbeda, jadi kita tinggal melihat stack yang terlihat ada, lalu tinggal diurutkan sesuai dengan urutan komparasi.
![enter image description here](https://github.com/kerupuksambel/ctf-writeup/raw/master/Hology_2019/dian/Dian_3.png) 

Flag : **hctf{L3ts_le4RN_3ndianeS5_s1mply_6abf90}**
