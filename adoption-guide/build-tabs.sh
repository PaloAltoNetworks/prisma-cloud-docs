# Build Code & Build tabs
echo "Generate Code & Build tabs"
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/code-build-advanced.xml adoption-guide/code-build-advanced.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/code-build-foundational.xml adoption-guide/code-build-foundational.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/code-build-intermediate.xml adoption-guide/code-build-intermediate.adoc

# Build Deploy tabs
echo "Generate Deploy tabs"
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/deploy-advanced.xml adoption-guide/deploy-advanced.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/deploy-foundational.xml adoption-guide/deploy-foundational.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/deploy-intermediate.xml adoption-guide/deploy-intermediate.adoc

# Build Run tabs
echo "Generate Run tabs"
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/run-advanced.xml adoption-guide/run-advanced.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/run-foundational.xml adoption-guide/run-foundational.adoc
asciidoctor -r ~/.pandita/dita.rb -b dita -a experimental --out-file output/adoption-guide/run-intermediate.xml adoption-guide/run-intermediate.adoc

# Copy map file to output dir
echo "Copy fixed map file to output dir"
cp _adoption-guide.ditamap output/adoption-guide/

echo "Done"
