import './globals.css';
import type { Metadata } from 'next';
import { Nav } from '@/components/Nav';
import { ThemeProvider } from '@/components/theme-provider';

export const metadata: Metadata = {
  title: 'DocsGenTray — Modern SaaS for document generation',
  description: 'Automate document generation from Excel with secure offline licensing and modern SaaS UX.',
  openGraph: {
    title: 'DocsGenTray',
    description: 'Modern SaaS platform for document automation',
    type: 'website',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='en' suppressHydrationWarning>
      <body>
        <ThemeProvider>
          <Nav />
          <main className='mx-auto max-w-7xl px-4'>{children}</main>
        </ThemeProvider>
      </body>
    </html>
  );
}
