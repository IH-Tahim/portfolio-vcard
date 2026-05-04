import os

portfolio_dir = r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\pages\portfolio'
os.makedirs(portfolio_dir, exist_ok=True)

index_content = '''---
import Layout from '../../layouts/Layout.astro';
import { getCollection } from 'astro:content';

const portfolio = await getCollection('portfolio');
const sortedPortfolio = portfolio.sort((a, b) => new Date(b.data.date).valueOf() - new Date(a.data.date).valueOf());
---

<Layout title="Portfolio | Imam Hasan Tahim">
  <section style="padding: 120px 7%; background: var(--dark); min-height: 80vh;">
    <div class="section-head reveal" style="text-align: center;">
      <div class="eyebrow" style="justify-content: center;">My Work</div>
      <h1 class="services-headline syne" style="margin-top: 1rem;">Featured <em>Projects</em></h1>
    </div>

    {sortedPortfolio.length === 0 ? (
      <div style="text-align: center; color: var(--muted); margin-top: 40px;">
        <p>No projects found yet.</p>
      </div>
    ) : (
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        {sortedPortfolio.map((project) => (
          <a href={`/portfolio/${project.id}`} style="display: block; background: var(--surface); border: 1px solid var(--border); border-radius: 8px; overflow: hidden; transition: all 0.3s;" class="reveal" onmouseover="this.style.borderColor='var(--border-o)'; this.style.transform='translateY(-4px)';" onmouseout="this.style.borderColor='var(--border)'; this.style.transform='translateY(0)';">
            {project.data.image && (
              <div style="width: 100%; height: 200px; overflow: hidden;">
                <img src={project.data.image} alt={project.data.title} style="width: 100%; height: 100%; object-fit: cover;" />
              </div>
            )}
            <div style="padding: 2rem;">
              <div style="font-size: 0.75rem; color: var(--orange); font-weight: 600; text-transform: uppercase; margin-bottom: 1rem;">
                {project.data.category} · {new Date(project.data.date).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}
              </div>
              <h3 class="syne" style="font-size: 1.5rem; font-weight: 700; color: var(--cream); margin-bottom: 1rem; line-height: 1.2;">
                {project.data.title}
              </h3>
              <p style="font-size: 0.95rem; color: var(--muted); line-height: 1.7;">
                {project.data.description}
              </p>
              <div style="margin-top: 1.5rem; font-size: 0.8rem; font-weight: 600; color: var(--orange); text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; gap: 8px;">
                View Project <span style="font-size: 1.2rem;">→</span>
              </div>
            </div>
          </a>
        ))}
      </div>
    )}
  </section>
</Layout>
'''

with open(os.path.join(portfolio_dir, 'index.astro'), 'w', encoding='utf-8') as f:
    f.write(index_content)

slug_content = '''---
import Layout from '../../layouts/Layout.astro';
import { getCollection, render } from 'astro:content';

export const prerender = true;

export async function getStaticPaths() {
  const projects = await getCollection('portfolio');
  return projects.map(project => ({
    params: { slug: project.id },
    props: { project },
  }));
}

const { project } = Astro.props;
const { Content } = await render(project);
---

<Layout title={`${project.data.title} | Portfolio`}>
  <article style="padding: 120px 7%; background: var(--dark); max-width: 900px; margin: 0 auto; min-height: 80vh;">
    <div class="reveal" style="margin-bottom: 3rem;">
      <div style="font-size: 0.75rem; color: var(--orange); font-weight: 600; text-transform: uppercase; margin-bottom: 1rem;">
        {project.data.category} · {new Date(project.data.date).toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}
      </div>
      <h1 class="syne" style="font-size: clamp(2.2rem,4vw,3.4rem); font-weight: 800; color: var(--cream); margin-bottom: 1.5rem; line-height: 1.1;">{project.data.title}</h1>
      {project.data.description && <p style="font-size: 1.1rem; color: var(--muted); line-height: 1.8;">{project.data.description}</p>}
    </div>

    {project.data.image && (
      <div class="reveal" style="margin-bottom: 3rem; border-radius: 12px; overflow: hidden; border: 1px solid var(--border);">
        <img src={project.data.image} alt={project.data.title} style="width: 100%; height: auto; display: block;" />
      </div>
    )}

    <div class="prose prose-lg prose-invert max-w-none prose-headings:font-syne prose-headings:font-bold prose-a:text-[#FF4D00] reveal">
      <Content />
    </div>
  </article>
</Layout>
'''

with open(os.path.join(portfolio_dir, '[slug].astro'), 'w', encoding='utf-8') as f:
    f.write(slug_content)

print('Portfolio pages created.')
