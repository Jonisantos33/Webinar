import re


def test_dark_mode_toggle_exists_in_html():
    """Test that the dark mode toggle button exists in the HTML"""
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Check for toggle button with id="darkModeToggle"
    assert 'id="darkModeToggle"' in html_content, "Dark mode toggle button not found in HTML"
    
    # Check for the button element
    assert 'class="dark-mode-toggle"' in html_content, "Dark mode toggle button class not found"
    
    # Check for aria-label for accessibility
    assert 'aria-label' in html_content and 'darkModeToggle' in re.sub(
        r'\s+', ' ', html_content[html_content.find('darkModeToggle')-100:html_content.find('darkModeToggle')+200]
    ), "aria-label not found near dark mode toggle"


def test_light_mode_css_variables_defined():
    """Test that light mode CSS variables are properly defined in the :root selector"""
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract the :root CSS block
    root_match = re.search(r':root\s*\{([^}]+)\}', html_content)
    assert root_match, ":root selector not found in CSS"
    
    root_css = root_match.group(1)
    
    # Check for light mode color variables
    light_mode_vars = {
        '--bg': '#ffffff',
        '--bg2': '#f8fafc',
        '--surface': '#f1f5f9',
        '--text': '#0a0e1a',
        '--border': 'rgba(0,0,0,0.08)',
    }
    
    for var_name, expected_value in light_mode_vars.items():
        assert var_name in root_css, f"Light mode variable {var_name} not found in :root"
        # Check if the value is present (allowing for whitespace variations)
        assert re.search(rf'{var_name}\s*:\s*{re.escape(expected_value)}', root_css), \
            f"Light mode variable {var_name} value mismatch. Expected: {expected_value}"


def test_dark_mode_css_variables_defined():
    """Test that dark mode CSS variables are properly defined in the :root.dark-mode selector"""
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract the :root.dark-mode CSS block
    dark_root_match = re.search(r':root\.dark-mode\s*\{([^}]+)\}', html_content)
    assert dark_root_match, ":root.dark-mode selector not found in CSS"
    
    dark_root_css = dark_root_match.group(1)
    
    # Check for dark mode color variables
    dark_mode_vars = {
        '--bg': '#0a0e1a',
        '--bg2': '#0f1526',
        '--surface': '#141b2e',
        '--text': '#ffffff',
        '--border': 'rgba(255,255,255,0.08)',
    }
    
    for var_name, expected_value in dark_mode_vars.items():
        assert var_name in dark_root_css, f"Dark mode variable {var_name} not found in :root.dark-mode"
        # Check if the value is present (allowing for whitespace variations)
        assert re.search(rf'{var_name}\s*:\s*{re.escape(expected_value)}', dark_root_css), \
            f"Dark mode variable {var_name} value mismatch. Expected: {expected_value}"


if __name__ == '__main__':
    test_dark_mode_toggle_exists_in_html()
    print("✓ Test 1 passed: Dark mode toggle button exists in HTML")
    
    test_light_mode_css_variables_defined()
    print("✓ Test 2 passed: Light mode CSS variables are properly defined")
    
    test_dark_mode_css_variables_defined()
    print("✓ Test 3 passed: Dark mode CSS variables are properly defined")
    
    print("\nAll tests passed! ✓")
