import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The user wants both sliders to be the same. 
# Let's extract the correct section from the top and apply to the bottom.
# First, let's find the products slider and replace it
# Or just use Python to replace merchant-4.png with logo-reisespill.png and add logo-home-interior.png

html = re.sub(r'<div class="merchant-logo">\s*<img src="images/merchant-4\.png" alt="Reisespill">\s*</div>', 
              '<div class="merchant-logo"><img src="images/logo-reisespill.png" alt="Reisespill"></div>\n                <div class="merchant-logo"><img src="images/logo-home-interior.png" alt="Home and interior"></div>', 
              html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed bottom carousel")
