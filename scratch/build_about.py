import os
import re

with open(r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\exampledemo\ihtahim_about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The body content of the about page starts after the nav and ends before the footer.
# But it's usually inside <main> or some wrapper, let's just grab everything after </nav> and before <footer>
match = re.search(r'</nav>(.*?)<footer', content, re.DOTALL | re.IGNORECASE)

if match:
    body_content = match.group(1).strip()
else:
    print('Could not find nav and footer tags.')
    exit(1)

astro_frontmatter = '''---
import Layout from '../layouts/Layout.astro';
---

<Layout title="About | Imam Hasan Tahim">
'''

astro_footer = '''
</Layout>
'''

with open(r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\pages\about.astro', 'w', encoding='utf-8') as f:
    f.write(astro_frontmatter + body_content + astro_footer)

print('about.astro generated successfully.')
