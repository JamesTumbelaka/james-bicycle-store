Nama        : James Zefanya Tumbelaka
NPM         : 2206824653
Kelas       : PBP E
Adaptable   : https://james-bicycle-store.adaptable.app/

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
    total_items = Product.objects.count()
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