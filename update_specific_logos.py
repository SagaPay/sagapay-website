import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make sure we have a CSS rule targeting specific logos
new_css_rules = """
/* Specific size boosts for text-heavy merchant logos */
.merchant-logo img[src*="merchant-3"], /* Home and interior */
.merchant-logo img[src*="merchant-2"], /* Lashly */
.merchant-logo img[src*="merchant-4"], /* Reisespill */
.merchant-logo img[src*="merchant-5"]  /* Delikate matgaver */ {
    max-height: 100px;
    transform: scale(1.3);
}

.merchant-logo img[src*="merchant-3"]:hover,
.merchant-logo img[src*="merchant-2"]:hover,
.merchant-logo img[src*="merchant-4"]:hover,
.merchant-logo img[src*="merchant-5"]:hover {
    transform: scale(1.35);
}
"""

if "Specific size boosts" not in css_content:
    with open('styles.css', 'a', encoding='utf-8') as f:
        f.write(new_css_rules)
