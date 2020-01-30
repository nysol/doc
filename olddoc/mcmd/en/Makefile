
all: index
	platex mcmd2.tex && dvipdfmx mcmd2.dvi

index:
	cd examples && ruby runall.rb
	platex mcmd2.tex && makeindex mcmd2
clean:
	rm -f *.aux
	rm -f *.dvi
	rm -f *.idx
	rm -f *.log
	rm -f *.out
	rm -f *.toc

