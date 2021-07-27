---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/scholar?hl=en&as_sdt=5%2C31&sciodt=0%2C31&cites=13754600401406655328&scipsc=&q=Christopher+Lutsko&btnG=}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
