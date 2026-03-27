import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Reisespill: normal scale 5.0, hover 5.1
css = re.sub(r'\[src\*="logo-reisespill"\]\s*\{\s*transform:\s*scale\([\d\.]+\)', r'[src*="logo-reisespill"] { transform: scale(5.0)', css)
css = re.sub(r'\[src\*="logo-reisespill"\]:hover\s*\{\s*transform:\s*scale\([\d\.]+\)', r'[src*="logo-reisespill"]:hover { transform: scale(5.1)', css)

# Make sure logo-home-interior hover matches normal + 0.1
normal_home_inner = re.search(r'\[src\*="logo-home-interior"\]\s*\{\s*transform:\s*scale\(([\d\.]+)\)', css)
if normal_home_inner:
    val = float(normal_home_inner.group(1))
    css = re.sub(r'\[src\*="logo-home-interior"\]:hover\s*\{\s*transform:\s*scale\([\d\.]+\)', f'[src*="logo-home-interior"]:hover {{ transform: scale({val + 0.1})', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Hover fixed")
