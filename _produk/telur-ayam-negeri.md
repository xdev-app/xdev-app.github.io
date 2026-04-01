---
layout: produk
title: "Telur Ayam Lokal"
id_produk: "telur_lokal"
satuan: "kg"
kategori: "Fresh Product"
foto: "/assets/images/telur-ayam-lokal.jpg"
---

{% assign p_id = page.id_produk %}
{% assign p_data = site.data.harga[p_id] %}

Kami adalah agen sembako **{{ page.title }}** dengan kualitas terbaik di Bandung. Produk kami selalu baru setiap harinya karena diambil langsung dari mitra peternak.

### Informasi Harga & Stok (Update Hari Ini)
* **Harga Terkini:** Rp **{{ p_data.harga }}** / {{ page.satuan }}
* **Status Stok:** {% if p_data.stok == "Ready" %}
    <span class="status-pill ready">✓ Ready Stok</span>
  {% else %}
    <span class="status-pill limited">⚠ Stok Terbatas</span>
  {% endif %}

---

### Spesifikasi Produk:
* **Kemasan:** Ikat (isi kurang lebih **15 kg**) atau Peti.
* **Kondisi:** Sortir ketat (bebas pecah dan retak).
* **Minimal Order:** 20 ikat untuk pengiriman gratis wilayah Bandung.

### Keunggulan Alfutuhaat:
Sangat cocok untuk kebutuhan warung sembako, toko kue, atau konsumsi rumah tangga dalam partai besar. Kami menjamin **tidak ada telur busuk** dalam setiap kiriman karena telah melalui proses sortir manual.

<div class="cta-box">
    <h3>Pesan {{ page.title }} Sekarang</h3>
    <p>Dapatkan harga grosir terbaik untuk pengiriman area Bandung.</p>
    <a href="https://wa.me/{{ site.phone }}?text=Halo%20Alfutuhaat,%20saya%20ingin%20tanya%20stok%20{{ page.title }}" class="btn-wa">
        Hubungi Admin (WhatsApp)
    </a>
</div>
