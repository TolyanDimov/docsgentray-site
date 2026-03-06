import { Card } from '@/components/ui/card';

const items = [
  ['Does it work offline?', 'Yes. Desktop app and license verification run offline.'],
  ['What formats are supported?', 'Excel + Word templates with PDF export.'],
  ['How is license protected?', 'Ed25519 asymmetric signature verification.'],
];

export default function FaqPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>FAQ</h1>
      <div className='mt-6 grid gap-4'>
        {items.map(([q, a]) => <Card key={q}><h3 className='font-semibold'>{q}</h3><p className='mt-2 text-sm text-muted-foreground'>{a}</p></Card>)}
      </div>
    </section>
  );
}
