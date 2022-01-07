publish: bibliography.bib manuscript.md template.docx figures/*
	pandoc -s -o manuscript.docx --bibliography bibliography.bib manuscript.md --reference-doc=template.docx --filter pandoc-crossref --citeproc -L pagebreak.lua

draft:bibliography.bib manuscript.md template_draft.docx figures/*
	pandoc -s -o manuscript.docx --bibliography bibliography.bib manuscript.md --reference-doc=template_draft.docx --filter pandoc-crossref --citeproc -L pagebreak.lua

inverse: manuscript.docx
	pandoc -s -o output.md --track-changes manuscript.docx