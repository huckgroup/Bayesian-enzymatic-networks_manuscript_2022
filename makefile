# publish: bibliography.bib manuscript.md template.docx figures/*
# 	pandoc -s -o manuscript.docx --bibliography bibliography.bib manuscript.md --reference-doc=template.docx --filter pandoc-crossref --citeproc -L pagebreak.lua

publish: draft si

draft:  bibliography.bib manuscript.md template_draft.docx figures/*
	pandoc -s -o out/manuscript.docx --bibliography bibliography.bib manuscript.md --reference-doc=template_draft.docx --filter pandoc-crossref --citeproc -L pagebreak.lua
	pandoc -s -o out/manuscript.pdf --bibliography bibliography.bib manuscript.md --filter pandoc-crossref --citeproc -L pagebreak.lua
	
inverse: manuscript.docx
	pandoc -s -o output.md --track-changes manuscript.docx

si: bibliography.bib SI.md template_draft.docx figures/* data/* notebooks/* notebooks/diagnostics/* notebooks/pdfs/*
	pandoc -s -o out/SI.pdf --bibliography bibliography.bib SI.md --filter pandoc-crossref --citeproc --lua-filter=codeBlockToTable.lua  -L pagebreak.lua --lua-filter=scholarly-metadata.lua --lua-filter=author-info-blocks.lua --lua-filter=include-files.lua  

bibliography.bib: ~/phd/library/Library.bib manuscript.md figures/*
	pandoc --to bibexport.lua --bibliography ~/phd/library/Library.bib manuscript.md --filter pandoc-crossref --citeproc -L pagebreak.lua


