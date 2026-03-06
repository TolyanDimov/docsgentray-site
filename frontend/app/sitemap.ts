import { MetadataRoute } from 'next';
import { seoPages } from '@/lib/seo-pages';

export default function sitemap(): MetadataRoute.Sitemap {
  const base = 'https://docsgentray.example.com';
  const staticRoutes = ['', '/features', '/pricing', '/docs', '/blog', '/faq', '/contact', '/auth', '/dashboard', '/admin'];
  return [
    ...staticRoutes.map((route) => ({ url: `${base}${route}` })),
    ...seoPages.map((p) => ({ url: `${base}/seo/${p.slug}` })),
  ];
}
