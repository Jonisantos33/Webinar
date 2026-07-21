"""
Tests for dark mode toggle functionality
"""
import re
from pathlib import Path


def read_html_file():
    """Read the index.html file"""
    html_path = Path(__file__).parent / "index.html"
    with open(html_path, 'r', encoding='utf-8') as f:
        return f.read()


def test_dark_mode_toggle_exists():
    """Test that the toggle button exists in the HTML"""
    html_content = read_html_file()
    
    # Check for theme toggle button
    assert 'id="themeToggle"' in html_content, "Dark mode toggle button not found"
    assert 'class="theme-toggle"' in html_content, "Theme toggle class not found"
    assert 'aria-label' in html_content, "Accessibility label not found"


def test_light_mode_css_variables_defined():
    """Test that light mode CSS variables are properly defined"""
    html_content = read_html_file()
    
    # Check for light mode variables in :root
    light_mode_vars = {
        '--bg: #ffffff': '--bg: #ffffff',
        '--bg2: #f8fafc': '--bg2: #f8fafc',
        '--surface: #f1f5f9': '--surface: #f1f5f9',
        '--text: #0a0e1a': '--text: #0a0e1a',
        '--border: rgba(0,0,0,0.08)': '--border: rgba(0,0,0,0.08)',
    }
    
    for var_name, var_value in light_mode_vars.items():
        assert var_name in html_content, f"Light mode variable '{var_name}' not found"


def test_dark_mode_css_variables_defined():
    """Test that dark mode CSS variables are properly defined"""
    html_content = read_html_file()
    
    # Check for dark mode variables (data-theme="dark")
    dark_mode_vars = [
        '--bg: #0a0e1a',
        '--bg2: #0f1526',
        '--surface: #141b2e',
        '--text: #ffffff',
        '--border: rgba(255,255,255,0.08)',
    ]
    
    # Find the dark mode CSS block
    dark_mode_pattern = r':root\[data-theme="dark"\]\s*\{[^}]*\}'
    dark_mode_blocks = re.findall(dark_mode_pattern, html_content, re.DOTALL)
    
    assert len(dark_mode_blocks) > 0, "Dark mode CSS variables not found"
    
    # Check that at least one dark mode variable is present
    dark_mode_content = ' '.join(dark_mode_blocks)
    found_vars = [var for var in dark_mode_vars if var in dark_mode_content]
    assert len(found_vars) > 0, "No dark mode CSS variables found in :root[data-theme='dark']"


def test_smooth_transition_defined():
    """Test that smooth transitions are defined for theme changes"""
    html_content = read_html_file()
    
    # Check for transition property
    assert 'transition:' in html_content, "Transition property not found"
    assert '0.3s' in html_content, "0.3s transition duration not found"


def test_modal_works_in_dark_mode():
    """Test that modal styling is adapted for dark mode"""
    html_content = read_html_file()
    
    # Check that modal has dark mode styling
    assert ':root[data-theme="dark"] .modal' in html_content, "Modal dark mode styling not found"


def test_input_dark_mode_styling():
    """Test that input fields have dark mode styling"""
    html_content = read_html_file()
    
    # Check for dark mode input styling
    assert ':root[data-theme="dark"] input' in html_content, "Input dark mode styling not found"
    assert '#141b2e' in html_content, "Dark mode input background color not found"


def test_javascript_dark_mode_functionality():
    """Test that JavaScript dark mode toggle function exists"""
    html_content = read_html_file()
    
    # Check for necessary JavaScript functions
    assert 'themeToggle' in html_content, "themeToggle element not found in JavaScript"
    assert 'sessionStorage' in html_content, "sessionStorage not used for persistence"
    assert 'applyTheme' in html_content, "applyTheme function not found"
    assert 'data-theme' in html_content, "data-theme attribute handling not found"
