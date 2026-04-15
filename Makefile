.DEFAULT_GOAL := help

QUARTO ?= quarto
PYTHON ?= $(HOME)/.pyenv/versions/3.12.2/envs/manim-env/bin/python
QUARTO_PYTHON ?= $(PYTHON)
MPLCONFIGDIR ?= $(CURDIR)/.make-tmp/mpl

export QUARTO_PYTHON
export MPLCONFIGDIR

RU_NOTEBOOKS := probability_demo poisson_gaussian_demo likelihood_demo fitting_demo intervals_demo feldman_cousins_demo hypothesis_tests_demo systematics_demo neutrino_cases_demo
EN_NOTEBOOKS := $(RU_NOTEBOOKS)

.PHONY: help check-env all books notebooks figures \
	pages-site \
	ru ru-html ru-pdf en en-html en-pdf \
	ru-notebooks en-notebooks \
	ru-notebook en-notebook clean clean-ru clean-en clean-notebooks clean-figures clean-cache

help: ## Показать цели сборки
	@printf '%s\n' 'Доступные цели:'
	@awk 'BEGIN {FS = ":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "  %-24s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@printf '\n%s\n' 'Отдельный notebook:'
	@printf '  make ru-notebook NOTEBOOK=probability_demo\n'
	@printf '  make en-notebook NOTEBOOK=probability_demo\n'

check-env: ## Проверить Quarto и manim-env
	@command -v "$(QUARTO)" >/dev/null || { echo "Не найден quarto: $(QUARTO)"; exit 1; }
	@test -x "$(PYTHON)" || { echo "Не найден Python: $(PYTHON)"; exit 1; }
	@mkdir -p "$(MPLCONFIGDIR)"

all: figures books ## Собрать фигуры и обе книги

books: ru en ## Собрать обе книги

pages-site: figures ru-html en-html ## Собрать локальный артефакт GitHub Pages в .make-tmp/pages-site
	scripts/assemble_pages_site.sh

ru: check-env ## Собрать русскую книгу целиком
	$(QUARTO) render ru

en: check-env ## Собрать английскую книгу целиком
	$(QUARTO) render en

ru-html: check-env ## Собрать HTML русской книги
	$(QUARTO) render ru --to html

ru-pdf: check-env ## Собрать PDF русской книги
	$(QUARTO) render ru --to pdf

en-html: check-env ## Собрать HTML английской книги
	$(QUARTO) render en --to html

en-pdf: check-env ## Собрать PDF английской книги
	$(QUARTO) render en --to pdf

figures: check-env ## Сгенерировать общие фигуры
	$(PYTHON) scripts/build_figures.py

ru-notebooks: check-env ## Пересобрать все русские ноутбуки как отдельные входы
	@for nb in $(RU_NOTEBOOKS); do \
	  scripts/render_notebook_standalone.sh ru $$nb; \
	done

en-notebooks: check-env ## Пересобрать все английские ноутбуки как отдельные входы
	@for nb in $(EN_NOTEBOOKS); do \
	  scripts/render_notebook_standalone.sh en $$nb; \
	done

ru-notebook: check-env ## Собрать один русский notebook: make ru-notebook NOTEBOOK=probability_demo
	@test -n "$(NOTEBOOK)" || { echo "Укажи NOTEBOOK=<slug>"; exit 1; }
	scripts/render_notebook_standalone.sh ru $(NOTEBOOK)

en-notebook: check-env ## Собрать один английский notebook: make en-notebook NOTEBOOK=probability_demo
	@test -n "$(NOTEBOOK)" || { echo "Укажи NOTEBOOK=<slug>"; exit 1; }
	scripts/render_notebook_standalone.sh en $(NOTEBOOK)

clean: clean-ru clean-en clean-notebooks clean-figures clean-cache ## Очистить артефакты сборки

clean-ru: ## Очистить артефакты русской книги
	rm -rf ru/_book ru/.quarto

clean-en: ## Очистить артефакты английской книги
	rm -rf en/_book en/.quarto

clean-notebooks: ## Очистить standalone-артефакты ноутбуков
	rm -rf ru/notebooks/*.html ru/notebooks/*.pdf ru/notebooks/*_files en/notebooks/*.html en/notebooks/*.pdf en/notebooks/*_files

clean-figures: ## Очистить figures/generated
	rm -rf figures/generated/*

clean-cache: ## Очистить временные кэши
	rm -rf .make-tmp
