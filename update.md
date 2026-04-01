---
layout: default
title: Update Stok Harian
description: Pantau ketersediaan stok pangan harian di Distributor Pangan Berkah.
---

<div class="update-header">
  <h1>Status Ketersediaan Barang</h1>
  <p>Pembaruan Terakhir: <span class="gold-text">{{ "now" | date: "%d %B %Y" }}</span></p>
</div>

{% include adsense.html %}

<div class="stock-status-container">
  <table class="stock-table">
    <thead>
      <tr>
        <th>Komoditas</th>
        <th>Harga Hari Ini</th>
        <th>Status Stok</th>
        <th>Info Pengiriman</th>
      </tr>
    </thead>
    <tbody>
      {% for entry in site.data.harga %}
        {% assign item = entry[1] %}
      <tr>
        <td class="prod-name"><strong>{{ item.produk }}</strong></td>
        <td class="gold-text">Rp {{ item.harga }}</td>
        <td>
          {% if item.stok == 'Ready' %}
            <span class="status-pill ready">● TERSEDIA</span>
          {% elsif item.stok == 'Terbatas' %}
            <span class="status-pill limited">● STOK TIPIS</span>
          {% else %}
            <span class="status-pill empty">○ HABIS</span>
          {% endif %}
        </td>
        <td>
          {% if item.stok == 'Ready' %}
            Ready Kirim (Bandung)
          {% else %}
            Cek Estimasi via WA
          {% endif %}
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<div class="share-section" style="text-align: center; margin-top: 40px;">
  <p>Bagikan update stok **Alfutuhaat** ke kolega Anda:</p>
  <a href="https://api.whatsapp.com/send?text=Cek%20update%20stok%20dan%20harga%20terbaru%20di%20Alfutuhaat%20Bandung%20hari%20ini:%20{{ site.url }}{{ page.url }}" class="share-btn" style="background: #25D366; color: white; padding: 12px 25px; border-radius: 8px; text-decoration: none; font-weight: bold; display: inline-block;">
    Bagikan ke WhatsApp
  </a>
</div>
