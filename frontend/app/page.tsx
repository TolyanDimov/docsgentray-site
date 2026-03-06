import { HeroSection } from '@/components/sections/hero';
import { FeaturesGrid } from '@/components/sections/features';
import { PricingSection } from '@/components/sections/pricing';
import { CtaSection } from '@/components/sections/cta';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <FeaturesGrid />
      <PricingSection />
      <CtaSection />
    </>
  );
}
