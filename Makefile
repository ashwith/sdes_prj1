default: output/143079021.html output/van_der_pol_eps.eps output/van_der_pol_init.eps
	cd source && pdflatex -shell-escape report.tex
	cd source && pdflatex -shell-escape report.tex
	cd source && bibtex report
	cd source && pdflatex -shell-escape report.tex
	cd source && pdflatex -shell-escape report.tex
	mv source/report.pdf output/143079021.pdf
	rm -fr source/report.aux source/report.out source/report.log
	rm -fr source/report.bbl source/report.blg
	rm -fr output/van_der_pol_eps-eps-converted-to.pdf
	rm -fr output/van_der_pol_init-eps-converted-to.pdf

output/143079021.html: output/animation.ogg
	cd source && bash genhtml.bash ../output/143079021.html ../output/animation.ogg

output/animation.ogg output/van_der_pol_eps.eps output/van_der_pol_init.eps: source/vanderpol.py
	$(info Creating images and animation. Please wait.)
	mkdir output
	cd source && python3 vanderpol.py

clean:
	rm -fr output

test: source/vanderpol.py
	pytest source/test_vanderpol.py
