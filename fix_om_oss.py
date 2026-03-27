import re

with open("om-oss.html", "r") as f:
    html = f.read()

pattern = re.compile(
    r'(<div class="nettbetaling-hero-img-container"[^>]*>).*?(</div>\s*</div>\s*</section>)', 
    re.DOTALL
)

replacement = r'''\1
                <img src="images/dashboard.png" alt="Sagapay Dashboard" style="width: 100%; max-width: 500px; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.1);">
            </div>
        </div>
    </section>'''

new_html, num_subs = pattern.subn(replacement, html, count=1)

if num_subs > 0:
    with open("om-oss.html", "w") as f:
        f.write(new_html)
    print("Successfully replaced heroine image in om-oss.html")
else:
    print("Match not found in om-oss.html!")

