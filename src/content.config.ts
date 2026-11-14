import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const news = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    image: z.string().optional(),
  }),
});

const events = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/events' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    location: z.string().optional(),
  }),
});

const staff = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/staff' }),
  schema: z.object({
    title: z.string(),
    role: z.string().optional(),
    photo: z.string().optional(),
  }),
});

const settings = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/settings' }),
  schema: z.object({
    countdownDate: z.coerce.date(),
    announcement: z.string().optional(),
    instagramUrl: z.string().url().optional(),
  }),
});

export const collections = { news, events, staff, settings };
