import os
import datetime

posts_dir = r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\content\posts'
portfolio_dir = r'C:\Users\Tahim\OneDrive\Protfolio Antigraity\src\content\portfolio'

os.makedirs(posts_dir, exist_ok=True)
os.makedirs(portfolio_dir, exist_ok=True)

blog_posts = [
    {
        "title": "The Future of Web Development with Astro",
        "description": "Astro is revolutionizing the way we build static and server-rendered sites. Discover why I switched to Astro and how it can boost your site's performance to 100/100.",
        "content": "Astro is an all-in-one web framework for building fast, content-focused websites. By extracting your UI components to islands, it dramatically reduces the amount of JavaScript sent to the client..."
    },
    {
        "title": "Mastering Facebook Ads in 2026",
        "description": "Learn the hidden secrets of Facebook Ads that top-tier digital marketers use to drastically reduce CPA and increase conversion rates.",
        "content": "The landscape of Facebook Ads has changed significantly. In this guide, we dive deep into the new AI-driven targeting algorithms and how you can leverage them for maximum ROI..."
    },
    {
        "title": "Why You Need a Dynamic Portfolio",
        "description": "A static portfolio is great, but a dynamic one powered by a Headless CMS like Keystatic gives you the flexibility to showcase your latest work effortlessly.",
        "content": "Managing a portfolio shouldn't be a chore. With Keystatic and Astro, you can simply write markdown files or use an intuitive UI to add new projects in minutes..."
    },
    {
        "title": "10 SEO Strategies that Actually Work",
        "description": "Stop wasting time on outdated SEO tactics. These 10 actionable strategies are proven to move the needle in today's competitive search landscape.",
        "content": "SEO is constantly evolving. In this article, we cover core web vitals, programmatic SEO, semantic HTML, and exactly how to optimize your content architecture..."
    },
    {
        "title": "Building High-Converting Landing Pages",
        "description": "Design isn't just about making things look pretty; it's about guiding the user to action. Learn the anatomy of a landing page that converts at 20%+.",
        "content": "A successful landing page relies on clear copy, contrasting calls to action, and removing friction. Let's break down the psychology of a high-converting page..."
    },
    {
        "title": "Shopify vs WordPress for E-commerce",
        "description": "Struggling to choose the right platform for your online store? We break down the pros and cons of Shopify and WooCommerce.",
        "content": "When it comes to E-commerce, both Shopify and WordPress are titans. However, the best choice depends entirely on your specific business model and technical expertise..."
    },
    {
        "title": "The Importance of Mobile-First Design",
        "description": "With over 60% of web traffic coming from mobile devices, a responsive design is no longer optional. It's mandatory.",
        "content": "A mobile-first approach means designing for the smallest screen first and working your way up. This ensures a flawless user experience regardless of the device..."
    },
    {
        "title": "How to Use Google Tag Manager effectively",
        "description": "Google Tag Manager is a powerful tool. Learn how to track conversions, button clicks, and implement Partytown for better performance.",
        "content": "Instead of hardcoding tags, GTM gives you a centralized dashboard. By pairing it with Astro's Partytown integration, you can maintain perfect Lighthouse scores..."
    }
]

portfolio_items = [
    {
        "title": "E-Commerce Replatforming for Local Brand",
        "category": "Shopify Development",
        "description": "Successfully migrated a legacy WooCommerce store to Shopify, resulting in a 40% increase in mobile conversions.",
        "image": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80",
        "content": "The client needed a faster, more reliable platform. We built a custom Shopify theme, integrated their inventory management system, and optimized the checkout flow."
    },
    {
        "title": "B2B SaaS Marketing Website",
        "category": "Web Development & SEO",
        "description": "Designed and developed a blazing fast Astro website for a SaaS startup, achieving 100/100 Lighthouse scores across the board.",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        "content": "Using Astro and Keystatic, we delivered a site that marketing could easily edit while maintaining absolute peak performance for SEO."
    },
    {
        "title": "National Real Estate Ad Campaign",
        "category": "Facebook & Google Ads",
        "description": "Managed a $50k/month ad spend across Meta and Google, generating qualified leads for luxury real estate agents.",
        "image": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=800&q=80",
        "content": "By leveraging lookalike audiences and highly targeted search intent keywords, we reduced the Cost Per Lead by 35% within the first two months."
    },
    {
        "title": "Local Restaurant Online Ordering System",
        "category": "WordPress Development",
        "description": "Built a custom online ordering platform on WordPress for a popular local restaurant chain, eliminating third-party app fees.",
        "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
        "content": "The solution included a custom dashboard for kitchen staff and an intuitive mobile interface for customers, leading to a massive ROI."
    }
]

# Generate Blog Posts
for i, post in enumerate(blog_posts):
    # Format title for filename
    filename = post["title"].lower().replace(' ', '-').replace(',', '') + '.mdoc'
    filepath = os.path.join(posts_dir, filename)
    
    # Calculate a date
    post_date = (datetime.datetime.now() - datetime.timedelta(days=i*5)).strftime('%Y-%m-%d')
    
    content = f"""---
title: {post['title']}
date: '{post_date}'
readTime: 5 min read
description: {post['description']}
---
{post['content']}

### The Details
This is dummy content generated for your new dynamic Keystatic blog! You can edit this directly in Keystatic or via your markdown files.
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Generate Portfolio Items
for i, item in enumerate(portfolio_items):
    filename = item["title"].lower().replace(' ', '-').replace(',', '') + '.mdoc'
    filepath = os.path.join(portfolio_dir, filename)
    
    item_date = (datetime.datetime.now() - datetime.timedelta(days=i*30)).strftime('%Y-%m-%d')
    
    content = f"""---
title: {item['title']}
date: '{item_date}'
category: {item['category']}
description: {item['description']}
image: {item['image']}
---
{item['content']}

### Project Outcomes
This is dummy project content. Here you would detail the challenges faced, the solutions provided, and the final results delivered to the client.
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated dummy content successfully.")
