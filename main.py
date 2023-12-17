from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Inisialisasi objek SocketIO dan mengaitkannya dengan aplikasi Flask
socketio = SocketIO(app)

# List untuk menyimpan pesan-pesan yang dikirim melalui soket
messages = []

# Route untuk halaman utama
@app.route('/')
def index():
    # Render template 'index.html' dengan memberikan data pesan ke template
    return render_template('index.html', messages=messages)

# Event handler untuk event 'message' dari soket
@socketio.on('message')
def handle_message(msg):
    # Cetak pesan di server
    print('Message:', msg)
    
    # Menambahkan pesan ke dalam list messages
    messages.append(msg)
    
    # Mengirim pesan ke semua klien yang terhubung (broadcast=True)
    send(msg, broadcast=True)

# Menjalankan aplikasi Flask dengan SocketIO
if __name__ == '__main__':
    # Menggunakan SocketIO untuk menjalankan aplikasi dengan mode debug
    socketio.run(app, debug=True)
