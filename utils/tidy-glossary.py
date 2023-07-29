# tidy glosary
# runs through the glossary page and adds a aliggified ID to each term

import re

GLOSSARY_FILENAME = "docs/glossary.md"

DT_REGEX = re.compile(r'.*<dt\s*([^>]*)>\s*([^<,]+)((<br>|,)*[^<]*)?</dt>')

GLOSSARY_INDEX_START = "<!-- glossary index start -->"
GLOSSARY_INDEX_END = "<!-- glossary index end -->"

output_filename = "docs/new-glossary.md"

new_lines = []
glossary_entries = []

found_glossary_index_end = False
with open(GLOSSARY_FILENAME, "r") as glossary_md:
    while line := glossary_md.readline():
        if line.startswith(GLOSSARY_INDEX_START):
            while not found_glossary_index_end:
              found_glossary_index_end = glossary_md.readline().startswith(GLOSSARY_INDEX_END) 
        elif matches := re.match(DT_REGEX, line):
            term = matches.group(2)
            slug = term.lower().replace(" ", "-")
            glossary_entries.append((slug, term))
            extra_term = matches.group(3) or ""
            line =(f"<dt id=\"{slug}\">{term}{extra_term}</dt>\n")
        new_lines.append(line)

if not found_glossary_index_end:
    raise ValueError(f"Didn't find \"{GLOSSARY_INDEX_END}\" in {GLOSSARY_FILENAME}")

index_entries = [
  f"<li><a href=\"#{slug}\">{term.replace(' ', '&nbsp;')}</a></li>"
  for slug, term in glossary_entries
]

print(f"[ ] writing to {output_filename}...")
with open(output_filename, "w") as new_glossary_md:
  for line in new_lines:
      new_glossary_md.write(line)
      if line.startswith(GLOSSARY_INDEX_START):
          new_glossary_md.write('<ul class="glossary-index">\n')
          new_glossary_md.write("\n".join(index_entries))
          new_glossary_md.write('\n</ul>\n')
          new_glossary_md.write(GLOSSARY_INDEX_END)
    
print(f"[ ] total lines: {len(new_lines)}")

#print(index_entries)