import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

const plans = [
  ['1 Month', '₽1,990', 'For individual users'],
  ['3 Months', '₽4,990', 'Best for small teams'],
  ['6 Months', '₽8,990', 'Advanced automation growth'],
  ['12 Months', '₽14,990', 'Enterprise annual savings'],
] as const;

export function PricingSection() {
  return (
    <section className='py-14'>
      <h2 className='text-3xl font-semibold'>Simple pricing</h2>
      <div className='mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-4'>
        {plans.map(([name, price, caption]) => (
          <Card key={name} className='flex flex-col justify-between'>
            <div>
              <h3 className='font-semibold'>{name}</h3>
              <p className='mt-2 text-2xl font-bold'>{price}</p>
              <p className='mt-2 text-sm text-muted-foreground'>{caption}</p>
            </div>
            <Button className='mt-4'>Choose plan</Button>
          </Card>
        ))}
      </div>
    </section>
  );
}
