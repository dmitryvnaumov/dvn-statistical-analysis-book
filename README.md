# Stat Course Pilot

Двуязычный Quarto-проект для онлайн-книги по статистическому анализу.

## Structure

- `ru/` — русская книга
- `en/` — английская книга
- `shared/` — общие стили, библиография и PDF-настройки
- `figures/` — статические и генерируемые иллюстрации
- `data/` — исходные и подготовленные данные
- `scripts/` — служебные скрипты
- `archive/` — старые версии структуры, сохранённые отдельно

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

По умолчанию сборка использует Python из `manim-env`.

## Notes

- обе книги собираются через `lualatex`;
- языковые настройки PDF вынесены в `shared/latex/` по мотивам `dvn.sty`;
- после каждой главы идёт notebook-глава и карточка с переходом в companion notebook.
