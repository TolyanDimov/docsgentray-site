import { MetadataRoute } from 'next';
import { seoPages } from '@/lib/seo-pages';

export default function sitemap(): MetadataRoute.Sitemap {
  const base = 'https://docsgentray.example.com';
  const staticRoutes = ['', '/pricing', '/docs', '/blog', '/faq', '/contacts'];
  return [
    ...staticRoutes.map((route) => ({ url: `${base}${route}` })),
    ...seoPages.map((p) => ({ url: `${base}/seo/${p.slug}` })),
  ];
}
