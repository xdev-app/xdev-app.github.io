---
layout: default
title: Blog
---

<section class="blog-list">
  <h2 class="section-title">Artikel Terbaru</h2>
  <div class="posts">
    {% for post in site.posts %}
    <article class="post-card">
      <h3 class="post-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p class="post-meta">{{ post.date | date: "%-d %B %Y" }}</p>
      {% if post.excerpt %}
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 160 }}</p>
      {% endif %}
      <a class="read-more" href="{{ post.url | relative_url }}">Baca Selengkapnya</a>
    </article>
    {% endfor %}
  </div>
</section>
