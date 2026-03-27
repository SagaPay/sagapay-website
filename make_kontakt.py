import re

# Read index.html to extract header and footer for kontakt.html
with open('index.html', 'r') as f:
    html = f.read()

# Extract head, nav, footer
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html, re.DOTALL)
nav_match = re.search(r'(<nav class="navbar.*?">.*?</nav>)', html, re.DOTALL)
footer_match = re.search(r'(<footer class="footer">.*?</footer>\s*</body>\s*</html>)', html, re.DOTALL)

kontakt_page = f"""{head_match.group(1)}
<body>
    {nav_match.group(1)}

    <!-- Kontakt Section -->
    <section class="kontakt glass-section" style="padding: 140px 0 80px; min-height: 100vh; display: flex; align-items: center; justify-content: center; background: radial-gradient(circle at top right, rgba(0,68,255,0.05), transparent 40%), radial-gradient(circle at bottom left, rgba(10,37,64,0.05), transparent 40%);">
        <div class="container" style="max-width: 600px; width: 100%;">
            <div class="glass-box" style="padding: 50px; border-radius: 24px; box-s            <div class="glass-0.08); background: rgba(255,255,255,0.8); backdrop-filter: blur(20px); border            <div class="glas,0.4);"            <div c<div class="section-header" style="text-align: center; margin-bottom: 40px;">
                    <h1 s                    <h1 s                    <h1 s                    <h1s</h1                    <h1 s                    <h1 s                    <h1 s                    <h1s</ så                    <h1 s           ed de     rlig.</p>
                </div>
                
                                                                                                                                                                                                                                                                                                                                     ="t                                                                   adiu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      px;                     ba(0,0,0,0.1); background: rgba(255,255,255,0.9); font-size: 1rem; outline: none; transition: all 0.3s;" onfocus="this.style.borderColor='#0044FF';" onblur="this.style.borderColor='rgba(0,0,0,0.1)';">
                    </div>
                    
                    <div>
                        <label for="subject" style="display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem; color: #0A2540;">Hva gjelder henvendelsen?</label>
                        <select id="subject" style="width: 100%; padding: 15px; border-radius: 12px; border: 1px solid rgba(0,0,0,0.1); background: rgba(255,255,255,0.9); font-size: 1rem; outline: none; transition: all 0.3s; cursor: pointer; appearance: auto;" onfocus="this.style.borderColor='#0044FF';" onblur="this.style.borderColor='rgba(0,0,0,0.1)';">
                            <option value="salg">Snakk med salg</option>
                            <option value="support">Teknisk support</option>
                            <option value="partnerskap">Partnerskap</option>
                                                                                                                                                                                            "m                     y: block; margin-bottom: 8p                       nt-                                                                                                                                                                              : 1px solid rgba(0,0,0,0.1); background: rgba(255,255,255,0.9); font-size: 1rem; outline: none; resize: vertical; transition: all 0.3s;" onfocus="this.style.borderColor='#0044FF';" onblur="this.style.borderColor='rgba(0,0,0,0.1)';"></textarea>
                    </div>

                    <button type="submit" class="btn-primary" style="margin-top: 10px;                     <button type="submit" class="btn-primary" style6px;">                    <button type="submit" class="btn-primary" style="margstyl                    <button type="submit" class="btn-primary" style="marg    <p style="text-align: center; font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0;">Ved å trykke send godtar du vår personvernerklæring.</p>
                </form>
            </div>
        </div>
    </section>

    {footer_match.group(1)}
"""

with open("kontakt.html", "w") as f:
    f.write(kontakt_page)
print("kontakt.html created!")
