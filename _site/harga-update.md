layout: default
title: Panel Update Harga
noindex: true
sitemap: false

<section class="update-header">
  <h1>Panel Update Harga</h1>
  <p>Semua halaman (Beranda, Katalog, Detail Produk, Update Stok) membaca harga dari satu sumber: <strong>_data/harga.yml</strong>. Ubah file tersebut untuk memperbarui harga di seluruh situs.</p>
</section>

<div class="stock-status-container">
  <table class="stock-table">
    <thead>
      <tr>
        <th>Produk</th>
        <th>Kategori</th>
        <th>Harga</th>
        <th>Satuan</th>
        <th>Stok</th>
        <th>Foto</th>
      </tr>
    </thead>
    <tbody>
      {% for item in site.data.harga %}
      <tr>
        <td class="prod-name">{{ item.produk }}</td>
        <td>{{ item.kategori }}</td>
        <td class="gold-text">Rp {{ item.harga }}</td>
        <td>{{ item.satuan }}</td>
        <td>{{ item.stok }}</td>
        <td>{{ item.foto }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

<div class="share-section">
  <p>Cara memperbarui:</p>
  <ol style="text-align:left; max-width: 800px; margin: 0 auto; color: #cfcfcf;">
    <li>Buka file <code>_data/harga.yml</code> di GitHub repo Anda.</li>
    <li>Edit harga, stok, atau foto sesuai kebutuhan, lalu simpan (commit).</li>
    <li>Deploy (GitHub Pages) akan membangun ulang, dan seluruh halaman akan memakai harga baru.</li>
  </ol>
  <a class="share-btn" href="https://github.com/xdev-app/xdev-app.github.io/edit/main/_data/harga.yml" target="_blank" rel="noopener">Buka Editor harga.yml di GitHub</a>
</div>
