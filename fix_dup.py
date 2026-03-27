with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

# Find the SECOND occurrence of products section
occurrences = []
for i, line in enumerate(lines):
    if '<section id="products" class="products-section">' in line:
        occurrences.append(i)

if len(occurrences) > 1:
    start_idx = occurrences[1] # The duplicate starts here
    
    # Find AI-KALKULATOR after start_idx
    for i in range(start_idx, len(lines)):
        if '<!-- AI-KALKULATOR SEKSJON -->' in line:
            pass # wait bug in my mind, line is the old variable...

    for i in range(start_idx, len(lines)):
        if '<!-- AI-KALKULATOR SEKSJON -->' in lines[i]:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    print(f"Removing lines from {start_idx} to {end_idx}")
    new_lines = lines[:start_idx] + lines[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Removal successful!")
else:
    print("Could not find start/end indices")
    print(f"start: {start_idx}, end: {end_idx}")
