import re
import os

astro_dir = r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\pages'
demo_dir = r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\exampledemo'

pages = {
    'about.astro': 'ihtahim_about.html',
    'services.astro': 'ihtahim_services.html',
    'contact.astro': 'ihtahim_contact.html'
}

for astro_file, html_file in pages.items():
    with open(os.path.join(demo_dir, html_file), 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract everything between </nav> and <footer>
    match = re.search(r'</nav>\s*(.*?)\s*<footer>', html, re.DOTALL | re.IGNORECASE)
    if match:
        content = match.group(1).strip()
        
        # Build the Astro file
        astro_content = f'''---
import Layout from '../layouts/Layout.astro';
---

<Layout title="{astro_file.replace('.astro', '').capitalize()} | Imam Hasan Tahim">
{content}
</Layout>
'''
        with open(os.path.join(astro_dir, astro_file), 'w', encoding='utf-8') as f:
            f.write(astro_content)
        print(f'Updated {astro_file}')
    else:
        print(f'Could not extract content from {html_file}')
