import { PricingSection } from '@/components/sections/pricing';
import { CtaSection } from '@/components/sections/cta';

export default function PricingPage() {
  return (
    <>
      <section className='py-12'>
        <h1 className='text-4xl font-bold'>Pricing</h1>
        <p className='mt-3 text-muted-foreground'>Choose the tariff that matches your team size.</p>
      </section>
      <PricingSection />
      <CtaSection />
    </>
  );
}
