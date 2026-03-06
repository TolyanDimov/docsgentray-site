import { Card } from '@/components/ui/card';

export default function ContactPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Contact</h1>
      <Card className='mt-6'>
        <p>Email: support@docsgentray.com</p>
        <p className='mt-2'>Telegram: @docsgentray_support</p>
      </Card>
    </section>
  );
}
