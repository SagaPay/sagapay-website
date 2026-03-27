with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

if "/* Specific size boosts for text-heavy merchant logos */" in css:
    css = css.split("/* Specific size boosts for text-heavy merchant logos */")[0]

css += """/* Specific size boosts for text-heavy merchant logos */
.merchant-logo img[src*="merchant-2"] {
    max-height: 100px;
    transform: scale(1.3);
}

.merchant-logo img[src*="merchant-4"] {
    max-height: 50px !important; 
    transform: scale(0.9) !important; 
}

.merchant-logo img[src*="merchant-5"] {
    max-height: 100px;
    transform: scale(1.2);
}

.merchant-logo img[src*="merchant-3"] {
    width: 320px !important;
    max-width: 450px !important;
    max-height: 250px !important;
    transform: scale(2.5) !important;
}

.merchant-logo img[src*="merchant-2"]:hover { transform: scale(1.35); }
.merchant-logo img[src*="merchant-4"]:hover { transform: scale(0.95) !important; }
.merchant-logo img[src*="merchant-5"]:hover { transform: scale('.2.m; }
.merchant-logo img[src*="merchant-3"]:hover { transform: scale(2.55) !important; }
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css)
