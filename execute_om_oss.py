import re

with open('om-oss.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_content = """    <section class="nettbetaling-hero" style="background: linear-gradient(135deg, rgba(82,113,255,0.05) 0%, rgba(200,80,192,0.05) 100%);">
        <div class="container" style="display: flex; gap: 40px; align-items: center; min-height: 50vh;">
            <div class="nettbetaling-hero-text" style="flex: 1;">
                <h1>Om Sagapay.</h1>
                <p>Norskutviklet betalingsinfrastruktur for det moderne markedet. Vi tror på å fjerne unødvendige mellomledd for å gi bedrifter lavere kostnader, høyere konvertering og smidigere hverdager.</p>
                <div style="margin-top: 25px; display: flex; gap: 15px;">
                    <a href="mailto:hei@sagapay.no" class="btn-primary">Snakk med salg</a>
                    <a href="priser.html" class="btn-outline">Se våre priser</a>
                </div>
            </div>
            <div class="nettbetaling-hero-img-container" style="flex: 1; display: flex; align-items: center; justify-content: center; position: relative;">
                <!-- Reusing float-box styles for a cool "Data" layout -->
                <div style="position: relative; width: 100%; max-width: 400px; height: 350px;">
                    <div class="float-box glass-box bg-gradient-1" style="position: absolute; top: 10%; left: 0%; padding: 30px; border-radius: 20px; animation: float 6s ease-in-out infinite;">
                        <h3 style="font-size: 3rem; margin-bottom: 5px; color: white;">100%</h3>
                        <p style="opacity: 0.9; font-weight: 500; color: white;">Norskutviklet</p>
                    </div>
                    <div class="float-box glass-box bg-gradient-2" style="position: absolute; top: 40%; right: -10%; padding: 30px; border-radius: 20px; animation: float 7s ease-in-out infinite reverse;">
                        <h3 style="font-size: 3rem; margin-bottom: 5px; color: white;">24/7</h3>
                        <p style="opacity: 0.9; font-weight: 500; color: white;">Support & Drift</p>
                    </div>
                    <div class="float-box glass-box bg-gradient-3" style="position: absolute; bottom: 0%; left: 15%; padding: 30px; border-radius: 20px; animation: float 5s ease-in-out infinite;">
                        <h3 style="font-size: 2.5rem; margin-bottom: 5px; color: white;"><i class="fa-solid fa-lock"></i></h3>
                        <p style="opacity: 0.9; font-weight: 500; color: white;">PCI DSS Sertifisert</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Kjerneverdier -->
    <section class="features bg-light" style="padding-top: 80px; padding-bottom: 80px;">
        <div class="container">
            <div class="section-header" style="text-align: center; margin-bottom: 50px;">
                <h2 style="font-size: 2.5rem; margin-bottom: 15px;">Dette tror vi på</h2>
                <p style="font-size: 1.1rem; color: var(--text-muted); max-width: 600px; margin: 0 auto;">Verdiene som driver oss til å bygge bedre løsninger for norsk næringsliv hver eneste dag.</p>
            </div>
            
            <div class="bento-grid">
                <!-- Verdi 1 -->
                <div class="bento-card">
                    <div class="bento-img-container bento-bg-1" style="display: flex; align-items: center; justify-content: center; height: 160px; background: var(--gradient-1);">
                        <i class="fa-solid fa-shield-halved" style="font-size: 4rem; color: white;"></i>
                    </div>
                    <div class="bento-content">
                        <h3>Sikkerhet i DNA-et</h3>
                        <p>Betalinger krever total tillit. Plattformen vår er bygget fra grunnen av med de strengeste bransjekravene innen databeskyttelse og oppetid.</p>
                    </div>
                </div>

                <!-- Verdi 2 -->
                <div class="bento-card">
                    <div class="bento-img-container bento-bg-2" style="display: flex; align-items: center; justify-content: center; height: 160px; background: var(--gradient-2);">
                        <i class="fa-solid fa-lightbulb" style="font-size: 4rem; color: white;"></i>
                    </div>
                    <div class="bento-content">
                        <h3>Innovasjon som fjerner friksjon</h3>
                        <p>Teknologi skal fungere i bakgrunnen. Vi fjerner klikk, nedetid og unødvendig kompleksitet slik at du kan fokusere på driften.</p>
                    </div>
                </div>

                <!-- Verdi 3 -->
                <div class="bento-card">
                    <div class="bento-img-container bento-bg-3" style="display: flex; align-items: center; justify-content: center; height: 160px; background: var(--gradient-3);">
                        <i class="fa-solid fa-handshake-angle" style="font-size: 4rem; color: white;"></i>
                    </div>
                    <div class="bento-content">
                        <h3>Nærhet til kundene</h3>
                        <p>Når det brenner, trenger du svar nå. Vårt norske supportteam kjenner det lokale markedet og er alltid klare til å bistå ved behov.</p>
                    </div>
                </div>
                
                <!-- Verdi 4 -->
                <div class="bento-card">
                    <div class="bento-img-container bento-bg-4" style="display: flex; align-items: center; justify-content: center; height: 160px; background: var(--gradient-4);">
                        <i class="fa-solid fa-chart-line" style="font-size: 4rem; color: white;"></i>
                    </div>
                    <div class="bento-content">
                        <h3>Skalerbar vekst</h3>
                        <p>Små eller store volumer spiller ingen rolle. Vår infrastruktur vokser i takt med at du får flere kunder – både på nett og i butikk.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- MERCHANT LOGO TICKER -->
    <section class="trusted-by" style="padding-bottom: 60px;">
        <div class="container">
            <p style="text-align: center; color: var(--text-muted); font-weight: 600; margin-bottom: 20px;">Bedrifter som stoler på vår infrastruktur</p>
        </div>
        <div class="ticker-wrap merchant-ticker-wrap">
            <div class="ticker-slide merchant-slide">
                <div class="merchant-logo"><img src="images/merchant-2.png" alt="Lashly"></div>
                <div class="merchant-logo"><img src="images/merchant-diamanter.png" alt="Diamanter"></div>
                <div class="merchant-logo"><img src="images/merchant-sinocrack.png" alt="Sinorack"></div>
                <div class="merchant-logo"><img src="images/logo-reisespill.png" alt="Reisespill"></div>
                <div class="merchant-logo"><img src="images/logo-home-interior.png" alt="Home and interior"></div>
            </div>
            <!-- Duplicate for seamless looping -->
            <div class="ticker-slide merchant-slide">
                <div class="merchant-logo"><img src="images/merchant-2.png" alt="Lashly"></div>
                <div class="merchant-logo"><img src="images/merchant-diamanter.png" alt="Diamanter"></div>
                <div class="merchant-logo"><img src="images/merchant-sinocrack.png" alt="Sinorack"></div>
                <div class="merchant-logo"><img src="images/logo-reisespill.png" alt="Reisespill"></div>
                <div class="merchant-logo"><img src="images/logo-home-interior.png" alt="Home and interior"></div>
            </div>
        </div>
    </section>"""

pattern = re.compile(r'<header class="pricing-hero">.*?</section>', re.DOTALL)
if pattern.search(html):
    html = pattern.sub(new_content, html)
    print("Match found, replacing.")
else:
    print("Match not found!")

with open('om-oss.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replacement complete.")
