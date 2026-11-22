#!/bin/sh
cd /home/claude/paper_v12/build
for f in src/00_front.md src/01_opening.md src/02_wall.md src/03_criterion.md src/04_dirac_time.md src/05_two_votkps.md src/06_ball.md src/07_ledgers.md src/08_elements.md src/09_colour.md src/10_lab.md src/11_tests.md src/12_decay.md src/13_russell.md src/14_ledger.md src/15_prior_art.md src/16_lean.md src/17_tables.md src/18_sources.md; do cat $f; printf '\n\n'; done > all.md
sed 's#\.\./figs/#/home/claude/paper_v12/figs/#g' all.md > all_pdf.md
pandoc all_pdf.md -f markdown+tex_math_dollars+pipe_tables+implicit_figures -t latex --shift-heading-level-by=-1 --template=template.tex -o paper.tex
pdflatex -interaction=nonstopmode paper.tex > latex.log 2>&1
pdflatex -interaction=nonstopmode paper.tex >> latex.log 2>&1
pandoc all.md -f markdown+tex_math_dollars+pipe_tables+implicit_figures -t html5 --mathml --standalone --embed-resources --resource-path=/home/claude/paper_v12/build/src --metadata pagetitle="What the Peel Keeps v1.2" -H html_head.html -B html_title.html --toc --toc-depth=1 -o paper.html 2> html.log
