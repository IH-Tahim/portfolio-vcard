import os
import re

with open('body_content.txt', 'r', encoding='utf-8') as f:
    body_content = f.read()

astro_frontmatter = '''---
import Layout from '../layouts/Layout.astro';
import { getCollection } from 'astro:content';

const allPosts = await getCollection('posts');
const latestPosts = allPosts.sort((a, b) => new Date(b.data.date).valueOf() - new Date(a.data.date).valueOf()).slice(0, 3);
---

<Layout title="Imam Hasan Tahim — Digital Marketer & Web Developer">
'''

new_sections = '''
<!-- ═══════════════════ LATEST BLOG POSTS ═══════════════════ -->
<section id="blog" style="padding: 100px 7%; background: var(--dark);">
  <div class="section-head reveal">
    <div class="eyebrow">Latest Insights</div>
    <h2 class="services-headline syne" style="margin-top: 1rem;">My Recent <em>Articles</em></h2>
  </div>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
    {latestPosts.map((post) => (
      <a href={`/blog/${post.slug}`} style="display: block; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 2rem; transition: all 0.3s;" class="reveal" onmouseover="this.style.borderColor='var(--border-o)'; this.style.transform='translateY(-4px)';" onmouseout="this.style.borderColor='var(--border)'; this.style.transform='translateY(0)';">
        <div style="font-size: 0.75rem; color: var(--orange); font-weight: 600; text-transform: uppercase; margin-bottom: 1rem;">
          {new Date(post.data.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })} · {post.data.readTime}
        </div>
        <h3 class="syne" style="font-size: 1.5rem; font-weight: 700; color: var(--cream); margin-bottom: 1rem; line-height: 1.2;">
          {post.data.title}
        </h3>
        <p style="font-size: 0.95rem; color: var(--muted); line-height: 1.7;">
          {post.data.description}
        </p>
        <div style="margin-top: 1.5rem; font-size: 0.8rem; font-weight: 600; color: var(--orange); text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; gap: 8px;">
          Read Article <span style="font-size: 1.2rem;">→</span>
        </div>
      </a>
    ))}
    {latestPosts.length === 0 && (
      <p style="color: var(--muted);">No blog posts found. Check back later!</p>
    )}
  </div>
  <div style="margin-top: 3rem; text-align: center;" class="reveal">
    <a href="/blog" class="btn-cv">View All Posts</a>
  </div>
</section>

<!-- ═══════════════════ FAQ ═══════════════════ -->
<section id="faq" style="padding: 100px 7%; background: var(--dark2);">
  <div class="section-head reveal" style="text-align: center;">
    <div class="eyebrow" style="justify-content: center;">FAQ</div>
    <h2 class="services-headline syne" style="margin-top: 1rem;">Frequently Asked <em>Questions</em></h2>
  </div>
  
  <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 1rem;">
    <div style="background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; border-radius: 4px;" class="reveal">
      <h3 class="syne" style="font-size: 1.2rem; font-weight: 700; color: var(--cream); margin-bottom: 0.5rem;">What industries do you specialize in?</h3>
      <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.7;">I have experience working across various industries including E-commerce, Real Estate, SaaS, and B2B Services. My strategies are adaptable and data-driven to fit your specific market.</p>
    </div>
    <div style="background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; border-radius: 4px;" class="reveal">
      <h3 class="syne" style="font-size: 1.2rem; font-weight: 700; color: var(--cream); margin-bottom: 0.5rem;">How long does it take to see results from SEO?</h3>
      <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.7;">SEO is a long-term game. Typically, you'll start seeing noticeable improvements in organic traffic and rankings within 3 to 6 months, depending on the competitiveness of your niche.</p>
    </div>
    <div style="background: var(--surface); border: 1px solid var(--border); padding: 1.5rem; border-radius: 4px;" class="reveal">
      <h3 class="syne" style="font-size: 1.2rem; font-weight: 700; color: var(--cream); margin-bottom: 0.5rem;">Do you offer custom web development?</h3>
      <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.7;">Yes! I build custom, high-performance websites using Astro, WordPress, and Shopify, tailored to your brand's unique needs and designed to convert visitors into customers.</p>
    </div>
  </div>
</section>
'''

astro_footer = '''
</Layout>
'''

# Wait! The body_content contains <!-- ═══════════════════ CTA BANNER ═══════════════════ -->
# The CTA banner is usually at the bottom. I should put my new sections BEFORE the CTA Banner!

# Let's split body_content by CTA Banner
parts = re.split(r'(<!-- ═══════════════════ CTA BANNER ═══════════════════ -->)', body_content)

if len(parts) > 1:
    final_content = parts[0] + new_sections + '\n' + parts[1] + parts[2]
else:
    final_content = body_content + new_sections

with open(r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\pages\index.astro', 'w', encoding='utf-8') as f:
    f.write(astro_frontmatter + final_content + astro_footer)

print('index.astro generated successfully.')
