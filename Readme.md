van Der Pol Oscillator
=====================

This project explores the van Der Pol Oscillator. In order to build
the report and run the code you will need the following:

1. python 3.5
2. ipython 3.5 (to view and run the ipython notebook)
3. numpy
4. scipy
5. matplotlib
6. LaTeX (with the command pdflatex) with packages: graphicx, float, amsmath, hyperref
7. bibtex
8. The codec for ogg: libtheora (to generate the animation).
9. ffmpeg

To generate the report, simple run:

`make`

Everything that make generates is in the output directory. The report
is in 143079021.pdf, the animation is animation.ogg and the HTML
page with the animation is 143079021.html. Also generated are two
plots: van_der_pol_eps.eps and van_der_pol_init.eps
You can run the code tests by running

`make test`

Clean up the repository by running:

`make clean`

The latest version of this repository is always at:
https://github.com/ashwith/sdes_prj1
