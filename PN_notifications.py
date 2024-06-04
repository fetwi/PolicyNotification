import os
from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))

# Define the source folder
source_dir = os.path.join(dir_path, "source")
target_dir = os.path.join(dir_path, "clauses")

html_files = [f for f in os.listdir(source_dir) if f.endswith('.html')]

for html_file in html_files:
    with open(os.path.join(source_dir, html_file), 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
    language = soup.find('html')
    language = language['lang'] if language else 'N/A'
    effective_date_tag = soup.find('dt', string=lambda x: x in ['Effective Date', 'Date d\'effet '])
    effective_date = effective_date_tag.find_next_sibling('dd').find('span') if effective_date_tag else None
    effective_date = effective_date.text if effective_date else 'N/A'
    id_tag = soup.find('dt', string='ID')
    id = id_tag.find_next_sibling('dd') if id_tag else None
    id = id.text if id else 'N/A'
    
    output_filename = f'{language}~{effective_date}~{id}.txt'

    if language.lower() == "en":
        see_revision_history = "See revision history."
        remarks_label = "<h3 class=\"clause-heading\">Remarks – Recommended Use of SACC Item</h3>"
        legal_text_label = "<h3 class=\"clause-heading\">Legal text for SACC item</h3>"
    elif language.lower() == "fr":
        see_revision_history = "Voir l'historique des révisions."
        remarks_label = "<h3 class=\"clause-heading\">Remarques - Utilisation recommandée de l’item des CCUA</h3>"
        legal_text_label = "<h3 class=\"clause-heading\">Le texte légal de l’item des CCUA</h3>"

    sacc_item_text_heading = soup.find(id='sacc-item-text-heading')

    if sacc_item_text_heading is None:
        content = see_revision_history
    else:
        sibling_tags = []
        for sibling in sacc_item_text_heading.find_next_siblings():
            if sibling.name != 'abbr':  # Skip 'abbr' tags
                sibling_tags.append(str(sibling))  # Convert tag to string to get minified HTML
        content = ' '.join(sibling_tags)
        if not content:
            content = see_revision_history

    if not content.startswith('<pre>') and not content.endswith('</pre>'):
        content = '<pre>' + content + '</pre>'

    remarks = soup.select('section.group-sacc-remarks')
    if remarks:
        h3_tag = remarks[0].find('h3')
        if h3_tag:
            h3_tag.decompose()  # Remove the first h3 tag
            div_tag = remarks[0].find('div')
        if div_tag:
            div_tag.unwrap()  # Remove the div tag but keep its content

        content = remarks_label + remarks[0].prettify() + legal_text_label + content
    
    # Parse the content with BeautifulSoup
    content_soup = BeautifulSoup(content, 'html.parser')

    # Find all 'a' tags in the parsed content
    for a_tag in content_soup.find_all('a'):
        # If the 'a' tag has an 'href' attribute and the 'href' attribute does not start with '#'
        if 'href' in a_tag.attrs and not a_tag['href'].startswith('#'):
            # Replace the 'a' tag with its text content
            a_tag.replace_with(a_tag.get_text())
        if 'href' in a_tag.attrs and a_tag['href'].startswith('#'):
            # Insert effective_date and id after the '#'
            a_tag['href'] = '#' + effective_date + id + a_tag['href'][1:]

    # Find all tags with an 'id' attribute
    for tag in content_soup.find_all(id=True):
        # Insert effective_date and id before the 'id' value
        tag['id'] = effective_date + id + tag['id']

    # Convert the modified BeautifulSoup object back to a string
    content = str(content_soup)

    with open(os.path.join(target_dir, output_filename), 'w', encoding='utf-8') as file:
        file.write(content)