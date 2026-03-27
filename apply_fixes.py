import glob
import os

def apply_fixes():
    # 1. Update contacts in all html files
    html_files = glob.glob("*.html")
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace contacts
        content = content.replace('href="#sales"', 'href="mailto:support@sagapay.no"')
        content = content.replace('mailto:hei@sagapay.no', 'mailto:support@sagapay.no')
        content = content.replace('kristoffer@sagapay.no', 'support@sagapay.no')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    # 2. Fix specific om-oss.html layout issues
    om_oss_path = "om-oss.html"
    if os.path.exists(om_oss_path):
        with open(om_oss_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Fix floating boxes
        old_hero_boxes = '''<div style="position: relative; width: 100%; max-width: 400px; height: 350px;">
                        <div class="float-box glass-box bg-gradient-1" style="background: linear-gradient(135deg, #0A2540 0%, #4E65FF 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);" style="position: absolute; top: 10%; left: 0%; padding: 30px; border-radius: 20px; animation: float-bounce 6s ease-in-out infinite;">
                            <h3 style="color: white; font-size: 2rem; margin-bottom: 5px;">100%</h3>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">Norsk eid</p>
                        </div>
                        <div class="float-box glass-box bg-gradient-2" style="background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);" style="position: absolute; top: 40%; right: -10%; padding: 30px; border-radius: 20px; animation: float-bounce 7s ease-in-out infinite reverse;">
                            <h3 style="color: white; font-size: 2rem; margin-bottom: 5px;">24/7</h3>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">Support</p>
                        </div>
                        <div class="float-box glass-box bg-gradient-3" style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px);" style="position: absolute; bottom: 0%; left: 15%; padding: 30px; border-radius: 20px; animation: float-bounce 5s ease-in-out infinite;">
                            <h3 style="color: white; font-size: 2rem; margin-bottom: 5px;">0kr</h3>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">I etablering</p>
                        </div>
                    </div>'''
        
        new_hero_boxes = '''<div style="display: flex; flex-direction: column; gap: 20px; width: 100%; max-width: 400px; padding: 20px 0;">
                        <div class="float-box glass-box" style="background: #0A2540; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 30px; border-radius: 20px; transform: translateX(-10%); animation: float-bounce 6s ease-in-out infinite;">
                            <h3 style="color: white; font-size: 2rem; margin-bottom: 5px;">100%</h3>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">Norsk eid</p>
                        </div>
                        <div class="float-box glass-box" style="background: #0044FF; border: 1px solid rgba(255,255,255,0.1); backdrop-filter: blur(10px); padding: 30px; border-radius: 20px; transform: translateX(10%); animation: float-bounce 7s ease-in-out infinite reverse;">
                            <h3 style="color: white; font-size: 2rem; margin-bottom: 5px;">24/7</h3>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">Support</p>
                        </div>
                        <div class="float-box glass-box" style="background: #FFFFFF; border: 1px solid rgba(0,0,0,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 30px; border-radius: 20px; transform: translateX(5%); animation: float-bounce 5s ease-in-out infinite;">
                            <h3 style="color: #0A2540; font-size: 2rem; margin-bottom: 5px;">0kr</h3>
                            <p style="color: #4A5568; margin: 0; font-size: 0.9rem;">I etablering</p>
                        </div>
                    </div>'''
        
        content = content.replace(old_hero_boxes, new_hero_boxes)

        # Fix bento gradients and icon colors
        # Backgrounds to #F6F9FC
        content = content.replace('background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);', 'background: #F6F9FC;')
        content = content.replace('background: linear-gradient(135deg, #4E65FF 0%, #92EFFD 100%);', 'background: #F6F9FC;')
        content = content.replace('background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);', 'background: #F6F9FC;')
        content = content.replace('background: linear-gradient(135deg, #8E2DE2 0%, #4A00E0 100%);', 'background: #F6F9FC;')
        
        # Icon colors to #0044FF
        content = content.replace('color: white; font-size: 4rem;', 'color: #0044FF; font-size: 4rem;')

        with open(om_oss_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
if __name__ == "__main__":
    apply_fixes()
    print("Fixes applied successfully!")
