# Build the manuscript: make (requires a TeX distribution with latexmk and amsart).
seed_bsd.pdf: seed_bsd.tex refs.bib sections/*.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error seed_bsd.tex
clean:
	latexmk -C
