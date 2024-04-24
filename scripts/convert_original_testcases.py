#!/usr/bin/env python3.10

from os import walk, makedirs
from os.path import dirname, abspath, join
import re


ROOT_DIR = dirname(dirname(abspath(__file__)))

TEST_CASE_DIR = join(ROOT_DIR, "src", "03_test_cases")


def main():
    
    reg1 = re.compile(r"<td>\s*<i>([^<>]*)</i>(?:\s*-\s*<i>([^<>]*)</i>)?(?:[^\(]*\(([^\)]*)\))?")
    
    for (_, dirnames, _) in walk(TEST_CASE_DIR):
        for d in dirnames:
            for (dirpath, _, filenames) in walk(join(TEST_CASE_DIR, d)):
                for f in filenames:
                    iname = join(dirpath, f)
                    odir = join(ROOT_DIR, "src", "03_test_cases_mod", d) 
                    oname = join(odir, f) 
                    with open(iname, "r") as ifile:
                        makedirs(odir, exist_ok = True)
                        with open(oname, "w") as ofile:
                            tablestart = False
                            rowid = 0
                            reqs = [
                                [None, None, None],
                                [None, None, None]
                            ]
                            stepbystep_exists = False
                            assessment_exists = False
                            for line in ifile:
                                if "**Remediation**" in line:
                                    if not stepbystep_exists:
                                        ofile.write("**Step-By-Step Execution**\n\nToDo\n\n")
                                        stepbystep_exists = True
                                    ofile.write(line)
                                elif "**References**" in line:
                                    if not assessment_exists:
                                        ofile.write("**Assessment**\n\nToDo\n\n")
                                        assessment_exists = True
                                    ofile.write(line)
                                elif "**Required Access Levels**" in line:
                                    ofile.write("\n**Requirements**\n")
                                elif "**Step-By-Step Execution**" in line:
                                    stepbystep_exists = True
                                    ofile.write(line)
                                elif "**Assessment**" in line:
                                    assessment_exists = True
                                    ofile.write(line)
                                elif '<table' in line:
                                    tablestart = True
                                    rowid = 0
                                elif '<td>' in line:
                                    m = reg1.search(line)
                                    if m:
                                        if rowid < 2:
                                            reqs[rowid][0] = m.group(1)
                                            reqs[rowid][1] = m.group(2)
                                            reqs[rowid][2] = m.group(3)
                                            rowid += 1
                                        else:
                                            print(f"Error rowid = {rowid}")
                                    else:
                                        print(f"Error: {line}")
                                elif '</table>' in line:
                                    if reqs[0][1] is None:
                                        str1 = reqs[0][0]
                                    else:
                                        str1 = reqs[0][0] + " - " + reqs[0][1]
                                    if reqs[1][1] is None:
                                        str2 = reqs[1][0]
                                    else:
                                        str2 = reqs[1][0] + " - " + reqs[1][1]
                                    txt = f"""| Requirement          | Level        | Notes |
| -------------------- | ------------ | ----- |
| Physical Access      | {str1} | {reqs[0][2] if reqs[0][2] else ""} |
| Authorization Access | {str1} | {reqs[1][2] if reqs[1][2] else ""} |
| Data Security        | DS1 - DS4    |  ToDo |
| Security Impact      | SI1 - SI4    |  ToDo |
| Verification Level   | VL1 - VL4    |  ToDo |
| Firmware Type        | eLinux / SBB |  ToDo |
"""
                                    print(txt)
                                    ofile.write(txt)
                                elif ('<tr' in line
                                      or '<th' in line
                                      or '</tr>' in line):
                                    pass
                                else:
                                    ofile.write(line)




main()
