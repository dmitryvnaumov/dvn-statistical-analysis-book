# Stat Course Pilot

Двуязычный Quarto-проект для онлайн-книги по статистическому анализу.

## Structure

- `ru/book/` — русская книга
- `ru/slides/` — русские слайды
- `en/book/` — английская книга
- `en/slides/` — английские слайды
- `shared/` — общие стили, библиография, изображения, `notebooks/common` и PDF-настройки
- `scripts/` — служебные скрипты

## Build

```bash
make help
make ru
make en
make ru-slides
make en-slides
make ru-pdf
make en-pdf
make ru-notebook NOTEBOOK=probability_demo
make en-notebook NOTEBOOK=probability_demo
make pages-site
```

## Notes

- обе книги собираются через `lualatex`;
- после каждой главы идёт notebook-глава и карточка с переходом в companion notebook;
- сайт GitHub Pages собирается в `.make-tmp/pages-site` с деревом `ru/book`, `ru/slides`, `en/book`, `en/slides`.
