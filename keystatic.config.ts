import { config, fields, collection } from '@keystatic/core';

export default config({
  storage: {
    kind: process.env.NODE_ENV === 'development' ? 'local' : 'github',
    repo: {
      owner: 'IH-Tahim',
      name: 'portfolio-vcard'
    }
  },
  collections: {
    posts: collection({
      label: 'Blog Posts',
      slugField: 'title',
      path: 'src/content/posts/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Title' } }),
        date: fields.date({ label: 'Date', defaultValue: { kind: 'today' } }),
        image: fields.image({
          label: 'Cover Image',
          directory: 'public/images/posts',
          publicPath: '/images/posts/',
        }),
        readTime: fields.text({ label: 'Read Time', defaultValue: '5 min read' }),
        description: fields.text({ label: 'Short Description', multiline: true }),
        content: fields.markdoc({ label: 'Content' }),
      },
    }),
    portfolio: collection({
      label: 'Portfolio Projects',
      slugField: 'title',
      path: 'src/content/portfolio/*',
      format: { contentField: 'content' },
      schema: {
        title: fields.slug({ name: { label: 'Project Title' } }),
        date: fields.date({ label: 'Date', defaultValue: { kind: 'today' } }),
        category: fields.text({ label: 'Category', defaultValue: 'Web Development' }),
        description: fields.text({ label: 'Short Description', multiline: true }),
        image: fields.image({
          label: 'Project Cover',
          directory: 'public/images/portfolio',
          publicPath: '/images/portfolio/',
        }),
        content: fields.markdoc({ label: 'Project Details' }),
      },
    }),
  },
});
