"""
Prueba de criterios de aceptación - EDM-27
"""

def test_all_criteria():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extrae el header para análisis
    header_start = html.find('<header>')
    header_end = html.find('</header>')
    header_content = html[header_start:header_end]
    
    print("\n✅ CRITERIOS DE ACEPTACIÓN - EDM-27\n")
    print("=" * 70)
    
    # Criterio 1 - Toggle visible
    crit1 = 'id="themeToggle"' in header_content and '🌙' in header_content
    print(f"{'✓' if crit1 else '✗'} CRITERIO 1: Toggle visible en header")
    
    # Criterio 2 - Modo oscuro funcional
    crit2 = 'html.dark' in html and '--bg: #0a0e1a' in html and 'html.classList.add' in html
    print(f"{'✓' if crit2 else '✗'} CRITERIO 2: Variables CSS modo oscuro (#0a0e1a)")
    
    # Criterio 3 - Modo claro funcional
    crit3 = '--bg: #ffffff' in html and 'html.classList.remove' in html and '☀️' in html
    print(f"{'✓' if crit3 else '✗'} CRITERIO 3: Toggle a modo claro (#ffffff)")
    
    # Criterio 4 - Persistencia
    crit4 = "localStorage.getItem('theme')" in html and "localStorage.setItem('theme'" in html
    print(f"{'✓' if crit4 else '✗'} CRITERIO 4: Persistencia localStorage")
    
    # Criterio 5 - Modal intacto
    crit5 = 'ERROR REG-500' in html and 'id="errorModal"' in html
    print(f"{'✓' if crit5 else '✗'} CRITERIO 5: Modal ERROR REG-500 intacto")
    
    # Transición suave
    trans = 'transition: background-color 0.3s' in html
    print(f"{'✓' if trans else '✗'} Transición suave 0.3s")
    
    # Posición correcta
    logo_pos = header_content.find('class="logo"')
    toggle_pos = header_content.find('id="themeToggle"')
    badge_pos = header_content.find('header-badge')
    pos_correct = logo_pos < toggle_pos < badge_pos
    print(f"{'✓' if pos_correct else '✗'} Posición: logo → toggle → badge")
    
    print("=" * 70)
    
    all_pass = crit1 and crit2 and crit3 and crit4 and crit5 and trans and pos_correct
    if all_pass:
        print("\n🎉 TODOS LOS CRITERIOS CUMPLIDOS 🎉\n")
    else:
        print("\n⚠️  Revisar criterios no cumplidos\n")
    
    return all_pass

if __name__ == '__main__':
    test_all_criteria()
