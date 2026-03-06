import { Card } from '@/components/ui/card';

const posts = ['How to automate contract generation', 'Offline licensing best practices', 'Scaling document workflows to 1M users'];

export default function BlogPage() {
  return (
    <section className='py-12'>
      <h1 className='text-4xl font-bold'>Blog</h1>
      <div className='mt-6 grid gap-4'>
        {posts.map((post) => (
          <Card key={post}><h3 className='font-semibold'>{post}</h3><p className='text-sm text-muted-foreground mt-2'>Insights and tutorials from DocsGenTray team.</p></Card>
        ))}
      </div>
    </section>
  );
}
