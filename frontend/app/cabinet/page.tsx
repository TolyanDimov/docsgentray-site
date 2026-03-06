import { Card } from '@/components/ui/card';

export default function CabinetPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Cabinet</h1>
      <div className='mt-6 grid gap-4 md:grid-cols-2'>
        <Card><h3 className='font-semibold'>Profile</h3><p className='mt-2 text-sm text-muted-foreground'>email / phone / telegram</p></Card>
        <Card><h3 className='font-semibold'>License</h3><p className='mt-2 text-sm text-muted-foreground'>key / expires / tariff / fingerprint</p></Card>
      </div>
    </section>
  );
}
