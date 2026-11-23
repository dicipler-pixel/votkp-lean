#!/bin/sh
# SCRIPT: BUILD_WHAT_THE_PEEL_KEEPS_V1_2_3  (run from this folder)
set -e
HERE=$(pwd); mkdir -p build
for f in 00_front 01_opening 02_wall 03_criterion 04_dirac_time 05_two_votkps 06_ball 07_ledgers 08_elements 09_colour 10_lab 11_tests 12_decay 13_russell 14_ledger 15_prior_art 16_lean 17_tables 18_sources; do cat src/$f.md; printf '\n\n'; done > build/all.md
sed "s#\.\./figs/#$HERE/figs/#g" build/all.md > build/all_pdf.md
pandoc build/all_pdf.md -f markdown+tex_math_dollars+pipe_tables+implicit_figures -t latex --shift-heading-level-by=-1 --template=template.tex -o build/paper.tex
cd build; pdflatex -interaction=nonstopmode paper.tex > latex.log 2>&1 || true; pdflatex -interaction=nonstopmode paper.tex >> latex.log 2>&1 || true; cd ..
pandoc build/all_pdf.md -f markdown+tex_math_dollars+pipe_tables+implicit_figures -t html5 --mathml --standalone --embed-resources --metadata pagetitle="What the Peel Keeps v1.2.3" -H html_head.html -B html_title.html --toc --toc-depth=1 -o What_the_Peel_Keeps_v1_2_3_Jeromie_Beasley.html 2> build/html.log
cp build/paper.pdf What_the_Peel_Keeps_v1_2_3_Jeromie_Beasley.pdf
