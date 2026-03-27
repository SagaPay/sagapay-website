import re

with open('om-oss.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace variables with actual nice gradients
replacements = {
    'var(--gradient-1)': 'linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%)',
    'var(--gradient-2)': 'linear-gradient(135deg, #4E65FF 0%, #92EFFD 100%)',
    'var(--gradient-3)': 'linear-gradient(135deg, #11998e 0%, #38ef7d 100%)',
    'var(--gradient-4)': 'linear-gradient(135deg, #8E2DE2 0%, #4A00E0 100%)',
    'bg-gradient-1"': 'bg-gradient-1" style="background: linear-gradient(135deg, #0A2540 0%, #4E65FF 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);"',
    'bg-gradient-2"': 'bg-gradient-2" style="background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);"',
    'bg-gradient-3"': 'bg-gradient-3" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);"'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open('om-oss.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Inlined gradients.")
