#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "usage: $0 <ru|en> <notebook-slug>" >&2
  exit 1
fi

lang="$1"
slug="$2"

case "$lang" in
  ru) lang_header="ru-lang" ;;
  en) lang_header="en-lang" ;;
  *)
    echo "unsupported language: $lang" >&2
    exit 1
    ;;
esac

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
book_lang_dir="$root_dir/$lang/book"
source_qmd="$book_lang_dir/notebooks/$slug.qmd"

if [ ! -f "$source_qmd" ]; then
  echo "notebook not found: $source_qmd" >&2
  exit 1
fi

tmp_dir="$root_dir/.make-tmp/standalone-$lang-$slug"
mkdir -p "$tmp_dir"
rm -rf "$tmp_dir"/*

cp "$source_qmd" "$tmp_dir/index.qmd"

cat > "$tmp_dir/_metadata.yml" <<EOF
bibliography: ../../shared/bib/references.bib
lang: $lang

format:
  html:
    toc: true
    number-sections: true
    css: ../../shared/styles/book.css
    include-in-header:
      - ../../shared/html/mathjax.html
  pdf:
    pdf-engine: lualatex
    include-in-header:
      - ../../shared/latex/common-pdf.tex
      - ../../shared/latex/$lang_header.tex
EOF

(
  cd "$tmp_dir"
  quarto render index.qmd --to html --output "$slug.html"
  quarto render index.qmd --to pdf --output "$slug.pdf"
)

mv "$tmp_dir/$slug.html" "$book_lang_dir/notebooks/$slug.html"
mv "$tmp_dir/$slug.pdf" "$book_lang_dir/notebooks/$slug.pdf"

if [ -d "$tmp_dir/${slug}_files" ]; then
  rm -rf "$book_lang_dir/notebooks/${slug}_files"
  mv "$tmp_dir/${slug}_files" "$book_lang_dir/notebooks/${slug}_files"
fi
