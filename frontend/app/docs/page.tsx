import { Card } from '@/components/ui/card';

export default function DocsPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Documentation</h1>
      <div className='mt-6 grid gap-4 md:grid-cols-3'>
        <Card><h3 className='font-semibold'>Getting Started</h3><p className='mt-2 text-sm text-muted-foreground'>Install app, create project folder, add templates.</p></Card>
        <Card><h3 className='font-semibold'>Licensing</h3><p className='mt-2 text-sm text-muted-foreground'>Generate device key and activate with signed token.</p></Card>
        <Card><h3 className='font-semibold'>Admin API</h3><p className='mt-2 text-sm text-muted-foreground'>Manage users, tariffs, and license lifecycle.</p></Card>
      </div>
    </section>
  );
}
