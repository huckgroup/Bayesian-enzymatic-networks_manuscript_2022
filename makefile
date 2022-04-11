si: bibliography.bib SI.md figures/* data/* notebooks/* notebooks/diagnostics/*
	pandoc -s -o out/SI.pdf --bibliography bibliography.bib SI.md --filter pandoc-crossref --citeproc --lua-filter=codeBlockToTable.lua  -L pagebreak.lua --lua-filter=scholarly-metadata.lua --lua-filter=author-info-blocks.lua --lua-filter=include-files.lua  
