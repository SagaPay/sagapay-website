import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Erstatt manuelt inni fila for å være safe. Fjerner alt inni 'ticker-slide'
# og legger inn den oppdaterte listen.

split_str = """<div class="ticker-slide merchant-slide">"""

if split_str in html:
    chunks = html.split(split_str)
    
    new_html = chunks[0]
    
    # Rebuild slide 1
    new_html += split_str + """
                <div class="merchant-logo"><img src="images/merchant-2.png" alt="Lashly"></div>
                <div class="merchant-logo"><img src="images/merchant-diamanter.png" alt="Diamanter"></div>
                <div class="merchant-logo"><img src="images/merchant-sinocrack.png" alt="Sinorack"></div>
                <div class="merchant-logo"><img src="images/merchant-5.png" alt="Delikate matgaver"></div>
                <div class="merchant-logo"><img src="images/logo-reisespill.png" alt="Reisespill"></div>
                <div class="merchant-logo"><img src="images/logo-home-interior.png" alt="Home and interior"></div>
            </div>
            <!-- Duplicate for seamless looping -->
            <div class="ticker-slide merchant-slide">
                <div class="merchant-logo"><img src="images/merchant-2.png" alt="Lashly"></div>
                <div class="merchant-logo"><img src="images/merchant-diamanter.png" alt="Diamanter"></div>
                <div class="merchant-logo"><img src="images/merchant-sinocrack.png" alt="Sinorack"></div>
                <div class="merchant-logo"><img src="images/merchant-5.png" alt="Delikate matgaver"></div>
                <div class="merchant-logo"><img src="images/logo-reisespill.png" alt="Reisespill"></div>
                <div class="merchant-logo"><img src="images/logo-home-interior.png" alt="Home and interior"></div>
            </div>
        </div>
    </section>
"""
    
    # Find what's after the section
    end_section = """    </section>"""
    parts = html.split(end_section)
    if len(parts) > 1:
        new_html += end_section.join(parts[1:])
        
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
