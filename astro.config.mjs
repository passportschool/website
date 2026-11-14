import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.passportcharter.org',
  redirects: {
    // legacy WordPress hub slugs — keep URLs alive, point at the new directory pages
    '/parents-2': '/parents/',
    '/students-2': '/students/',
    '/school-calendar': '/parents-2/school-calendar/',
  },
});
