'use client';

import { motion } from 'framer-motion';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

export function HeroSection() {
  return (
    <section className='grid gap-10 py-16 md:grid-cols-2 md:py-24'>
      <div>
        <Badge className='mb-4'>#1 Offline document automation SaaS</Badge>
        <h1 className='text-4xl font-bold leading-tight md:text-6xl'>Generate Word/Excel/PDF docs from Excel in seconds</h1>
        <p className='mt-4 text-lg text-muted-foreground'>Modern platform for secure licensing and scaling document generation for teams.</p>
        <div className='mt-6 flex gap-3'>
          <Button size='lg'>Start Free Trial</Button>
          <Button variant='outline' size='lg'>View Demo</Button>
        </div>
      </div>
      <motion.div initial={{ opacity: 0, y: 16 }} animate={{ opacity: 1, y: 0 }} className='rounded-2xl border bg-gradient-to-br from-indigo-500/20 to-cyan-400/10 p-6'>
        <div className='rounded-xl border bg-background p-4'>
          <p className='text-sm text-muted-foreground'>Product screenshot placeholder</p>
          <div className='mt-4 h-56 rounded-lg bg-muted/60' />
        </div>
      </motion.div>
    </section>
  );
}
