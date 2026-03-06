import { FeaturesGrid } from '@/components/sections/features';
import { CtaSection } from '@/components/sections/cta';

export default function FeaturesPage() {
  return (
    <>
      <section className='py-12'>
        <h1 className='text-4xl font-bold'>Features</h1>
        <p className='mt-3 text-muted-foreground'>Everything you need to run enterprise-grade document automation.</p>
      </section>
      <FeaturesGrid />
      <CtaSection />
    </>
  );
}
