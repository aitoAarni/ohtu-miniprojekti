# Initial concept 

Possible fields:

@InProceedings{citekey,
  author       = "",
  title        = "",
  booktitle    = "",
  year         = "",
  editor       = "",
  volume       = "",
  number       = "",
  series       = "",
  pages        = "",
  month        = "",
  address      = "",
  organization = "",
  publisher    = "",
  note         = "",
  annote       = ""
}

key = citekey

types:
Article
Book
InProceedings


article An article from a journal or magazine. Required fields: author, title,
journal, year. Optional fields: volume, number, pages, month, note.



book A book with an explicit publisher. Required fields: author or editor,
title, publisher, year. Optional fields: volume or number, series,
address, edition, month, note.

## ARTICLE
**required**
- author
- title
- journal
- year

**optional**
- volume or number
- series
- address
- edition
- month
- note


## BOOK
**required**
- author or editor
- title
- publisher
- year

**optional**
- volume or number
- series
- address
- edition
- month
- note 


## INITIAL CONCEPT
- one table for data with the upformentioned fields. Db-check for not null on required fields
- PRIMARY KEY (INTEGER ALIAS)	
- 
