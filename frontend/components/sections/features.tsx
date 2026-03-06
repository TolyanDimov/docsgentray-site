import { FileSpreadsheet, ShieldCheck, Bot, Zap, LayoutDashboard, Database } from 'lucide-react';
import { Card } from '@/components/ui/card';

const features = [
  ['Excel/Word templates', 'Flexible placeholder engine for contracts/invoices/reports', FileSpreadsheet],
  ['Offline-safe licensing', 'Ed25519 signed activation keys verified in desktop app', ShieldCheck],
  ['Telegram automation', 'Quick license lookup and renew workflows', Bot],
  ['Fast generation', 'Batch render with PDF export, stamps and signatures', Zap],
  ['Admin panel', 'Manage users, tariffs, blocks and exports', LayoutDashboard],
  ['Scalable architecture', 'PostgreSQL + Redis + SSR + CDN-ready stack', Database],
] as const;

export function FeaturesGrid() {
  return (
    <section className='py-14'>
      <h2 className='text-3xl font-semibold'>Core capabilities</h2>
      <div className='mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-3'>
        {features.map(([title, desc, Icon]) => (
          <Card key={title}>
            <Icon className='h-5 w-5 text-primary' />
            <h3 className='mt-3 font-medium'>{title}</h3>
            <p className='mt-2 text-sm text-muted-foreground'>{desc}</p>
          </Card>
        ))}
      </div>
    </section>
  );
}
