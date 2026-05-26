import re

with open("index.html", "r") as f:
    html = f.read()

def replace_card(m):
    card_classes = m.group(1) # e.g. "card card-bio" or "card h-100"
    inner_html = m.group(2)
    
    # Try to guess a terminal title from the first h4 or h5
    title_match = re.search(r'<h[45]>(?:<b>)?(?:<img[^>]*>\s*\|\s*)?(?:<strong>)?([^<]+?)(?:</strong>)?(?:</b>)?</h[45]>', inner_html)
    title = title_match.group(1).strip().lower().replace(" ", "-") if title_match else "process"
    
    # Strip the hr that follows the title since we have the header now
    inner_html = re.sub(r'<hr>\s*', '', inner_html, count=1)
    
    header = f"""
          <div class="card-header">
            <div class="mac-buttons">
              <span class="mac-btn"></span>
              <span class="mac-btn"></span>
              <span class="mac-btn"></span>
            </div>
            <span class="terminal-title">~/{title}</span>
          </div>
          <div class="card-content">"""
          
    return f'<div class="{card_classes}">{header}{inner_html}</div>'

# Regex to find cards. Non-greedy match on the inside, stopping before the final </div> of the card.
# The card structure is usually: <div class="card..."><div class="card-body">...</div></div>
# We want to wrap <div class="card-body">...</div> inside the new <div class="card-content">
html = re.sub(r'<div class="(card[^"]*)">\s*(<div class="card-body">.*?</div>)\s*</div>', replace_card, html, flags=re.DOTALL)

# Add mono-metrics
html = html.replace('73.5%', '<span class="mono-metric">73.5%</span>')
html = html.replace('26×', '<span class="mono-metric">26×</span>')
html = html.replace('34.6%', '<span class="mono-metric">34.6%</span>')
html = html.replace('100%', '<span class="mono-metric">100%</span>')
html = html.replace('99.9%', '<span class="mono-metric">99.9%</span>')
html = html.replace('<1s', '<span class="mono-metric">&lt;1s</span>')
html = html.replace('3.9', '<span class="mono-metric">3.9</span>')

with open("index.html", "w") as f:
    f.write(html)
