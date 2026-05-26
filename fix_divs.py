with open("index.html", "r") as f:
    html = f.read()

# Replace all occurrences of </div></div> that happen right before the closing of the column or next card.
# The safest way is to just replace '</div></div>' with '</div></div></div>' where it was added by my previous script.
# My previous script returned f'<div class="{card_classes}">{header}{inner_html}</div>'
# where inner_html ends with </div>. So it generated exactly "</div></div>" at the end of every card.
html = html.replace('</div></div>\n', '</div></div></div>\n')

with open("index.html", "w") as f:
    f.write(html)
