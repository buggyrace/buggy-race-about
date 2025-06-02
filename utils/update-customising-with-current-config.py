from enum import Enum
import re
from os import path

#-------------------------------------------------------------------------------
#
#  Updates documentation with settings text downloaded from race server
#  ====================================================================
#
#  * Before running this script... best to have everything up-to-date in git
#  * then you can see what it's changed, and revert if necessary
#
#  +++ SCRIPT CHANGES MARKDOWN FILES IN docs/customise SO BE CAREFUL +++
#
#  Run this from root, e,g, python3 src/custom-util.py
#  You'll need an input file containing the markdown from the race server:
#  go to https://<your-race-server>/admin/config-docs-helper and click the
#  "download text" button.
#
#  >  Note:
#  >  If you get a 404 there (after you're logged in as staff!), make sure
#  >  the ENV setting for that server _IS_DOCS_HELPER_PAGE_ENABLED is set to 1.
#
#  ...and copy that into a file (the default is config-settings-for-docs.txt in
#  the src/ directory). Then run this script, which will replace the existing
#  tables of config settings in the "customise" section of the docs, and update
#  the current server version. (There's interaction on the command line, so
#  read the prompts). You probably want to commit those changes (once you've
#  checked they're OK!) and (if you're updating the public "official" docs)
#  push it up to https://github.com/buggyrace/buggy-race-server
#
#-------------------------------------------------------------------------------

DEFAULT_INPUT_FNAME = "src/config-settings-for-docs.txt"

class ConfigGroupNames(str, Enum):
    AUTH = "auth"
    EDITOR = "editor"
    LINKS = "links"
    ORG = "org"
    PROJECT = "project"
    RACES = "races"
    REMOTE = "remote"
    SERVER = "server"
    TASKS = "tasks"
    TECH_NOTES = "tech_notes"
    USERS = "users"
    VCS = "vcs"

### can nominate groups/sections to skip... currently none
### (but it ised to be links because the manual description was better than the
### automated one; since changes the output of the helper so this isn't so
SKIP_UPDATE = [] # empty now; used to be: [ConfigGroupNames.LINKS]

config_detail_lines = {}
source_version = None

input_fname = input(
    "[?] Filename containing content from <your-race-server>/admin/config-docs-helper?\n"
    f"[default: {DEFAULT_INPUT_FNAME}] "
) or DEFAULT_INPUT_FNAME
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
            if matches := re.match(r"<<\s*VERSION:\s*\"([^\"]+)\"\s*>>", line):
                source_version = matches.group(1)
                print(f"[ ] source version detected is \"{source_version}\"")
                if source_version.endswith("dev"):
                    source_version = source_version[:-3]
                source_version = input(
                    "[?] Update version number in docs? "
                    f"(default is {source_version}, enter another string, "
                    f" or \"no\" to prevent) ") or source_version
            line = input_file.readline()
print(f"[ ] done: finished reading {input_fname}")

if source_version:
    source_version = source_version.strip()
    if source_version.lower() == "no":
        source_version = None
    else:
        config_filename = "_config.yml"
        if not path.exists(config_filename):
            raise FileNotFoundError(f"can't find {config_filename}")
        lines = []
        with open(config_filename) as config_file:
            while line := config_file.readline():
                if line.startswith("  server_version:"):
                    line = f"  server_version: {source_version}"
                lines.append(line)
        print(f"[ ] updating {config_filename} with server version: {source_version}")
        print("[ ]    (note: Jekyll in watch mode needs restart to pick up config changes)")
        with open(config_filename, "w") as new_config_file:
            for line in lines:
                new_config_file.write(line)

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

