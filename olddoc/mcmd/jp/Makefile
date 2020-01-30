
all: index
	platex mcmd.tex && dvipdfmx mcmd.dvi

index:
	cd examples && ruby runall.rb
	platex mcmd.tex && makeindex mcmd
clean:
	rm -f *.aux
	rm -f *.dvi
	rm -f *.idx
	rm -f *.log
	rm -f *.out
	rm -f *.toc

