import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update the Bio Cards
# For each <div class="card card-bio">, we want to extract the title from the h4, and add a card-header.
def replace_bio_card(match):
    inner = match.group(1)
    # find the title: <h4><b><img ...> | Title</b></h4>
    # fallback to just "About" if not found
    title_match = re.search(r'<h4><b>(?:<img[^>]*>\s*\|\s*)?([^<]+)</b></h4>', inner)
    title = title_match.group(1).strip() if title_match else "bio"
    title_lower = title.lower().replace(" ", "-")
    
    # remove the old h4 and hr
    inner = re.sub(r'<h4><b>.*?</b></h4>\s*<hr>', '', inner, flags=re.DOTALL)
    
    return f"""<div class="card card-bio">
          <div class="card-header">
            <div class="mac-buttons">
              <span class="mac-btn"></span>
              <span class="mac-btn"></span>
              <span class="mac-btn"></span>
            </div>
            <span class="terminal-title">~/{title_lower}</span>
          </div>
          <div class="card-content">{inner}</div>"""

content = re.sub(r'<div class="card card-bio">(.*?)</div>\s*</div>\s*(?=</div>|\n\s*<div class="card)', 
                 lambda m: replace_bio_card(m) + "\n        </div>", 
                 content, flags=re.DOTALL)

# Let's actually use a simpler approach for the script to avoid regex hell on nested divs.
