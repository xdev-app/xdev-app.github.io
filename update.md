---
layout: default
title: Update Stok Harian
description: Pantau ketersediaan stok pangan harian di Distributor Pangan Berkah.
---

<div class="update-header">
  <h1>Status Ketersediaan Barang</h1>
  <p>Pembaruan Terakhir: <span class="gold-text">{{ "now" | date: "%d %B %Y, %H:%M" }} WIB</span></p>
</div>

<div class="stock-status-container">
  <table class="stock-table">
    <thead>
      <tr>
        <th>Komoditas</th>
        <th>Status</th>
        <th>Estimasi Kedatangan</th>
      </tr>
    </thead>
    <tbody>
      {% for item in site.data.harga %}
      <tr>
        <td class="prod-name">{{ item.produk }}</td>
        <td>
          {% if item.stok == 'Ready' %}
            <span class="status-pill ready">● TERSEDIA</span>
          {% elsif item.stok == 'Terbatas' %}
            <span class="status-pill limited">● STOK TIPIS</span>
          {% else %}
            <span class="status-pill empty">○ HABIS</span>
          {% endif %}
        </td>
        <td>{% if item.stok == 'Ready' %}Hari Ini{% else %}Hubungi Admin{% endif %}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<div class="share-section">
  <p>Bagikan status ini ke kolega Anda:</p>
  <a href="https://api.whatsapp.com/send?text=Cek%20update%20stok%20terbaru%20di%20Pangan%20Berkah%20hari%20ini:%20{{ site.url }}/update" class="share-btn">
    Bagikan ke WhatsApp
  </a>
</div>