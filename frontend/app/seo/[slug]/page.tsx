import type { Metadata } from 'next';
import { seoPages } from '@/lib/seo-pages';
import { notFound } from 'next/navigation';

export function generateStaticParams() {
  return seoPages.map((page) => ({ slug: page.slug }));
}

export function generateMetadata({ params }: { params: { slug: string } }): Metadata {
  const page = seoPages.find((item) => item.slug === params.slug);
  if (!page) return {};
  return {
    title: page.title,
    description: page.description,
    openGraph: {
      title: page.title,
      description: page.description,
      type: 'article',
    },
  };
}

export default function SeoLanding({ params }: { params: { slug: string } }) {
  const page = seoPages.find((p) => p.slug === params.slug);
  if (!page) return notFound();

  return (
    <main>
      <h1>{page.h1}</h1>
      <p>{page.body}</p>
    </main>
  );
}
