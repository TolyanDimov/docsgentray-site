import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';

export default function AuthPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Auth</h1>
      <Card className='mt-6 max-w-md'>
        <label className='text-sm'>Email</label>
        <input className='mt-1 w-full rounded-md border bg-background px-3 py-2' placeholder='you@example.com' />
        <label className='mt-4 block text-sm'>Password</label>
        <input type='password' className='mt-1 w-full rounded-md border bg-background px-3 py-2' placeholder='••••••••' />
        <Button className='mt-4 w-full'>Sign In</Button>
      </Card>
    </section>
  );
}
