import Link from 'next/link';
import { ThemeToggle } from '@/components/theme-toggle';

const items = [
  ['Home', '/'],
  ['Features', '/features'],
  ['Pricing', '/pricing'],
  ['Documentation', '/docs'],
  ['Blog', '/blog'],
  ['FAQ', '/faq'],
  ['Contact', '/contact'],
  ['Auth', '/auth'],
  ['Dashboard', '/dashboard'],
  ['Admin', '/admin'],
] as const;

export function Nav() {
  return (
    <header className='sticky top-0 z-50 border-b border-border/70 bg-background/70 backdrop-blur'>
      <div className='mx-auto flex h-16 max-w-7xl items-center justify-between px-4'>
        <Link href='/' className='font-semibold'>DocsGenTray</Link>
        <nav className='hidden gap-4 md:flex'>
          {items.map(([label, href]) => (
            <Link key={href} href={href} className='text-sm text-muted-foreground hover:text-foreground'>
              {label}
            </Link>
          ))}
        </nav>
        <ThemeToggle />
      </div>
    </header>
  );
}
