import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  // Use the glob loader to load markdoc files from src/content/posts
  loader: glob({ pattern: "**/*.mdoc", base: "./src/content/posts" }),
  schema: z.object({
    title: z.string(),
    date: z.string().or(z.date()).transform((val) => new Date(val)),
    readTime: z.string().default('5 min read'),
    description: z.string().optional(),
  }),
});

export const collections = { posts };
