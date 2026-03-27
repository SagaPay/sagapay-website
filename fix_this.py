import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove merchant-5.png
html = re.sub(r'<div class="merchant-logo">\s*<img src="images/merchant-5\.png" alt="Delikate matgaver">\s*</div>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Increase reisespill scale
css = re.sub(r'(\[src\*="logo-reisespill"\]\s*\{\s*transform:\s*scale\()([\d\.]+)(\)\s*!important;\s*\})', r'\g<1>4.0\g<3>', css)

# Make sure it's big enough
if '4.0' not in css and 'logo-reisespill' in css:
    css = re.sub(r'\[src\*="logo-reisespill"\][^}]+}', '[src*="logo-reisespill"] { transform: scale(4.0) !important; }', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated index.html and styles.css")
