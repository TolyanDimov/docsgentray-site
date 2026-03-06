import { Button } from '@/components/ui/button';

export function CtaSection() {
  return (
    <section className='my-16 rounded-2xl border bg-primary p-10 text-primary-foreground'>
      <h2 className='text-3xl font-semibold'>Ready to automate document generation?</h2>
      <p className='mt-2 max-w-2xl opacity-90'>Deploy DocsGenTray in your workflow with secure offline licenses and SaaS-grade UX.</p>
      <div className='mt-5 flex gap-3'>
        <Button variant='outline'>Book a call</Button>
        <Button className='bg-white text-black hover:bg-white/90'>Get started</Button>
      </div>
    </section>
  );
}
