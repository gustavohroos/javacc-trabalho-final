JAVACC=javacc
JAVAC=javac
EXAMPLES=exFinal1.lug exFinal2.lug exFinal3.lug exFinal4.lug exFinal5.lug exFinal6.lug fibonacci.lug

all: programa $(EXAMPLES)

programa: Lugosi.java
	$(JAVAC) *.java

Lugosi.java: Lugosi_arvore_sintatica.jj
	$(JAVACC) Lugosi_arvore_sintatica.jj

$(EXAMPLES): programa
	java Lugosi $@

clean:
	rm -f *.java *.class traduzidos/*.py