![vaderLogo](resources/vader-logo.svg)

# PR Code Change Description:
![appRunAfter](resources/jedi_mind_probe_script.gif)

### frontend

### backend
1. running jedi_mind_probe_script.py will analyze sentiment of titles based on a filtered keywords and export a clean excel file with new columns based on VADER sentiment analysis

# Functional Impacts:
1. extract sentiment of titles using NLP

# QA Reminders:
1. I used the Spyder python IDE via the Anaconda-Navigator application to write, test, & execute the jedi_mind_probe_script.py file.
2. running jedi_mind_probe_script_tests.py will take 3-4 min to complete due to VADER sentiment analysis of article titles.

# Acceptance Criteria:
1. write an MVP that extracts sentiments of article titles based on a keyword
2. write a script that will export a clean excel file with new columns based on the sentiment analysis findings

### story reference:
https://github.com/enzo-dante/JediMindProbe

# Build Tests:

### python unit_tests
![testRun](resources/jedi_mind_probe_tests.gif)
### jest
n/a

### angular
n/a

# Before:
![appRunBefore](resources/jedi_mind_probe_script_before.gif)

# After:
![appRunAfter](resources/jedi_mind_probe_script.gif)

# Kanban Board:

### TO-DO

US0004-use tableau to visualize the VADER findings from the python exported excel file