SRC := source
OUT := output

TEXFILE := report.tex
PYFILE := vanderpol.py
FIGURES := $(OUT)/van_der_pol_eps.eps $(OUT)/van_der_pol_init.eps 
WEBPAGE := $(OUT)/143079021.html
REPORT := $(OUT)/143079021.pdf

PY := python3
VIDEO := $(OUT)/animation.ogg
TEX := pdflatex -shell-escape
HTML := bash genhtml.bash

all: $(REPORT)

$(REPORT): $(WEBPAGE) $(FIGURES) $(SRC)/$(TEXFILE)
	cd $(SRC) && $(TEX) $(TEXFILE)
	cd $(SRC) && bibtex $(basename $(TEXFILE))
	cd $(SRC) && $(TEX) $(TEXFILE)
	cd $(SRC) && $(TEX) $(TEXFILE)
	mv $(SRC)/report.pdf $(REPORT)

$(WEBPAGE): $(VIDEO)
	cd $(SRC) && $(HTML) ../$(WEBPAGE) ../$(VIDEO)

$(FIGURES) $(VIDEO): $(SRC)/vanderpol.py
	mkdir -p $(OUT)
	$(info Creating images and animation. Please wait.)
	cd $(SRC) && $(PY) $(PYFILE)
	rm -fr *.pyc

clean: cleantex
	rm -fr $(OUT)

cleantex:
	rm -fr $(SRC)/report.aux $(SRC)/report.out $(SRC)/report.log
	rm -fr $(SRC)/report.bbl $(SRC)/report.blg
	rm -fr $(OUT)/van_der_pol_eps-eps-converted-to.pdf
	rm -fr $(OUT)/van_der_pol_init-eps-converted-to.pdf

test: $(SRC)/vanderpol.py
	pytest $(SRC)/$(PYFILE)
	rm -fr *.pyc
