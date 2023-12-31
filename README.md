Nama        : James Zefanya Tumbelaka
NPM         : 2206824653
Kelas       : PBP E
Adaptable   : https://james-bicycle-store.adaptable.app/
Link Web    : http://james-zefanya-tugas.pbp.cs.ui.ac.id/

# Membuat sebuah proyek Django baru.
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file baru dengan nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:
`django`
`gunicorn`
`whitenoise`
`psycopg2-binary`
`requests`
`urllib3`
5. Install *dependencies* dengan perintah `pip install -r requirements.txt` dalam mode virtual environment menyala.
6. Membuat proyek Django dengan nama yang diinginkan melalui perintah `django-admin startproject shopping_list .`
7. Buka file settings.py yang ada di dalam folder yang telah dibuat dan tambahkan '*' pada `ALLOWED_HOSTS` untuk mengizinkan akses dari semua *host*.
8. Buka kembali terminal dan jalankan perintah `python manage.py runserver` dan buka http://localhost:8000 untuk melihat apakah aplikasi Django berhasil dibuat.
9. Matikan server dengan menekan `Ctrl+C` di keyboard kemudian jalankan perintah `deactivate` untuk mematikan virtual environment. Add, commit, dan push hasil perubahan yang dilakukan ke GitHub.

# Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka berkas settings.py di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

# Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL yang terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.
2. Buka berkas `urls.py` di direktori proyek dan buka file `urls.py` di direktori `main` dan tambahkan rute URL seperti berikut:
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
*Path* `main/` akan diarahkan ke rute yang didefinisikan dalam berkas `urls.py` pada aplikasi `main`.

# Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
1. Buka file `models.py` dan isi file dengan nama dan atribut yang diminta.
2. Berdasarkan ketentuan soal, file harus setidaknya memiliki isi sebagai berikut:
```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` setiap kali melakukan perubahan pada model.

# Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka file `views.py` di dalam direktori `main`.
2. Tambahkan kode berikut ke dalam file.
```python 
from django.shortcuts import render
``` 
3. Tambahkan fungsi berikut ke dalam file.
```python
def show_main(request):
    context = {
        'name': 'nama',
        'class': 'kelas'
    }

    return render(request, "main.html", context)
```
4. Buat direktori dengan nama `templates` di dalam direktori main dan buat file dengan nama `main.html` kemudian isi dengan kode html untuk menampilkan data yang ada di file sebelumnya.
```html
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>
```

# Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


# Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-teman melalui Internet.
1. Buka web Adaptable.io dan buat akun melalui akun GitHub. 
2. Setelah login, tekan tombol `New APP`dan pilih `Connect an Existing Repository`.
3. Pilih `All Repositories` untuk memberikan akses kepada semua repository di akun GitHUB.
4. Pilih repository yang berisi aplikasi yang ingin di-*deploy*.
5. Pilih `Pyhon App Template` sebagai *template deployment*.
6. Pilih `PostgreSQL` sebagai tipe basis data.
7. Sesuaikan versi Python dan masukkan perintah `python manage.py migrate && gunicorn (nama direktori utama).wsgi.` di bagian `Start Command`.
8. Tulis nama aplikasi yang diinginkan dan centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai *deployment*.

# *Request client* ke web aplikasi berbasis Django beserta responnya
![Diagram](https://github.com/JamesTumbelaka/james-bicycle-store/assets/119837499/6d389dca-b19d-4a56-8fea-1b95d4cb93e5)

Pertama, *user* atau *client* akan meminta akses atau *resource*. Django akan kemudian akan memproses URL dari *client* dan menyesuaikannya sesuai dengan file `urls.py` (URL Mapping).
Kedua, Django akan akan membuka file `views.py` dan meminta tampilan. 
File `models.py` kemudian menangani data yang terkait permintaan pengguna dan folder `template` akan berisi file dengan ekstension html. File yang berisi ekstension html tersebut akan berisi kode-kode html untuk mengatur tulisan, tabel, ukuran, dan lainnya. Setelah selesai diproses, tampilan akan diberikan ke *client* atau *user*.
*Source*: https://intellipaat.com/blog/tutorial/python-django-tutorial/

# Fungsi Virtual Environment
Isolasi *Dependencies*
Virtual environment memungkinkan untuk mengisolasi dependensi pada proyek sehingga proyek satu tidak akan saling mengganggu proyek yang lain.

Mencegah konflik
Virtual environment membantu mencegah masalah yang mungkin muncul ketika berbagi proyek dengan orang lain.

Faktor Keamanan
Virtual environment memungkinkan penerapan berbagai konfigurasi dan versi python tanpa merusak instalasi Python global pada komputer kita. Virtual environment membatasi akses proyek terhadap instalasi Python global sehingga mencegah perubahan tidak terduga di berbagai proyek python.

Menyesuaikan Versi Python 
Penggunaan virtual environment memungkinkan user untuk menggunakan versi Python yang berbeda untuk berbagai proyek.

*Source*: https://csguide.cs.princeton.edu/software/virtualenv#:~:text=In%20a%20nutshell%2C%20Python%20virtual,or%20used%20by%20other%20projects.

# Apakah proyek Django tetap bisa dibuat tanpa Virtual Environment
Proyek Django tetap bisa dibuat tanpa menggunakan virtual environment, namun virtual environment disarankan untuk tetap digunakan untuk mencegah berbagai risiko yang dapat terjadi tanpa adanya virtual environment.

*Source*: https://www.w3schools.com/django/django_create_virtual_environment.php#:~:text=It%20is%20suggested%20to%20have,we%20will%20call%20it%20myworld%20.

# MVC, MVT, dan MVVM
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) merupakan tiga jenis pola arsitektur software yang berbeda dalam pengembangan aplikasi web. Ketiganya memiliki konsep yang mirip dalam separasi visualisasi, pemrosesan, dan manajemen data. Ketiga pola arsitektur tersebut bertujuan untuk meningkatkan fleksibilitas, kemudahan testing, dan memudahkan maintenance aplikasi.

### MVC (Model-View-Controller):
**Model:** komponen yang mengelola data dan logika aplikasi. Model berisi struktur data dan operasi terkait data.
**View:** komponen yang mengatur tampilan antarmuka pengguna. View mengambil data dari Model dan menampilkannya kepada pengguna.
**Controller:** komponen yang mengelola aliran kontrol dalam aplikasi. *Controller* menerima input dari pengguna, memprosesnya, dan berinteraksi dengan Model dan View sesuai dengan instruksi yang diberikan.

MVC biasanya digunakan dalam pengembangan aplikasi desktop, web, dan mobile.
Controller bertanggung jawab untuk menerima dan mengirimkan input dari pengguna, mengambil tindakan yang sesuai, dan memperbarui Model dan View sesuai kebutuhan.

### MVT (Model-View-Template):
**Model:** komponen yang mengelola data dan logika.
**View:** Tidak seperti *View* dalam MVC, *View* dalam MVT hanya bertanggung jawab untuk mengatur tampilan dan tidak memiliki logika.
**Template:** komponen yang mengatur cara data ditampilkan. Template menggabungkan data dari Model dengan tampilan.

MVT adalah varian dari MVC dan umumnya digunakan dalam kerangka kerja web yang didasarkan pada Python seperti Django.
Perbedaan utama adalah penggunaan Template, yang memisahkan tampilan dari logika sehingga memudahkan pengembangan dan pemeliharaan.

### MVVM (Model-View-ViewModel):
**Model:** komponen yang mengelola data dan logika.
**View:** komponen yang mengatur tampilan antarmuka pengguna.
**ViewModel:** komponen yang bertindak sebagai perantara antara *Model* dan *View*. *ViewModel* mengambil data dari *Model* dan mengubahnya menjadi format yang sesuai untuk ditampilkan *View*.

MVVM biasanya digunakan dalam pengembangan aplikasi berbasis data.
ViewModel memungkinkan binding dua arah antara Model dan View, yang memungkinkan perubahan data secara otomatis dalam tampilan.

*Source*: https://appmaster.io/id/blog/pola-arsitektur-mvc-mvp-dan-mvvm

# Tugas 3

## Perbedaan Antara Form POST dan Form GET dalam Django

### POST (HTTP POST method)
1. Data dikirim sebagai body request HTTP.
2. Invisible dalam URL, maka lebih aman untuk pengiriman data sensitif.
3. Digunakan untuk mengirim data yang akan dimasukkan atau diubah dalam server, seperti formulir atau penyimpanan data ke dalam database.
4. Data POST tidak tersimpan dalam cache web browser, maka tidak akan muncul di history browser ataupun URL.

### GET (HTTP GET method)
1. Data dikirim melalui URL sebagai query string.
2. Visible dalam URL, maka tidak aman untuk data sensitif karena dapat dilihat oleh orang lain.
3. Digunakan untuk mengambil data dari server, seperti mengambil hasil pencarian atau mengakses halaman web dengan parameter tertentu.
4. Data GET dapat disimpan dalam cache web browser, sehingga dapat muncul di history browser ataupun URL.

*Source*: https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST%20are%20typically,the%20state%20of%20the%20system

## Perbedaan Utama antara XML, JSON, dan HTML dalam Konteks Pengiriman Data

### XML (eXtensible Markup Language)
1. Merupakan format data yang digunakan untuk menggambarkan dan mengatur struktur data.
2. Lebih kompleks dan berat dibandingkan JSON dan HTML.
3. Sering digunakan dalam pertukaran data terstruktur antara aplikasi, terutama dalam environment dengan kebutuhan validasi tipe data yang ketat.

### JSON (JavaScript Object Notation)
1. Merupakan format data ringan yang digunakan untuk pertukaran data antar aplikasi.
2. Mudah dibaca oleh manusia dan mudah diinterpretasikan oleh mesin.
3. Biasa digunakan dalam pengembangan web modern untuk mengirim data antara server dan client, serta sebagai format konfigurasi dalam berbagai environment.

### HTML (Hypertext Markup Language)
1. Merupakan markup language yang digunakan untuk membuat halaman web dan menampilkan konten web.
2. Digunakan khusus untuk representasi konten yang ditampilkan di web browser.
3. Tidak digunakan untuk pertukaran data antar aplikasi, tetapi sebagai alat untuk merender dan menampilkan informasi kepada end user.

*Source*: https://www.geeksforgeeks.org/difference-between-json-and-xml/

## Mengapa JSON Sering Digunakan dalam Pertukaran Data antara Aplikasi Web Modern ?

### Ringkas dan Mudah Dibaca
JSON memiliki bentuk struktur yang simple dan mudah dibaca dan dimengerti oleh manusia, sehingga ideal untuk proses debugging.

### Mudah Diproses
JSON dapat diproses dengan mudah oleh bahasa pemrograman yang biasa digunakan, seperti JavaScript (banyak digunakan pada sisi client), Python, Java, dan bahasa pemrograman lainnya.

### Open Format
JSON merupakan format data terbuka yang disupport secara luas, sehingga berbagai aplikasi dan platform dapat mengkomunikasikan data dengan mudah.

### Ringan
JSON memiliki overhead yang rendah dalam hal data size yang dikirimkan lewat network, sehingga dapat menghemat bandwidth dari network yang digunakan.

### Compatible dengan JavaScript
JSON merupakan bentuk data yang compatible dengan JavaScript, sehingga sesuai untuk komunikasi antara client dan server dalam proses web development.

### Terstruktur dengan Baik
JSON mendukung struktur data yang simple dan well-structured, memungkinkan untuk mengirim objek dan nested array.

Karena karakteristik - karakteristik diatas, JSON menjadi pilihan utama dalam pertukaran data antara aplikasi web modern, baik dari sisi client maupun server.

*Source*: https://www.geekboots.com/story/json-with-advantage-and-disadvantage

# Langkah Implementasi Checklist Tugas

## Implementasi Skeleton sebagai Kerangka Views
Membuat skeleton yang akan berfungsi sebagai kerangka views dari situs web, untuk memastikan adanya konsistensi dalam desain situs web dan memperkecil terjadinya redundansi kode.

1. Membuat folder `templates` pada root folder dan membuat file HTML baru dengan nama `base.html`. File `base.html` akan berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk web page lainnya dalam proyek. File `base.html` di isi dengan kode berikut:

```html
{% load static }
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```

2. Membuka file `settings.py` yang ada pada subdirektori `bicycle_store` dan mencari baris yang mengandung `TEMPLATES`. Menyesuaikan kode yang ada dengan potongan kode berikut supaya file `base.html` terdeteksi sebagai file template.

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
        'APP_DIRS': True,
        ...
    }
]
...
```

3. Pada subdirektori `templates` yang ada pada direktori `main`, mengubah kode pada file `main.html` menjadi sebagai berikut:

```html
{% extends 'base.html' %}

{% block content %}
    <h1>Shopping List Page</h1>

    <h5>Name:</h5>
    <p>{{name}}</p>

    <h5>Class:</h5>
    <p>{{class}}</p>
{% endblock content %}
```
Pada kode diatas, `base.html` digunakan sebagai template utama program.

## Membuat Form Input Data dan Menampilkan Data Produk Pada HTML

1. Membuat file baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data produk baru. Menambahkan kode berikut dalam file `forms.py`.

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "amount", "description"]
```
Penjelasan Kode:
* `model = Product` untuk menunjukkan model yang akan digunakan untuk form. Saat data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek `Product`.
* `fields = ["name", "price", "amount", "description"]` untuk menunjukkan field dari model Product yang digunakan untuk form. Field `date_added` tidak dimasukkan ke list `fields` karena tanggal akan ditambahkan secar otomatis.

2. Buka file `views.py` yang ada pada folder `main` dan tambahkan beberapa import pada bagian atas.

```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
```

3. Membuat fungsi baru dengan nama `create_product` pada file tersebut yang menerima parameter `request` dan menambahkan kode di bawah ini untuk men-generate formulir yang dapat menambahkan data produk secara otomatis ketika data disubmit dari form.

```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

4. Mengubah fungsi `show_main` yang sudah ada pada file `views.py` menjadi seperti berikut:

```python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Pak Bepe', # Nama kamu
        'class': 'PBP A', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
```

5. Membuka `urls.py` yang ada pada folder `main` dan *import* fungsi `create_product` yang sudah dibuat.

```python
from main.views import show_main, create_product
```

6. Menambahkan path url ke dalam `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi yang sudah di-*import*

```python
path('create-product', create_product, name='create_product'),
```

7. Buat file HTML baru dengan nama `create_product.html` pada direktori `main/templates`. Isi file dengan kode berikut:

```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

8. Membuka `main.html` dan menambahkan kode berikut dalam `{% block content %}` untuk menampilkan data produk dalam bentuk table serta tombol "Add New Product" yang akan me-*redirect* ke halaman form.

```html
...
<table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>

{% endblock content %}
```

9. Mencoba menjalankan proyek Django dengan *command* `python manage.py runserver` dan membuka http://localhost:8000 di browser. Menambahkan beberapa data produk baru dan memeriksa apakah data yang ditambahkan sudah bisa ditampilkan pada halaman utama aplikasi.

## Mengembalikan Data dalam Bentuk XML, JSON, XML by ID, dan JSON by ID

1. Membuka `views.py` yang ada pada folder `main` dan tambahkan *import* `HttpResponse` dan `Serializer` pada bagian paling atas program.

```python
from django.http import HttpResponse
from django.core import serializers
```

2. Membuat sebuah fungsi yang menerima parameter *request* dengan nama `show_xml` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil *query* dari semua data yang ada pada `Product`. Menambahkan *return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.

```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

3. Membuka `urls.py` yang ada pada folder `main` dan *import* fungsi yang sudah dibuat.

```python
from main.views import show_main, create_product, show_xml 
```

4. Menambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di-*import*

```python
...
path('xml/', show_xml, name='show_xml'), 
...
```

5. Menjalankan proyek Django dengan `python manage.py runserver` dan buka http://localhost:8000/xml

6. Mengulangi proses langkah nomor `2` untuk pengembalian data dalam bentuk JSON, XML by ID, dan JSON by ID. Menambahkan fungsi - fungsi berikut:

```python
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

7. Membuka `urls.py` yang ada pada folder `main` dan *import* fungsi-fungsi yang sudah dibuat.

```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```

8. Menambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi-fungsi yang sudah di-*import*

```python
path('json/', show_json, name='show_json'),
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```

9. Menjalankan proyek Django dengan `python manage.py runserver` dan buka http://localhost:8000/json , http://localhost:8000/xml/[id] , http://localhost:8000/json/[id].

## Menggunakan Postman sebagai *Data Viewer*

1. Menjalankan server dengan perintah `python manage.py runserver`.
2. Membuka Postman dan membuat *request* baru dengan *method* `GET` dengan menggunakan *url* berikut:
* http://localhost:8000/
* http://localhost:8000/xml
* http://localhost:8000/json
* http://localhost:8000/xml/[id]
* http://localhost:8000/json/[id]
3. Men-*screenshot* hasil yang ditampilkan masing-masing *url*

## Screenshot Postman dengan Bentuk Data HTML
![Screenshot HTML](https://github.com/JamesTumbelaka/james-bicycle-store/blob/main/html%20ss.png)

## Screenshot Postman dengan Bentuk Data XML
![Screenshot XML](https://github.com/JamesTumbelaka/james-bicycle-store/blob/main/xml%20ss.png)

## Screenshot Postman dengan Bentuk Data JSON
![Screenshot JSON](https://github.com/JamesTumbelaka/james-bicycle-store/blob/main/json%20ss.png)

## Screenshot Postman dengan Bentuk Data XML Berdasarkan ID
![Screenshot XMLbyID](https://github.com/JamesTumbelaka/james-bicycle-store/blob/main/xml%20by%20id%20ss.png)

## Screenshot Postman dengan Bentuk Data JSON Berdasarkan ID
![Screenshot JSONbyID](https://github.com/JamesTumbelaka/james-bicycle-store/blob/main/json%20by%20id%20ss.png)

## Penjelasan Untuk Soal Bonus Point
Untuk menambahkan pesan "anda menyimpan X sepeda pada aplikasi ini", terdapat beberapa kode yang perlu ditambahkan dalam proyek.

1. Membuka `views.py` dan menambahkan kode berikut di dalam fungsi `show_main` dalam posisi seperti dibawah ini.

```python
def show_main(request):
    products = Product.objects.all()
    total_items = products.count()
    context = {
        'name': 'James Zefanya Tumbelaka',
        'class': 'PBP E',
        'products': products,
        'total_items': total_items,
    }

    return render(request, "main.html", context)
```
Potongan kode `total_items = Product.objects.count()` ditambahkan untuk men-*track* jumlah produk, dalam hal ini sepeda, yang sedang disimpan dalam aplikasi web ini.

2. Menambahkan kode di `main.html` untuk menampilkan pesan "anda menyimpan X sepeda pada aplikasi ini" sebelum bagian kode pembuatan table seperti berikut:

```html
...
<div class="current_total_item">
    <h4>anda menyimpan {{ total_items }} sepeda pada aplikasi ini</h4>
</div>
<table class="box">
        <thead>
...
```

3. Menjalankan perintah `python manage.py runserver` untuk menjalankan server. Mencoba menambahkan sepeda dalam aplikasi, pesan "anda menyimpan X sepeda pada aplikasi ini" sudah dapat ditampilkan diatas table produk.

# Tugas 4

## Apa Itu Django `UserCreationForm`, dan Jelaskan apa Kelebihan dan Kekurangannya ?

Django `UserCreationForm` merupakan salah satu form *built-in* yang tersedia dalam Django untuk mempermudah pembuatan user dalam sistem autentikasi dalam aplikasi web. Form memungkinkan developer web untuk membuat *sign-up page* dengan mudah tanpa harus memprogram form dari awal.

### Kelebihan

1. Dalam `UserCreationForm` sudah tersedia form pendaftaran yang sudah well-structured sehingga tidak perlu diprogram kembali dari awal.
2. Form sudah terintegrasi dengan sistem autentikasi Django, sehingga user yang sudah terdaftar dapat melakukan login dengan mudah setelah pendaftaran.
3. Di dalam form juga sudah termasuk program validasi user secara otomatis, seperti validasi keunikan alamat email atau penilaian tingkat keamanan password.

### Kekurangan

1. `UserCreationForm` pada beberapa kasus kurang fleksibel sehingga tidak mudah untuk disesuaikan dengan persyaratan - persyaratan khusus dari aplikasi web.
2. Form memiliki tampilan yang standar, sehingga akan memerlukan banyak proses kustomisasi untuk menyesuaikan dengan tema desain aplikasi.

## Apa Perbedaan antara Autentikasi dan Otorisasi dalam Konteks Django, dan Mengapa Keduanya Penting ?

### Autentikasi
Autentikasi merupakan proses verifikasi identitas pengguna web yang melakukan attempt untuk mengakses sistem atau aplikasi. Hal ini mencakup pemeriksaan dan konfirmasi kredensial pengguna, seperti nama dan password. Proses ini biasa dilakukan pada halaman login aplikasi web.

### Otorisasi
Otorisasi merupakan proses memberikan clearence atau hak akses kepada pengguna yang telah melewati proses autentikasi. Proses tersebut akan menentukan hal apa saja yang dapat dilakukan oleh pengguna setelah berhasil login ke aplikasi web. Proses otorisasi berperan dalam mengontrol hak akses pengguna terhadap resource ataupun fitur tertentu dalam aplikasi web.

Keduanya penting dan saling berkesinambungan karena memiliki fungsi yang sama, yakni menjaga keamanan sistem aplikasi web, dimana autentikasi berperan dalam verifikasi user, sedangan otorisasi mengatur aktivitas user dalam aplikasi web.

## Apa Itu *cookies* dalam Konteks Aplikasi Web, dan Bagaimana Django Menggunakan *cookies* untuk Mengelola Data Sesi Pengguna ?

Cookies adalah data berukuran kecil yang disimpan di sisi client dan digunakan oleh aplikasi web untuk mengidentifikasi dan melacak pengguna. Django menggunakan cookies untuk mengelola data sesi pengguna, seperti mengidentifikasi pengguna yang telah login dan menyimpan preferensi pengguna.

Django menyediakan built-in support untuk mengelola cookies dengan mudah melalui modul `django.http.Cookie`. Pengembang dapat menggunakan cookies untuk menyimpan informasi sesi, seperti token otentikasi, preferensi pengguna, ataupun data sesi lainnya.

## Apakah Penggunaan *cookies* Aman Secara *default* dalam Pengembangan Web, atau Apakah ada Risiko Potensial yang Harus Diwaspadai ?

Penggunaan cookies dalam pengembangan web memiliki beberapa risiko potensial yang harus diwaspadai, antara lain:
1. Ketidakamanan data, dimana data yang tersimpan dalam cookies dapat diakses oleh pengguna ataupun pihak lain yang memiliki akses fisik ke perangkat ke pengguna, sehingga tidak disarankan untuk menyimpan data sensitif dalam cookies serta mengkonfigurasi enkripsi untuk data cookies di server.
2. Risiko kebocoran data melalui web dengan protokol HTTP yang dapat disadap oleh pihak ketiga.
3. Tracking melalui cookies yang tidak transparan
4. Adanya risiko Cross-Site Scripting (XSS) dan Cross-Site Request Forgery (CSRF) yang dapat melanggar privasi data pengguna dalam web.

# Langkah Implementasi Checklist Tugas

## Membuat Fungsi dan Form Registrasi

1. Menjalankan virtual environment.
2. Membuka `views.py` pada subdirektori `main` dan menambahkan import `redirect`, `UserCreationForm`, dan `messages` pada bagian atas.

```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

3. Membuat fungsi dengan nama `register` yang menerima parameter `request`.

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

4. Membuat berkas HTML baru dengan nama `register.html` pada folder `main/templates`, dan mengisinya dengan kode berikut.

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

5. Membuka `urls.py` pada subdirektori `main` dan mengimpor fungsi yang sudah dibuat pada langkah sebelumnya.

```python
from main.views import register
```

6. Menambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport.

```python
...
path('register/', register, name='register'),
...
```

## Membuat Fungsi Login

1. Membuka `views.py` pada subdirektori `main` dan menambahkan import `authenticate` dan `login` pada bagian atas.

```python
from django.contrib.auth import authenticate, login
```

2. Membuat fungsi dengan nama `login_user` yang menerima parameter `request` seperti berikut.

```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

3. Membuat berkas HTML baru dengan nama `login.html` pada folder `main/templates` dan mengisinya dengan kode berikut.

```HTML
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

4. Membuka `urls.py` pada subdirektori `main` dan impor fungsi yang sudah dibuat.

```python
from main.views import login_user
```

5. Menambahkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimport.

```python
...
path('login/', login_user, name='login'),
...
```

## Membuat Fungsi Logout

1. Membuka `views.py` pada subdirektori `main` dan menambahkan import `logout` pada bagian atas.

```python
from django.contrib.auth import logout
```

2. Membuat fungsi `logout` yang menerima parameter `request`.

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

3. Membuka berkas `main.html` pada folder `main/templates`.
4. Menambahkan potongan kode berikut setelah *hyperlink tag* untuk *Add New Product* pada file `main.html`.

```HTML
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

5. Membuka `urls.py` pada subdirektori `main` dan mengimpor fungsi yang sudah dibuat.

```python
from main.views import logout_user
```

6. Menambahkan *path url* ke dalam *urlpatterns* untuk mengakses fungsi yang sudah diimport.

```python
path('logout/', logout_user, name='logout'),
```

## Merestriksi Akses Halaman Main

1. Membuka `views.py` pada subdirektori `main` dan mengimpor `login_required` pada bagian atas.

```python
from django.contrib.auth.decorators import login_required
```

2. Menambahkan kode berikut di atas fungsi `show_main` supaya halaman `main` hanya dapat diakses oleh pengguna yang sudah terautentikasi.

```python
...
@login_required(login_url='/login')
def show_main(request):
...
```

## Menggunakan Data Dari *Cookies*

1. Memastikan sudah melakukan logout dari aplikasi web Django.
2. Membuka `views.py` pada subdirektori `main` dan mengimpor beberapa fungsi berikut.

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

3. Memodifikasi fungsi `login_user` untuk menambahkan *cookie* yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan *login*.

```python
...
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

4. Menambahkan potongan kode berikut ke dalam variabel `context`.

```python
context = {
    'name': 'James Zefanya Tumbelaka',
    'class': 'PBP E',
    'products': products,
    'last_login': request.COOKIES['last_login'],
}
```

5. Mengubah fungsi `logout_user` menjadi seperti berikut.

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

6. Membuka berkas `main.html` dan menambahkan potongan kode berikut di antara tabel dan tombol *logout* untuk menampilkan data *last login*.

```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

7. Data *last login* seharusnya sudah muncul di halaman `main` setelah me-*refresh* halaman.

## Menghubungkan Product dengan User

1. Membuka `models.py` pada subdirektori `main` dan menambahkan kode berikut di bagian atas.

```python
...
from django.contrib.auth.models import User
...
```

2. Menambahkan potongan kode berikut dalam model `Product` yang sudah dibuat.

```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

3. Membuka `views.py` pada subdirektori `main`, dan mengubah potongan kode berikut pada fungsi `create_product`.

```python
def create_product(request):
 form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
 ...
```

4. Mengubah fungsi `show_main` menjadi seperti berikut.

```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
    ...
    }
...
```

5. Menyimpan semua perubahan dan melakukan migrasi model dengan perintah `python manage.py makemigrations`.

6. Memilih `1` untuk menetapkan *default value* untuk *field user* pada semua baris yang telah dibuat pada basis data.

7. Mengetik angka 1 kembali untuk menetapkan *user* dengan ID 1 (yang sudah dibuat sebelumnya)

8. Melakukan perintah `python manage.py migrate` untuk mengaplikasikan migrasi yang sudah dilakukan.

## Penjelasan Untuk Soal Bonus Point

### Fitur Menghapus Product

1. Membuka `views.py` dan mengimport fungsi `get_object_or_404`.

```python
from django.shortcuts import get_object_or_404
```

2. Membuat fungsi baru bernama `delete_product` yang menerima parameter `request` dan `id`.

3. Menambahkan kode berikut sebagai isi dari fungsi yang sudah dibuat.

```python
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        product.delete()
        return redirect('main:show_main')

    return render(request, 'delete_product.html', {'product': product})
```

4. Membuka `urls.py` dan mengimport fungsi yang sudah dibuat.

```python
from main.views import delete_product
```

5. Menambahkan *path url* untuk pemanggilan fungsi `delete_product`.

```python
...
path('delete_product/<int:id>/', delete_product, name='delete_product'),
...
```

6. Membuka `main.html` dan menambahkan kode berikut dibawah elemen tabel `product.date_added`.

```HTML
...
<td class="box-0lax">{{ product.date_added }}</td>
<td class="box-0lax">
    <a href="{% url 'main:delete_product' product.id %}">Delete</a>
</td>
...
```

7. Membuat berkas baru `delete_product.html` dalam subdirektori `main/templates` sebagai halaman konfirmasi penghapusan produk dalam inventori.

8. Menambahkan kode berikut sebagai isi dari `delete_product.html`.

```HTML
<!DOCTYPE html>
<html>
<head>
    <title>Confirm Deletion</title>
    <style type="text/css">
        body {
                font-family: 'Times New Roman', Times, serif;
                background-color:rgb(202, 200, 197);
            }
    </style>
</head>
<body>
    <h2>Confirm Deletion</h2>
    <p>Are you sure you want to delete this product?</p>
    <table>
        <tr>
            <td>
                <a href="{% url 'main:show_main' %}">Cancel</a>
            </td>
            <td>
                <form method="post">
                    {% csrf_token %}
                    <input type="submit" value="Delete">
                </form>
            </td>
        </tr>
    </table>
</body>
</html>
```

9. Menjalankan server dengan `python manage.py runserver` dan fitur `delete` untuk penghapusan produk dalam inventori sudah berfungsi.

### Fitur Menambah dan Mengurangi Nilai Amount

1. Membuka `views.py` dan membuat dua fungsi baru `increment_amount` dan `decrement_amount` yang menerima parameter `request` dan `id` untuk menambah dan mengurangi nilai `amount`.

2. Mengisi masing - masing fungsi dengan kode seperti berikut.

```python
def increment_amount(request, id):
    product = get_object_or_404(Product, pk=id)
    product.amount += 1
    product.save()
    return redirect('main:show_main')

def decrement_amount(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.amount > 0:
        product.amount -= 1
        product.save()
    return redirect ('main:show_main')
```

3. Membuka `urls.py` dan mengimport dua fungsi yang baru dibuat.

```python
from main.views import increment_amount, decrement_amount
```

4. Menambahkan *path url* untuk kedua fungsi yang sudah import.

```python
...
path('increment_amount/<int:id>/', increment_amount, name='increment_amount'),
path('decrement_amount/<int:id>/', decrement_amount, name='decrement_amount'),
...
```

5. Membuka `main.html` dan menambahkan tombol untuk `add` dan `sub` nilai `amount` di bawah komponen `product.amount`.
```HTML
...
<td class="box-0lax">{{ product.amount }}</td>
<td class="box-0lax">
    <form method="POST" action="{% url 'main:decrement_amount' product.id %}">
        {% csrf_token %}
        <button type="submit">sub</button>
    </form>
    <form method="POST" action="{% url 'main:increment_amount' product.id %}">
        {% csrf_token %}
        <button type="submit">add</button>
    </form>
</td>
...
```

6. Menjalankan server dengan perintah `python manage.py runserver` dan tombol `add` dan `sub` seharusnya sudah ditampilkan di kolom sebelah `Amount`.

# Tugas 5

## Jelaskan Manfaat dari Setiap *Element Selector* dan Kapan Waktu yang Tepat untuk Menggunakannya
### Element Selector (`tagname`)
Selector ini memilih semua elemen dengan tag yang sesuai. Kelebihannya adalah sederhana dan mudah digunakan. Selector ini dapat digunakan ketika ingin menerapkan *general style* pada semua elemen dengan tag yang sama, misalnya mengubah semua teks pada elemen <p> menjadi warna biru.

### Class Selector (`.classname`)
Class selector berfungsi untuk memilih elemen berdasarkan nama kelas yang diberikan. Selector ini akan sangat berguna ketika ingin menerapkan gaya yang sama pada beberapa elemen yang tidak perlu memiliki tag yang sama. Misalnya, kita bisa menggunakan class selector untuk mengubah warna teks pada beberapa elemen <div> tanpa harus memberikan tag yang sama untuk semua elemen tersebut.

### ID Selector (`#idname`)
ID Selector memilih elemen dengan atribut `id` yang sesuai. Selector ini digunakan ketika kita ingin menerapkan gaya atau memanipulasi elemen unik tertentu pada halaman HTML. ID harus unik dalam satu halaman, sehingga selector ini cocok untuk digunakan pada elemen - elemen yang hanya ada satu dalam halaman.

### Universal Selector (`*`)
Universal selector memilih semua elemen dalam dokumen HTML. Selector ini sebaiknya digunakan dengan hati-hati karena dapat memiliki dampak besar pada performa halaman HTML. Selector dapat digunakan hanya dalam situasi tertentu, seperti menetapkan margin dan padding standar ke nol untuk menghindari perbedaan bawaan antara browser.

### Pseudo-Class Selector (`:pseudo-class`)
Pseudo-class selector digunakan untuk memilih elemen dalam kondisi tertentu atau dalam keadaan tertentu, seperti elemen yang sedang dihover oleh kursor atau elemen yang berada dalam keadaan aktif. Selector ini bermanfaat untuk memberikan interaksi dan tampilan yang dinamis pada elemen.

## Beberapa Contoh HTML5 Tag
1. `<header>` : Menunjukkan bagian judul utama atau sub judul dalam halaman web, dengan contoh penerapan seperti <h1>Judul</h1> untuk Heading 1.
2. `<nav>` : Mengelompokkan elemen-elemen yang berfungsi sebagai menu navigasi.
3. `<section>` : Membagi halaman web menjadi bagian-bagian yang berbeda, seperti bagian untuk berita, artikel, atau konten lainnya.
4. `<article>` : Mendefinisikan konten yang dapat berdiri sendiri, seperti artikel berita atau blog.
5. `<aside>` : Menunjukkan konten yang berhubungan dengan konten di sekitarnya, seperti sidebar.
6. `<footer` : Bagian bawah dari sebuah halaman web dan berisi informasi seperti hak cipta atau tautan ke halaman terkait.

## Perbedaan Antara Margin dan Padding
### Margin
Margin adalah jarak antara elemen dengan elemen-elemen di luarnya (biasanya elemen tetangga). Margin digunakan untuk mengatur ruang antara elemen tersebut dan elemen-elemen lain di sekitarnya. Margin tidak memiliki background color dan tidak akan mengubah warna latar belakang elemen tersebut.

### Padding
Padding adalah jarak antara konten elemen dan batas elemen itu sendiri. Padding digunakan untuk mengatur ruang antara konten elemen dan tepi elemen tersebut. Padding dapat memiliki background color dan akan mempengaruhi warna latar belakang elemen.

## Perbedaan antara CSS Framework Bootstrap dan Tailwind
### Bootstrap
* Menyediakan desain bawaan yang lebih lengkap dan atraktif secara visual.
* Menggunakan kelas-kelas yang lebih banyak, sehingga memungkinkan pembuatam *interface* lebih cepat dengan penulisan HTML yang lebih sedikit.
* Lebih cocok untuk proyek-proyek yang memerlukan pengembangan cepat dan desain yang sudah ada.

### Tailwind CSS
* Lebih modular dan memungkinkan kustomisasi setiap komponen dengan lebih rinci.
* Tidak memiliki gaya desain bawaan, sehingga tampilannya lebih minimalis.
* Menggunakan kelas-kelas kecil untuk mengatur styling, yang memerlukan lebih banyak penulisan HTML.
* Cocok untuk proyek-proyek yang memerlukan desain kustom yang sangat spesifik.

## Kapan Sebaiknya Menggunakan Bootstrap atau Tailwind CSS ?
* Sebaiknya gunakan Bootstrap jika kita ingin mengembangkan dengan cepat dan kita tidak memiliki banyak waktu untuk menyesuaikan desain. Ini juga cocok jika kita tidak memiliki pengalaman desain web yang banyak.

* Sebaiknya gunakan Tailwind CSS jika kita ingin desain yang sangat kustom dan kita memiliki waktu untuk mengatur setiap detailnya. Ini cocok jika kita ingin menciptakan tampilan yang unik dan sesuai dengan kebutuhan proyek kita.

# Implementasi Langkah Pengerjaan Tugas
## Menambahkan Bootstrap CSS, Javascript dan styling CSS
1. Membuka `base.html` dalam folder `templates` dan menambahkan Bootstrap CSS dan JavaScript di bagian `<head>`.
```HTML
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
```

2. Menambahkan kode berikut sebagai kustomisasi elemen - elemen HTML di bawah `</title>` pada berkas `base.html`.
```HTML
 <style type="text/css">
    .productform {
        font-family:"Rubik";
    }
    .card {
        font-weight: bold;
        margin-left: 30px;
    }
    .current_total_item {
        text-align: center;
        color: red;
        font-family: Menlo, monospace;
        text-decoration: underline;
        font-size: 15px;
    }
    .box {
        border: 2px solid black;
        border-collapse: collapse; 
        border-spacing: 0;
        margin-left: auto; 
        margin-right: auto;
    }
    .box td {
        border-color: black; 
        border-style: solid; 
        border-width: 2px; 
        font-family: 'Times New Roman', Times, serif; 
        font-size: 14px;
        overflow: hidden; 
        padding: 10px 5px; 
        word-break: normal;
        text-align: center;
        background-color: rgb(226, 221, 219);
    }
    .box th {
        border-color: black; 
        border-style: solid; 
        border-width: 2px; 
        font-family: 'Times New Roman', Times, serif; 
        font-size: 16px;
        font-weight: bold; 
        color: white;
        overflow: hidden; 
        padding: 10px 5px; 
        word-break: normal;
        text-align: center;
        background-color: rgb(38, 36, 36);
    }
    .createproduct {
        background-color: rgb(202, 200, 197);
    }
    .add_product {
        text-align: left;
    }
    .marquee-container {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: black;
        text-align: left;
        white-space: nowrap;
        overflow: hidden;
    }
    .add_product {
        color: black;
        text-align: center;

    }
    body {
        font-family: 'Times New Roman', Times, serif;
        background-color: whitesmoke;
    }
</style>
```

## Menambahkan *navbar* dalam Aplikasi Web
1. Membuka berkas `main.html` kemudian menambahkan kode berikut untuk membentuk *navbar* yang akan berisi Nama Toko, tombol `Add Product` dan `Logout`.
```HTML
<nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
        <a class="navbar-brand">James Bicycle Store</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'main:create_product' %}">Add Product</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="{% url 'main:logout' %}">Logout</a>
                </li>
            </ul>
        </div>
        </div>
    </nav>
```

2. Membuka berkas `base.html` dan menambahkan sedikit perubahan *styling* untuk *navbar* yang sudah dibuat.
```HTML
<style type="text/css">
            .productform {
                font-family:"Rubik";
            }
            .container-fluid {
                margin-left: 25px;
            }
            .navbar-brand {
                font-weight: bold;
            }
            ...
```

## Menambahkan Fitur Edit Product
1. Membuka `views.py` dan menambahkan fungsi berikut yang akan berfungsi untuk mengubah isi produk.
```python
def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

2. Membuka `urls.py` pada direktori `main` dan mengimpor fungsi yang sudah dibuat.
```python
from main.views import edit_product
```

3. Menambahkan *path url* untuk pemanggilan fungsi `edit_product`.
```python
path('edit-product/<int:id>', edit_product, name='edit_product'),
```

4. Membuat berkas baru bernama `edit_product.html` yang akan berfungsi sebagai halaman edit produk dan menambahkan kode berikut pada berkas tersebut.
```HTML
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <a href="{% url 'main:show_main' %}">Cancel</a>
                <input type="submit" value="Edit Product"/>
            </td>
            <td>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

5. Membuka `main.html` dan menambahkan kode berikut pada ujung setiap baris pada tabel produk.
```HTML
...
    <td>
        <a href="{% url 'main:edit_product' product.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    ...
```

6. Menjalankan proyek Django dengan perintah `python manage.py runserver` dan fitur edit produk sudah dapat terlihat di ujung setiap baris produk dan berfungsi dengan seharusnya.

# Tugas 6

## Jelaskan Perbedaan antara *Asynchronous Programming* dengan *Synchronous Programming*

Pada pemrograman asinkronus, *task - task* akan dieksekusi tanpa harus menunggu tugas sebelumnya selesai. Sebuah tugas dapat dimulai, kemudian tugas lain akan dapat dimulai sebelum tugas pertama selesai. Hal ini berguna untuk mengatasi operasi I/O yang memakan banyak waktu. Hal ini membuat aplikasi terasa lebih responsif dan memungkinkan aplikasi untuk mengelola banyak operasi secara bersamaan.

Pada pemrograman sinkronus atau *blocking*, *task - task* akan dieksekusi secara berurutan. Task berikutnya harus menunggu *task* sebelumnya selesai dieksekusi sebelum dapat dijalankan. Jika terdapat operasi I/O yang memakan waktu banyak, seperti menarik data dari server, maka seluruh eksekusi program JS akan berhenti dan menunggu operasi selesai. Hal ini akan mengakibatkan aplikasi terasa lambat dan kurang responsif jika terdapat operasi berjalan yang memakan banyak waktu.

## Jelaskan Maksud dari Paradigma *Event-Driven Programming* dan Sebut Salah Satu Contoh Penerapannya

Paradigma *Event-Driven Programming* merupakan pendekatan pemrograman dimana *execution flow* program tidak ditentukan oleh urutan *task* yang sudah didefinisikan terlebih dahulu, melainkan berdasarkan kejadian atau events yang terjadi selama eksekusi program. Program dapat merespon kejadian yang terjadi secara asinkronus, seperti user interaction, input, dan event lainnya yang akan men-trigger fungsi web yang sesuai.

Salah satu contohnya adalah menambahkan *event listener* dalam sebuah button yang akan memanggil fungsi sesuai dengan yang sudah didefinisikan dalam script.

```HTML
<body>
    <button id="myButton">Klik</button>
    <p id="output"></p>

    <script>
        // Mendapatkan referensi ke elemen tombol
        var button = document.getElementById("myButton");

        // Menambahkan event listener ke tombol
        button.addEventListener("click", function() {
            // Ketika tombol di-klik, tindakan ini akan dijalankan
            var output = document.getElementById("output");
            output.innerHTML = "Tombol telah diklik!";
        });
    </script>
</body>
```

## Jelaskan Penerapan *Asynchronous Programming* pada AJAX

Berikut langkah - langkah yang umum dilakukan dalam menerapkan *asynchronous programming* pada AJAX:
1. Membuat `asynchronous request` ke server.
2. Mendefinisikan fungsi respons yang akan dijalankan ketika respons dari server diterima, biasa disebut sebagai *callback function*.
3. Mengirim permintaan ke server dengan metode `GET` atau `POST`.
4. Program menunggu respons.
5. Program menangani respons setelah server merespons, dengan menjalankan `callback function` yang sudah didefinisikan.

## Bandingkan Fetch API dengan Library jQuery dan Tuliskan Pendapat Terkait Teknologi Manakah yang Lebih Baik untuk Digunakan

### Fetch API

Beberapa kelebihan dari penggunaan `Fetch API` yakni Native Browser Support, penggunaan konsep Promise (kode asinkron lebih mudah dibaca), serta lebih fleksibel, dimana web developer memiliki lebih banyak kontrol atas permintaan dan respons HTTP. Kekurangan dari `Fetch API` adalah dari segi *learning curve* untuk developer, dimana memerlukan banyak pengalaman untuk dapat beradaptasi, terutama untuk konsep Promises.

### jQuery

Kelebihan utama dari penggunaan `jQuery` adalah dari segi kemudahan penggunaan, dimana `jQuery` dirancang untuk menyederhanakan *common tasks* pada *web development*, sehingga dapat membuat proses pengembangan lebih cepat.

### Pendapat

Menurut pendapat saya, dengan mempertimbangkan kelebihan dan kekurangan teknologi masing - masing, `Fetch API` lebih baik untuk digunakan, terutama untuk memahami konsep - konsep dasar dari JavaScript, untuk memperoleh *skill* yang *transferrable* ke proyek - proyek web lain.

# Langkah Implementasi Checklist

## AJAX GET

1. Membuka berkas `views.py` dan membuat fungsi baru bernama `get_product_json` yang menerima parameter `request` dan mengisinya dengan kode seperti berikut.

```python
def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))
```

2.  Membuka berkas `urls.py` dan membuat path url untuk fungsi yang sudah dibuat.

```python
...
path('get-product/', get_product_json, name='get_product_json'),
...
```

3. Membuka berkas `main.html` dan membuat block `<script>` di bagian bawah berkas dan menambahkan fungsi baru dengan nama `getProducts()`.

```HTML
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
</script>
```

4. Mengubah bagian kode tabel di `main.html` menjadi bentuk card seperti ini untuk diproses dengan Ajax.

```HTML
<div class="row row-cols-1 row-cols-md-3 row-cols-sm-2 row-cols-xs-1 g-4">
</div>
```

## AJAX POST

1. Membuka berkas `views.py` , mengimpor `@csrf_exempt`, dan membuat fungsi `add_product_ajax` yang menerima parameter `request`dan mengisinya dengan kode seperti berikut.

```python
from django.views.decorators.csrf import csrf_exempt
...
@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_product = Product(name=name, price=price, amount=amount, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
```

2. Membuka berkas `urls.py` dan membuat path url untuk memanggil fungsi yang sudah dibuat.

```python
...
path('create-ajax/', add_product_ajax, name='add_product_ajax'),
...
```

3. Membuka berkas `main.html` dan menambahkan fungsi `refreshProducts()` untuk melakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar sepeda yang sudah diperbarui tanpa reload halaman utama secara keseluruhan.

```HTML
<script>
    ...
    async function refreshProducts() {
            document.querySelector(".row").innerHTML = "";
            const products = await getProducts();
            
            products.forEach((item, index) => {
                const productCard = `
                    <div class="col">
                        <div class="card mb-4">
                            <div class="card-body">
                                <h5 class="card-title">${item.fields.name}</h5>
                                <p class="card-text">${item.fields.description}</p>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">Price: ${item.fields.price}</li>
                                <li class="list-group-item">Amount: ${item.fields.amount}</li>
                                <li class="list-group-item">Date Added: ${item.fields.date_added}</li>
                            </ul>
                            <div class="card-body">
                                <a onclick="openEditModal(${item.pk}, '${item.fields.name}', ${item.fields.price}, ${item.fields.amount}, '${item.fields.description}')">
                                    <button type="button" class="btn btn-sm btn-primary">Edit</button>
                                </a>
                                <button type="button" class="btn btn-sm btn-danger" onclick="showConfirmationModal(${item.pk})">Delete</button>
                            </div>
                        </div>
                    </div>`;
                
                const row = document.querySelector(".row");
                row.innerHTML += productCard;

            
            });
        }

        refreshProducts();
    ...
</script>
```

4. Membuat tombol yang akan membuka modal untuk melakukan `add product`.

```HTML
<div class="add_product_ajax_button">
        <button type="button" class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#productModal">Add Product by AJAX</button>
</div>
```

5. Membuat modal yang akan berfungsi untuk mengisi data produk yang akan ditambahkan kedalam daftar produk.

```HTML
...
<div class="modal fade" id="productModal" tabindex="-1" aria-labelledby="productModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="productModalLabel">Add New Product</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
            </div>
        </div>
    </div>
</div>
...
```

6. Membuat fungsi JavaScript pada bagian blok `<script>` untuk menambah produk menggunakan Ajax.

```HTML
<script>
    ...
    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts)

        document.getElementById("form").reset()
        return false
    }
    ...
</script>
```

7. Menambahkan potongan kode berikut untuk menghubungkan tombol dengan fungsi yang akan memanggil modal produk dan menambahkan hasilnya ke daftar produk.

```HTML
<script>
    document.getElementById("button_add").onclick = addProduct;
    document.getElementById("addProductLink").addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default behavior of the link
        document.querySelector('[data-bs-target="#productModal"]').click();
    });
</script>
```

8. Melakukan *refresh page* dan fitur *add product* dengan Ajax sudah berfungsi seperti seharusnya.

## Melakukan Perintah `collectstatic`

1. Membuka terminal pada direktori utama dan menjalankan perintah berikut untuk mengumpulkan file static dari setiap aplikasi ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi.

```sh
python manage.py collectstatic
```

2. Folder `static` sudah terbentuk di dalam direktori utama.

## Penjelasan Langkah Jawaban Soal Bonus

1. Membuka berkas `views.py` dan membuat fungsi baru yang menerima parameter `request` dan `id` dengan nama `delete_product_ajax`.

```python
...
@csrf_exempt
def delete_product_ajax(request, id):
    product = Product.objects.get(pk = id)
    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    return HttpResponseNotFound()
...
```

2. Membuka berkas `urls.py` dan membuat path url untuk memanggil fungsi yang baru dibuat sebelumnya.

```python
...
path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
...
```

3. Membuka berkas `main.html` dan menambahkan fungsi dengan nama `deleteProduct()` yang menerima parameter `productID` pada blok `<script>` untuk mengakses fungsi yang sudah dibuat, dan mengisinya dengan kode berikut.

```HTML
<script>
    ...
    function deleteProduct(productId) {
        fetch(`{% url 'main:delete_product_ajax' 0 %}`.replace('0', productId), {
            method: "POST"
        })
        .then((response) => {
            if (response.ok) {
                refreshProducts();
            } else {
                alert("Delete failed. Please try again.");
            }
        })
        .catch((error) => {
            console.error("Error while deleting product:", error);
            alert("Delete failed. Please try again.");
        });
    }
    ...
</script>
```

4. Membuat modal konfirmasi penghapusan produk yang akan muncul jika tombol delete ditekan.

```HTML
<div class="modal fade" id="confirmationModal" tabindex="-1" aria-labelledby="confirmationModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="confirmationModalLabel">Confirm Deletion</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>Are you sure you want to remove this bicycle ?</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                <button type="button" class="btn btn-danger" id="confirmDelete" data-bs-dismiss="modal">Remove</button>
            </div>
        </div>
    </div>
</div>
```

5. Membuat fungsi untuk menampilkan `confirmationModal` setelah tombol Delete ditekan.
```HTML
<script>
    function showConfirmationModal(productId) {
            document.getElementById("confirmDelete").setAttribute("data-product-id", productId);

            document.getElementById("confirmDelete").addEventListener("click", function() {
                const productId = this.getAttribute("data-product-id");
                deleteProduct(productId);
            });

            const confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));
            confirmationModal.show();
        }
</script>
```

6. Memodifikasi table daftar produk sehingga tombol `delete` terdapat di setiap `Card` produk.

```HTML
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
    async function refreshProducts() {
            document.querySelector(".row").innerHTML = "";
            const products = await getProducts();
            
            products.forEach((item, index) => {
                const productCard = `
                    <div class="col">
                        <div class="card mb-4">
                            <div class="card-body">
                                <h5 class="card-title">${item.fields.name}</h5>
                                <p class="card-text">${item.fields.description}</p>
                            </div>
                            <ul class="list-group list-group-flush">
                                <li class="list-group-item">Price: ${item.fields.price}</li>
                                <li class="list-group-item">Amount: ${item.fields.amount}</li>
                                <li class="list-group-item">Date Added: ${item.fields.date_added}</li>
                            </ul>
                            <div class="card-body">
                                <a onclick="openEditModal(${item.pk}, '${item.fields.name}', ${item.fields.price}, ${item.fields.amount}, '${item.fields.description}')">
                                    <button type="button" class="btn btn-sm btn-primary">Edit</button>
                                </a>
                                <button type="button" class="btn btn-sm btn-danger" onclick="showConfirmationModal(${item.pk})">Delete</button>
                            </div>
                        </div>
                    </div>`;
                
                const row = document.querySelector(".row");
                row.innerHTML += productCard;

            });
        }

        refreshProducts();
```

7. Melakukan *refresh page* dan tombol `Delete` sudah berfungsi sesuai dengan proses fungsi yang sudah didefinisikan sebelumnya.


