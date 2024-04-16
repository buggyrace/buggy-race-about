from enum import Enum
import re
from os import path

#  * before running this script... best to have everything up-to-date in git
#  * then you can see what it's changed, and revert if necessary
#
# +++ SCRIPT CHANGES MARKDOWN FILES IN docs/customise SO BE CAREFUL +++
#
# Run this from root, e,g, python3 src/custom-util.py
# You'll need an input file containing the markdown produced by the race server:
# go to https://<your-race-server>/admin/config-docs-helper
#
# >  Note:
# >  If you get a 404 there (after you're logged in as staff!), make sure
# >  the ENV setting for that server _IS_DOCS_HELPER_PAGE_ENABLED is set to 1.
#
# ...and copy that into a file (the default is src/input.txt). Then run this
# script, which will replace the existing tables of config settings in the
# "customise" section of the docs.
# You probably want to commit those changes (once you've checked they're OK!)
# and push it up to https://github.com/buggyrace/buggy-race-server if you're
# updating the public "official" docs.

DEFAULT_INPUT_FNAME = "src/input.txt"

class ConfigGroupNames(str, Enum):
    AUTH = "auth"
    GITHUB = "github"
    ORG = "org"
    PROJECT = "project"
    RACES = "races"
    SERVER = "server"
    SOCIAL = "social"
    TASKS = "tasks"
    TECH_NOTES = "tech_notes"
    USERS = "users"

### skip social because the manual description is better than the automated one
SKIP_UPDATE = [ConfigGroupNames.SOCIAL]

config_detail_lines = {}

input_fname = input(f"Filename containing content from /admin/config-docs-helper? (default is {DEFAULT_INPUT_FNAME}) ") or DEFAULT_INPUT_FNAME
with open(input_fname) as input_file:
    line = input_file.readline()
    while line:
        if re.match(r"^\s*---+\s*$", line):
            line = input_file.readline()
            if m := re.match(r"# (\S.*\S+)", line):
                section_name = m.group(1).lower().replace(" ", "-")
                line = input_file.readline()
                if not re.match(r"^\s*---+\s*$", line):
                    raise ValueError("expected section title between lines of dashes")
                print(f"[ ] OK section is {section_name}")
                config_detail_lines[section_name] = []
                line = input_file.readline()
                while line and not re.match(r"^\s*---+\s*$", line):
                    config_detail_lines[section_name].append(line)
                    line = input_file.readline()
                print(f"[ ]   {section_name} has {len(config_detail_lines[section_name])} lines")
            elif re.match(r".*\S", line):
                raise ValueError("Unexpected: missing ----/# section/---- structure")
        else:
            line = input_file.readline()
print(f"[ ] done: finished reading {input_fname}")

for group_name in config_detail_lines:
    if group_name in SKIP_UPDATE:
        print(f"[-] skipping {group_name} because it's in the SKIP_UPDATE list")
        continue
    group_md_filename = f"docs/customising/{group_name}.md"
    if not path.exists(group_md_filename):
        raise FileNotFoundError(f"can't find {group_md_filename}")
    new_lines = []
    with open(group_md_filename) as md_file:
        is_adding = True
        while md_line := md_file.readline():
            # ## Config settings
            if is_adding:
                if re.match(r"## Config settings.*", md_line):
                    is_adding = False
                    settings = config_detail_lines[group_name]
                    for new_setting_line in settings:
                        new_lines.append(new_setting_line)
            else:
                if re.match(r"\s?---.*", md_line):
                    is_adding = True
            if is_adding:
                new_lines.append(md_line)
    with open(group_md_filename, "w") as new_md_file:
        print(f"[ ] updating {group_md_filename} with latest config settings")
        for new_line in new_lines:
            new_md_file.write(new_line) # already have newline ending

