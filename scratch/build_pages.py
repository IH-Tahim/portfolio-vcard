import os
import re

files_to_process = [
    ('ihtahim_services.html', 'services.astro', 'Services | Imam Hasan Tahim'),
    ('ihtahim_contact.html', 'contact.astro', 'Contact | Imam Hasan Tahim'),
    ('vcard.html', 'vcard.astro', 'vCard | Imam Hasan Tahim')
]

for in_file, out_file, title in files_to_process:
    with open(rf'C:\Users\Tahim\OneDrive\Protfolio Antigraity\exampledemo\{in_file}', 'r', encoding='utf-8') as f:
        content = f.read()

    # The body content starts after the nav and ends before the footer.
    # However, vcard.html might not have a nav or footer, or it might be different. Let's check vcard.html structure by looking for nav and footer.
    nav_match = re.search(r'</nav>', content, re.IGNORECASE)
    footer_match = re.search(r'<footer', content, re.IGNORECASE)

    start_idx = nav_match.end() if nav_match else re.search(r'<body.*?>', content, re.IGNORECASE).end()
    end_idx = footer_match.start() if footer_match else re.search(r'</body>', content, re.IGNORECASE).start()

    body_content = content[start_idx:end_idx].strip()

    astro_frontmatter = f'''---
import Layout from '../layouts/Layout.astro';
---

<Layout title="{title}">
'''

    astro_footer = '''
</Layout>
'''

    with open(rf'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\pages\{out_file}', 'w', encoding='utf-8') as f:
        f.write(astro_frontmatter + body_content + astro_footer)

    print(f'{out_file} generated successfully.')
