#!/usr/bin/env bash
set -euo pipefail

root_dir="$(cd "$(dirname "$0")/.." && pwd)"
site_dir="$root_dir/.make-tmp/pages-site"

rm -rf "$site_dir"
mkdir -p "$site_dir"

cp "$root_dir/pages/index.html" "$site_dir/index.html"
cp "$root_dir/pages/robots.txt" "$site_dir/robots.txt"
touch "$site_dir/.nojekyll"

mkdir -p "$site_dir/ru" "$site_dir/en" "$site_dir/slides" "$site_dir/shared/figures"
cp -R "$root_dir/book/ru/_book/." "$site_dir/ru/"
cp -R "$root_dir/book/en/_book/." "$site_dir/en/"
cp -R "$root_dir/slides/_site/." "$site_dir/slides/"
cp -R "$root_dir/shared/figures/." "$site_dir/shared/figures/"
