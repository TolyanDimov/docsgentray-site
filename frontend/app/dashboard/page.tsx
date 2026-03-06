import { Card } from '@/components/ui/card';

export default function DashboardPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Dashboard</h1>
      <div className='mt-6 grid gap-4 md:grid-cols-3'>
        <Card><h3 className='font-semibold'>Active License</h3><p className='mt-2 text-sm text-muted-foreground'>12 months / active</p></Card>
        <Card><h3 className='font-semibold'>Device</h3><p className='mt-2 text-sm text-muted-foreground'>fingerprint: 2f4d...e92</p></Card>
        <Card><h3 className='font-semibold'>Renewal</h3><p className='mt-2 text-sm text-muted-foreground'>Next renewal in 243 days</p></Card>
      </div>
    </section>
  );
}
