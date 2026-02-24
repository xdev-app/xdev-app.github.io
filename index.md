---
layout: default
title: Home
---

<section class="hero">
  <h1>{{ site.title }}</h1>
  <p>{{ site.description }}</p>
</section>

<section class="product-slideshow">
  <div class="slider">
    <div class="slider-track">
      {% for item in site.data.harga limit:5 %}
      <div class="slide">
        <div class="slide-image">
          <img src="{{ '/assets/images/' | relative_url }}{{ item.foto }}" alt="{{ item.produk }}" onerror="this.src='https://placehold.co/800x500?text=Gambar+Kosong'">
        </div>
        <div class="slide-content">
          <span class="category">{{ item.kategori }}</span>
          <h3 class="slide-title">{{ item.produk }}</h3>
          <div class="price-value">
            <span class="currency">Rp</span>
            <span class="amount">{{ item.harga }}</span>
            <span class="unit">/{{ item.satuan }}</span>
          </div>
          <a href="https://wa.me/{{ site.phone }}?text=Halo,%20saya%20ingin%20pesan%20{{ item.produk }}" class="slide-btn">Pesan via WhatsApp</a>
        </div>
      </div>
      {% endfor %}
    </div>
    <button class="slide-arrow prev" aria-label="Sebelumnya">‹</button>
    <button class="slide-arrow next" aria-label="Berikutnya">›</button>
    <div class="slide-dots">
      {% for item in site.data.harga limit:5 %}
      <button class="dot" data-index="{{ forloop.index0 }}" aria-label="Slide {{ forloop.index }}"></button>
      {% endfor %}
    </div>
  </div>
</section>

<div class="filter-container">
  <button class="filter-btn active" onclick="filterProduct('all')">Semua</button>
  <button class="filter-btn" onclick="filterProduct('Fresh Product')">Telur & Segar</button>
  <button class="filter-btn" onclick="filterProduct('Rice & Grains')">Beras</button>
  <button class="filter-btn" onclick="filterProduct('Mie Instan')">Mie Instan</button>
</div>

<div class="product-grid" id="productContainer">
  {% for item in site.data.harga %}
  <div class="product-card" data-category="{{ item.kategori }}">
    <div class="product-badge">{{ item.stok }}</div>
    <div class="product-image">
      <img src="{{ '/assets/images/' | relative_url }}{{ item.foto }}" 
     alt="{{ item.produk }}" 
     onerror="this.src='https://placehold.co/600x400?text=Gambar+Kosong'">
    </div>
    <div class="product-info">
      <span class="category">{{ item.kategori }}</span>
      <h3>{{ item.produk }}</h3>
      <div class="price-tag">
        <span class="currency">Rp</span>
        <span class="amount">{{ item.harga }}</span>
        <span class="unit">/{{ item.satuan }}</span>
      </div>
      <a href="https://wa.me/{{ site.phone }}?text=Halo,%20saya%20ingin%20pesan%20{{ item.produk }}" class="buy-btn">
         Beli Sekarang
      </a>
    </div>
  </div>
  {% endfor %}
</div>

<section class="order-steps">
  <div class="container">
    <h2 class="section-title">Cara Pemesanan</h2>
    <div class="steps-container">
      <div class="step">
        <div class="step-num">1</div>
        <p>Pilih produk & cek harga harian</p>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <p>Klik tombol WA untuk konfirmasi stok</p>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <p>Lakukan pembayaran (Transfer/COD*)</p>
      </div>
      <div class="step">
        <div class="step-num">4</div>
        <p>Barang dikirim ke lokasi Anda</p>
      </div>
    </div>
  </div>
</section>

<section class="retail-price-section">
  <div class="container">
    <h2 class="section-title">Daftar Harga Retail</h2>
    <p style="text-align: center; color: var(--gold-light); margin-top: -30px; margin-bottom: 40px;">Update harian untuk pembelian eceran / satuan</p>
    
    <div class="table-container">
      <table class="retail-table">
        <thead>
          <tr>
            <th>Komoditas</th>
            <th>Varian</th>
            <th>Harga Retail</th>
            <th>Satuan</th>
          </tr>
        </thead>
        <tbody>
          {% for item in site.data.harga %}
          <tr>
            <td class="prod-name">{{ item.produk }}</td>
            <td>{{ item.kategori }}</td>
            <td class="gold-text">Rp {{ item.harga }}</td>
            <td>{{ item.satuan }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="shipping-info">
  <div class="container">
    <h2 class="section-title">Logistik & Pengiriman</h2>
    <div class="shipping-grid">
      <div class="shipping-item">
        <div class="shipping-icon">🚚</div>
        <h3>Armada Sendiri</h3>
        <p>Pengiriman cepat & aman menggunakan armada internal khusus untuk area Bandung dan sekitarnya.</p>
      </div>
      
      <div class="shipping-item">
        <div class="shipping-icon">📦</div>
        <h3>Packing Premium</h3>
        <p>Standar pengemasan tinggi untuk menjaga kesegaran telur dan kualitas beras hingga ke tangan Anda.</p>
      </div>

      <div class="shipping-item">
        <div class="shipping-icon">🕒</div>
        <h3>Pengiriman Terjadwal</h3>
        <p>Pesan hari ini sebelum jam 15.00 WIB untuk jadwal pengiriman di hari berikutnya (Next Day).</p>
      </div>

      <div class="shipping-item">
        <div class="shipping-icon">📍</div>
        <h3>Jangkauan Luas</h3>
        <p>Melayani pengiriman skala besar ke agen, pasar, hingga restoran di seluruh wilayah jangkauan kami.</p>
      </div>
    </div>
  </div>
</section>

<section class="logistics-details">
  <div class="container-split">
    
    <div class="map-section">
      <h3 class="gold-text">Lokasi Pusat Distribusi</h3>
      <div class="map-wrapper">
        <iframe 
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d126920.27928674!2d106.789184!3d-6.229728!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f3e945e3fa87%3A0x60c88514800877!2sJakarta%20Selatan!5e0!3m2!1sid!2sid!4v1700000000000!3m2!1sid!2sid" 
          width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy">
        </iframe>
      </div>
    </div>

    <div class="faq-section">
      <h3 class="gold-text">Pertanyaan Umum (FAQ)</h3>
      <div class="faq-container">
        <details>
          <summary>Berapa minimal order untuk pengiriman?</summary>
          <p>Minimal order adalah 20 Ikat untuk produk telur dan 5 karung untuk produk beras untuk mendapatkan gratis ongkir area Bandung.</p>
        </details>
        <details>
          <summary>Apakah melayani pengiriman luar kota?</summary>
          <p>Ya, untuk luar kota kami bekerja sama dengan ekspedisi cargo terpercaya dengan tarif kompetitif.</p>
        </details>
        <details>
          <summary>Kapan jadwal pengiriman dilakukan?</summary>
          <p>Pengiriman dilakukan setiap Senin - Sabtu. Pesanan yang masuk sebelum jam 15.00 akan dikirim keesokan paginya.</p>
        </details>
      </div>
    </div>

  </div>
</section>

<script>
function filterProduct(category) {
    const cards = document.querySelectorAll('.product-card');
    const btns = document.querySelectorAll('.filter-btn');
    
    // Atur status aktif tombol
    btns.forEach(btn => {
        btn.classList.remove('active');
        if(btn.innerText.toLowerCase() === category.toLowerCase() || (category === 'all' && btn.innerText === 'Semua')) {
            btn.classList.add('active');
        }
    });

    // Filter kartu
    cards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
            card.style.display = 'block';
            setTimeout(() => card.style.opacity = '1', 10);
        } else {
            card.style.opacity = '0';
            setTimeout(() => card.style.display = 'none', 300);
        }
    });
}

const track = document.querySelector('.slider-track');
const slides = document.querySelectorAll('.slide');
const nextBtn = document.querySelector('.slide-arrow.next');
const prevBtn = document.querySelector('.slide-arrow.prev');
const dots = document.querySelectorAll('.dot');
let currentSlide = 0;
let autoTimer;

function updateSlide() {
  if (!track) return;
  track.style.transform = 'translateX(' + (-currentSlide * 100) + '%)';
  dots.forEach((d,i)=>{ if(i===currentSlide){ d.classList.add('active'); } else { d.classList.remove('active'); } });
}
function nextSlide() {
  currentSlide = (currentSlide + 1) % slides.length;
  updateSlide();
}
function prevSlide() {
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  updateSlide();
}
function startAuto() {
  stopAuto();
  autoTimer = setInterval(nextSlide, 4000);
}
function stopAuto() {
  if (autoTimer) clearInterval(autoTimer);
}
if (nextBtn && prevBtn) {
  nextBtn.addEventListener('click', ()=>{ stopAuto(); nextSlide(); startAuto(); });
  prevBtn.addEventListener('click', ()=>{ stopAuto(); prevSlide(); startAuto(); });
}
dots.forEach(dot=>{
  dot.addEventListener('click', ()=>{
    stopAuto();
    const idx = parseInt(dot.getAttribute('data-index'));
    if (!isNaN(idx)) { currentSlide = idx; updateSlide(); startAuto(); }
  });
});
let startX = 0;
let isPointer = false;
const sliderEl = document.querySelector('.slider');
function onStart(e) {
  isPointer = true;
  stopAuto();
  startX = e.touches ? e.touches[0].clientX : e.clientX;
}
function onMove(e) {}
function onEnd(e) {
  if (!isPointer) return;
  const endX = e.changedTouches ? e.changedTouches[0].clientX : e.clientX;
  const diff = endX - startX;
  if (Math.abs(diff) > 50) { if (diff < 0) { nextSlide(); } else { prevSlide(); } }
  startAuto();
  isPointer = false;
}
if (sliderEl) {
  sliderEl.addEventListener('touchstart', onStart, { passive: true });
  sliderEl.addEventListener('touchend', onEnd, { passive: true });
  sliderEl.addEventListener('pointerdown', onStart);
  sliderEl.addEventListener('pointerup', onEnd);
}
updateSlide();
startAuto();
</script>
