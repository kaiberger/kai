#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright (C) 2017 Christian Berger <christian.berger@gu.se>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import bibtexparser

month = {'jan' : '01', 'feb' : '02', 'mar' : '03', 'apr' : '04', 'may' : '05', 'jun' : '06', 'jul' : '07', 'aug' : '08', 'sep' : '09', 'oct' : '10', 'nov' : '11', 'dec' : '12'}

def fixLatexString(input):
   s = str(input)
   s = s.replace("\\\"{a}", "ä")
   s = s.replace("\\\"{o}", "ö")
   s = s.replace("\\\"{u}", "ü")
   s = s.replace("\\\"{A}", "Ä")
   s = s.replace("\\\"{O}", "Ö")
   s = s.replace("\\\"{U}", "Ü")
   s = s.replace("\\\'{a}", "á")
   s = s.replace("\\\'{e}", "é")
   s = s.replace("\\\'{o}", "ó")
   s = s.replace("\\\'{u}", "ú")
   s = s.replace("\\&", "&")
   s = s.replace("\\ss{}", "ß")
   s = s.replace("\\_", "_")
   s = s.replace("\"", "")
   s = s.replace("\\", "")
   return s

with open('library.bib') as bibtex_file:
    bibtex_str = bibtex_file.read()

bib_database = bibtexparser.loads(bibtex_str)

#print bib_database.entries

for entry in bib_database.entries:
    # Skip entries that don't belong to me.
    if "keyword" in entry:
        if "DE" in entry["keyword"]:
            continue
        if "reviewed" not in entry["keyword"]:
            continue
        if "MINE" not in entry["keyword"]:
            continue
    else:
        continue

    print "Processing " + entry["ID"]

    file = open("content/publication/" + entry["ID"] + ".md", "w")
    file.write("+++\n")
    file.write("title = \"" + fixLatexString(entry["title"]) + "\"\n")
    if "abstract" in entry:
        file.write("abstract = \"" + fixLatexString(entry["abstract"]) + "\"\n")
    else:
        file.write("abstract = \"\"\n")
    file.write("abstract_short = \"\"\n")
    file.write("publication_short = \"\"\n")
    if "booktitle" in entry:
        file.write("publication = \"" + fixLatexString(entry["booktitle"]) + "\"\n")
    elif "journal" in entry:
        file.write("publication = \"" + fixLatexString(entry["journal"]) + "\"\n")
    else:
        file.write("publication = \"\"\n")
    if "author" in entry:
        file.write("authors = [\"" + fixLatexString(entry["author"]) + "\"]\n")
    if "editor" in entry:
        file.write("editors = [\"" + fixLatexString(entry["editor"]) + "\"]\n")
    if "year" in entry and "month" in entry:
        file.write("date = \"" + entry["year"] + "-" + month[entry["month"]] + "-01" + "\"\n")
    else:
        file.write("date = \"" + entry["year"] + "-01-01" + "\"\n")
    file.write("image = \"\"\n")
    file.write("image_preview = \"\"\n")
    file.write("math = false\n")
    if "SELECTED" in entry["keyword"]:
        file.write("selected = true\n")
    else:
        file.write("selected = false\n")
    file.write("url_slides = \"\"\n")
    file.write("url_project = \"\"\n")
    file.write("url_code = \"\"\n")
    if "link" in entry:
        file.write("url_pdf = \"" + fixLatexString(entry["link"]) + "\"\n")
    else:
        file.write("url_pdf = \"\"\n")
    file.write("url_video = \"\"\n")
    file.write("url_dataset = \"\"\n")
    file.write("\n")
    file.write("+++\n")
    file.close()
