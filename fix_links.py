import glob

html_files = glob.glob("*.html")
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Oppdater fra epost-lenke til kontakt.html
    new_content = content.replace('href="mailto:support@sagapay.no"', 'href="kontakt.html"')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)
            print(f"Updated links in: {filepath}")

print("All support links now navigate directly to kontakt.html")
