import { Card } from '@/components/ui/card';

export default function AdminPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Admin Panel</h1>
      <Card className='mt-6'>
        <p className='text-sm text-muted-foreground'>Users, licenses, tariffs, blocks, CSV/XLSX export, and operational controls.</p>
        <div className='mt-4 overflow-x-auto'>
          <table className='w-full text-left text-sm'>
            <thead><tr className='border-b'><th className='py-2'>ID</th><th>Email</th><th>Tariff</th><th>Status</th></tr></thead>
            <tbody><tr><td className='py-2'>1</td><td>admin@example.com</td><td>12m</td><td>active</td></tr></tbody>
          </table>
        </div>
      </Card>
    </section>
  );
}
