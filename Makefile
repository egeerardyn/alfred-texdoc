ZIP=zip
BINDIR=./bin

workflow:
	git archive --format=zip -o $(BINDIR)/TeXdoc.alfredworkflow HEAD

.PHONY: clean install

install:
	open $(BINDIR)/TeXdoc.alfredworkflow

clean:
	rm $(BINDIR)/*.alfredworkflow
