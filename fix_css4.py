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
    min-width: 320px; /* Mer plass igjen for å fordele bredden pent mellom gigantene */
}

/* Base styles for å overstyre tidligere låste høyder/bredder */
.merchant-logo img[src*="merchant-2"],
.merchant-logo img[src*="merchant-3"],
.merchant-logo img[src*="merchant-4"],
.merchant-logo img[src*="merchant-5"] {
    width: auto !important;
    height: auto !important;
    max-height: none !important;
    max-width: none !important;
    transform: none !important;
}

/* Lashly - Vokst frem til å se stor ut */
.merchant-logo img[src*="merchant-2"] {
    height: 155px !important; 
}

/* Home & Interior - Gjort gigantisk for å oppveie store hvite felter i bildet */
.merchant-logo img[src*="merchant-3"] {
    height: 200px !important; 
}

/* Reisespill - Jekket opp til behagelig "komplett" størrelse */
.merchant-logo img[src*="merchant-4"] {
    height: 105px !important; 
}

/* Delikate Matgaver - Din mal (denne forblir uendret) */
.merchant-logo img[src*="merchant-5"] {
    height: 100px !important; 
}

/* Hover effects (skalerer pent opp ved mus-over) */
.merchant-logo img[src*="merchant-2"]:hover,
.merchant-logo img[src*="merchant-3"]:hover,
.merchant-logo img[src*="merchant-4"]:hover,
.merchant-logo img[src*="merchant-5"]:hover {
    transform: scale(1.05) !important;
}
"""

with open("styles.css", "w", encoding="utf-8") as f:
    f.write(css + new_css)
