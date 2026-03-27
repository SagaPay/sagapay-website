import os
import glob
import re

html_files = glob.glob("*.html")

for filepath in html_files:
    with open(filepath, 'r') as file:
        content = file.read()

    # Modify all `#sales` or `#contact` or `hei@sagapay.no` occurrences 
    # to mailto:support@sagapay.no
    content = content.replace('href="#sales"', 'href="mailto:support@sagapay.no"')
    content = content.replace('href="#contact"', 'href="mailto:support@sagapay.no"')
    content = content.replace('href="mailto:hei@sagapay.no"', 'href="mailto:support@sagapay.no"')
    content = content.replace('hei@sagapay.no', 'support@sagapay.no')

    with open(filepath, 'w') as file:
        file.write(content)

print("Global string replacements complete.")
