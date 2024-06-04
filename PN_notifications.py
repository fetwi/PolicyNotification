import os
from bs4 import BeautifulSoup

dir_path = os.path.dirname(os.path.realpath(__file__))

# Define the source folder
source_dir = os.path.join(dir_path, "source")
target_dir = os.path.join(dir_path, "notifications")

html_files = [f for f in os.listdir(source_dir) if f.endswith('.html')]

for html_file in html_files:
    with open(os.path.join(source_dir, html_file), 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        
    language = soup.find('html')
    language = language['lang'] if language else 'NA'
    id_tag = soup.find('dd')
    id = id_tag.text if id_tag else 'NA'
    effective_date_tag = soup.find('dt', text=['Effective date', 'Date d\'effet'])
    effective_date = effective_date_tag.find_next_sibling('dd').text if effective_date_tag else 'NA'


    
    output_filename = f'{language}~{id}~{effective_date}.html'

    if language.lower() == "en":
        see_revision_history = "No content."
        remarks_label = "<h3 class=\"clause-heading\">Remarks – Recommended Use of SACC Item</h3>"
        legal_text_label = "<h3 class=\"clause-heading\">Legal text for SACC item</h3>"
    elif language.lower() == "fr":
        see_revision_history = "Pas de contentu."
        remarks_label = "<h3 class=\"clause-heading\">Remarques - Utilisation recommandée de l’item des CCUA</h3>"
        legal_text_label = "<h3 class=\"clause-heading\">Le texte légal de l’item des CCUA</h3>"

    pn_main_tag = soup.find('div', class_='field-name-field-body')
    pn_sm_tag = soup.find('div', class_='field-name-field-assoc-sm-items-view')
    pn_sacc_tag = soup.find('div', class_='field-name-field-assoc-sacc-items-view')

    if pn_main_tag is None:
        content = see_revision_history
    else:
        content = ''.join([str(pn_main_tag), str(pn_sm_tag), str(pn_sacc_tag)]) if pn_main_tag else 'NA'
        if not content:
            content = see_revision_history

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