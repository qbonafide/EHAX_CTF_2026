Borderline personality

Diberikan chall webex seperti berikut

![](/borderline_personality/screenshoots/1.png)


Pertama, aku analisis web dengan inspect dulu, ga ketemu apa-apa, lalu kan tadi dikasih handout.zip, mungkin bisa analisis sesuatu dari situ. Di `app.py`:
```python
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# The UI Template


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/submit', methods=['POST'])
def submit():
    data = request.get_data()
    return jsonify({"status": "success", "message": "Data received."}), 200


@app.route('/admin/flag', methods=['GET', 'POST'])
def flag():
    return "EHAX{TEST_FLAG}\n", 200


@app.errorhandler(404)
def not_found(e):
    return "Not Found\n", 404
```

Di sini itu terlihat kalau pakai endpoint /admin/flag bakal muncul flag. Sekarang kita liat `haproxy.cfg`:
```
global
    log stdout format raw local0
    maxconn 2000

defaults
    log     global
    mode    http
    option  httplog
    timeout connect 5000ms
    timeout client  50000ms
    timeout server  50000ms

frontend http-in
    bind *:8080
    
    acl restricted_path path -m reg ^/+admin
    http-request deny if restricted_path
    
    default_backend application_backend

backend application_backend
    server backend1 backend:5000
```


Di sini terlihat kalau HAProxy blok semua request yang path-nya dia lihat diawali /admin (juga //admin, ///admin, dst), seementara Flask backend nggak punya proteksi sama sekali di /admin/flag, jadi yang perlu dilakukan itu tinggal encode urlnya aja supaya bisa bypass haproxy, contohnya: `/%61dmin/flag`, %61 itu mewakili huruf a sehingga bisa bypass haproxy dan ketemu flagnya.

![](/borderline_personality/screenshoots/flag.png)