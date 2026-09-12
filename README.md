# chrislutsko.com

Source for Chris Lutsko's academic website, published with GitHub Pages.

## Local development

The site uses Jekyll and the AcademicPages theme.

```bash
bundle install
bundle exec jekyll serve
```

The local preview is available at `http://localhost:4000`.

## Content

- Main pages are in `_pages/`.
- PDFs and downloadable files are in `files/`.
- Site-wide settings are in `_config.yml`.
- Navigation is in `_data/navigation.yml`.
- Site-specific styles are at the end of `assets/css/main.scss`.

The underlying theme is derived from
[AcademicPages](https://github.com/academicpages/academicpages.github.io) and
[Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes).
