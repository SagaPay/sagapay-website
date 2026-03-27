import re

with open("styles.css", "r", encoding="utf-8") as f:
    css = f.read()

split_str = "/* Specific size boosts for text-heavy merchant logos */"
if split_str in css:
    css = css.split(split_str)[0]

new_css = """/* Specific size boosts for text-heavy merchant logos */
.merchant-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 150px; 
    margin: 0 20px; 
}

/* Base-størrelsen før zoom */
.merchant-logo img[src*="merchant-2"],
.merchant-logo img[src*="merchant-3"],
.merchant-logo img[src*="merchant-4"],
.merchant-logo img[src*="merchant-5"] {
    width: auto !important;
    height: 70px !important; 
    max-height: none !important;
    max-width: none !important;
    object-fit: contain !important;
}

/* Lashly */
.merchant-logo img[src*="merchant-2"] {
    transform: scale(2.0) !important; 
}

/* Home & Interior - FORSTORRET til vanvittige 5.5 */
.merchant-logo img[src*="merchant-3"] {
    transform: scale(5.5) !important; 
}

/* Reisespill */
.merchant-logo img[src*="merchant-4"] {
    transform: scale(1.1) !important; 
}

/* Delikate Matgaver */
.merchant-logo img[src*="merchant-5"] {
    transform: scale(1.0) !important; 
}


/* Hover effects */
.merchant-logo img[src*="merchant-2"]:hover { transform: scale(2.1) !important; }
.merchant-logo img[src*="merchant-3"]:hover { transform: scale(5.6) !important; }
.merchant-logo img[src*="merchant-4"]:hover { transform: scale(1.2) !important; }
.merchant-logo img[src*="merchant-5"]:hover { transform: scale(1.1) !important; }
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css + new_css)
