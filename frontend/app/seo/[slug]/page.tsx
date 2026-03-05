import { seoPages } from '@/lib/seo-pages';
import { notFound } from 'next/navigation';

export function generateStaticParams() {
  return seoPages.map((page) => ({ slug: page.slug }));
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
