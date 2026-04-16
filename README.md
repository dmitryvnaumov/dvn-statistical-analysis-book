# Stat Course Pilot

Двуязычный Quarto-проект для онлайн-книги по статистическому анализу.

## Structure

- `book/ru/` — русская книга
- `book/en/` — английская книга
- `slides/` — курс слайдов
- `shared/` — общие стили, библиография, изображения, `notebooks/common` и PDF-настройки
- `scripts/` — служебные скрипты

## Build

```bash
make help
make ru
make en
make ru-pdf
make en-pdf
make ru-notebook NOTEBOOK=probability_demo
make en-notebook NOTEBOOK=probability_demo
```

## Notes

- обе книги собираются через `lualatex`;
- после каждой главы идёт notebook-глава и карточка с переходом в companion notebook.
