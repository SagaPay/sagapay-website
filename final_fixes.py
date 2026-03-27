import glob
import re
import os

print("Starting fixes...")

# 1. Fix contact links in all HTML files
html_files = glob.glob('*.html')
for f_name in html_files:
    try:
        with open(f_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'href="#contact"' in content:
            new_content = content.replace('href="#contact"', 'href="mailto:support@sagapay.no"')
            if new_content != content:
                with open(f_name, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed #contact in {f_name}")
    except Exception as e:
        print(f"Error processing {f_name}: {e}")

# 2. Remove transform and animation from om-oss.html
try:
    with open('om-oss.html', 'r', encoding='utf-8') as f:
        osm_content = f.read()
        
    # We want to remove standard strings like:
    # transform: translateX(-10%); animation: float-bounce 6s ease-in-out infinite;
    # We can use regex to remove anything matching `transform: translateX(...);` and `animation: float-bounce...;`
    # Also reverse optionally on the animation
    
    new_osm = re.sub(r'transform:\s*translateX\([^)]+\);\s*animation:\s*float-bounce[^;]+;', '', osm_content)
    
    if new_osm != osm_content:
        with open('om-oss.html', 'w', encoding='utf-8') as f:
            f.write(new_osm)
        print("Fixed om-oss.html float-box styles")
    else:
        print("No transform/animation matched in om-oss.html.")
        
except Exception as e:
    print(f"Error processing om-oss.html: {e}")

print("Done!")
