---
layout: produk
title: "Telur Ayam Omega"
id_produk: "telur_omega"  # Kunci utama untuk ambil data dari _data/harga.yml
satuan: "kg"
kategori: "Fresh Product"
foto: "/assets/images/telur-ayam-omega-lokal.jpg"
---

{% assign p_id = page.id_produk | strip %}
{% assign live_data = site.data.harga[p_id] %}

Kami adalah agen resmi **{{ page.title }}** dengan kualitas premium untuk wilayah Bandung. Telur Omega kami memiliki kandungan nutrisi lebih tinggi dan kulit cangkang yang lebih kuat.

### Informasi Harga & Stok (Update Hari Ini)
* **Harga Grosir:** Rp **{{ live_data.harga | default: page.harga }}** / {{ page.satuan }}
* **Status Stok:** {% if live_data.stok == "Ready" %}
    <span class="status-pill ready">✓ Ready Stok</span>
  {% else %}
    <span class="status-pill limited">⚠ Stok Terbatas</span>
  {% endif %}
* **Update Terakhir:** {{ "now" | date: "%d %B %Y" }}

---

### Spesifikasi Produk:
* **Kemasan:** Ikat (isi kurang lebih **15 kg**) atau Peti Kayu.
* **Kondisi:** Sortir ketat (bebas pecah/retak) dan pembersihan cangkang.
* **Minimal Order:** 20 ikat untuk pengiriman gratis (Free Ongkir) seluruh wilayah Kota Bandung & Kabupaten Bandung.

### Keunggulan Alfutuhaat:
Sangat cocok untuk kebutuhan toko kue premium, restoran, atau konsumsi keluarga yang mengutamakan kesehatan. Kami menjamin kesegaran karena stok **Telur Ayam Omega** kami didatangkan langsung dari peternakan mitra setiap pagi.

<div class="cta-box">
    <h3>Pesan {{ page.title }} Sekarang</h3>
    <p>Dapatkan harga grosir terbaik untuk pengiriman area Bandung.</p>
    <a href="https://wa.me/{{ site.phone }}?text=Halo%20Alfutuhaat,%20saya%20ingin%20tanya%20stok%20{{ page.title }}" class="btn-wa">
        Hubungi Admin (WhatsApp)
    </a>
</div>
