from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Konfigurasi Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pesanan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model Database
class Pesanan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_produk = db.Column(db.String(100))
    jumlah = db.Column(db.Integer)
    status = db.Column(db.String(20), default='Pending')

with app.app_context():
    db.create_all()

# 1. Home Route (Agar tidak 404 saat dibuka di browser)
@app.route('/')
def index():
    return jsonify({"pesan": "Backend Distributor Pangan aktif!"})

# 2. CREATE: Simpan Order (POST)
@app.route('/api/order', methods=['POST'])
def simpan_order():
    data = request.json
    if not data or 'nama' not in data:
        return jsonify({"error": "Data tidak lengkap"}), 400
        
    baru = Pesanan(nama_produk=data['nama'], jumlah=data.get('jumlah', 1))
    db.session.add(baru)
    db.session.commit()
    return jsonify({"pesan": "Pesanan berhasil dicatat!", "id": baru.id}), 201

# 3. READ: Ambil Semua Order (GET)
@app.route('/api/orders', methods=['GET'])
def ambil_semua_order():
    semua_pesanan = Pesanan.query.all()
    hasil = []
    for p in semua_pesanan:
        hasil.append({
            "id": p.id,
            "nama_produk": p.nama_produk,
            "jumlah": p.jumlah,
            "status": p.status
        })
    return jsonify(hasil)

if __name__ == '__main__':
    app.run(debug=True, port=5000)