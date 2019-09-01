# Writeup JOINTS CTF 2019

My first CTF writeup that I wrote in GitHub, enjoy~
Brief note : I've done this CTF with my friends from ITS, and unfortunately I can't solve any web problem on that CTF :( ~~goddamn Java and Vue + Laravel aren't compatible for my noob knowledge~~

~~And also ini problemsetternya wibu semua apa gimana anjir~~

## Guess
**Deskripsi**

Silahkan tebak angka random saya

`nc ctf.joints.id 30001`

**Pembahasan**
Pertama, kita lihat source code dari `guess.py` yang disertakan dalam soal.
Saat dilihat ada suatu fungsi `input()` yang menjadi perantara antara input user dan program. Dan diketahui pula bahwa fungsi input() memiliki suatu vuln (https://www.geeksforgeeks.org/vulnerability-input-function-python-2-x/), yang menyebabkan `input()` dapat dimasuki dengan variabel dan fungsi dalam program.
Memanfaatkan kelemahan dari fungsi `input()` tersebut, maka kita gunakan input berikut :

    open('./flag.txt','r').read()

Flag : `JOINTS19{pYTh0n2_1nPuT_15_3ViL_8190fe72}`


## Kapital
**Deskripsi :**

flag ada di /flag.txt
Ayo ngegas di shell

`nc ctf.joints.id 30002`

**Pembahasan :**
Saat program dieksekusi, program akan membuat input dari user menjadi huruf kapital, dan membuat command tidak bisa dieksekusi. Berdasarkan dari video LiveOverflow berikut (https://www.youtube.com/watch?V=6D1LnMj0Yt0), karena problemnya cukup mirip,  kami mencoba melakukan command `???/???`
Terlihat ada folder cat, artinya kita bisa mengeksekusi command cat.
Lalu, perhatikan bahwa file flag.txt terdiri dari 8 karakter, maka kita bisa mengeksekusi command berikut

    ???/??? ????????

Flag : `JOINTS19{M4iN_sh3LL_P4kAi_SiMb0l_f63a6af2}`
