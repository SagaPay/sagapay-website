import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Instead of global margin change, let's target the wrapper divs for those specific images by matching the image inside
# But CSS doesn't have parent selectors (except :has, which is okay but better is targeting the margin of the img itself)
# We can just add margin to the img elements

# Let's add margin-right to Reisespill and margin-left to Home & Interior
reisespill_block = r'(\.merchant-logo img\[src\*="logo-reisespill"\]\s*\{[^}]+transform:\s*scale\([^}]+\)\s*!important;\s*)(\})'
home_interior_block = r'(\.merchant-logo img\[src\*="logo-home-interior"\]\s*\{[^}]+transform:\s*scale\([^}]+\)\s*!important;\s*)(\})'

css = re.sub(reisespill_block, r'\1margin-right: 60px !important;\n\2', css)
css = re.sub(home_interior_block, r'\1margin-left: 60px !important;\n\2', css)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Spacing added")
