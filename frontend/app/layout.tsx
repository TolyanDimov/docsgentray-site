import './globals.css';
import type { Metadata } from 'next';
import { Nav } from '@/components/Nav';

export const metadata: Metadata = {
  title: 'DocsGenTray — генератор документов из Excel',
  description: 'Оффлайн генератор документов по шаблонам Excel/Word с экспортом PDF и системой лицензирования.',
  openGraph: {
    title: 'DocsGenTray',
    description: 'Генерация документов из Excel в один клик',
    type: 'website',
  },
};

const orgSchema = {
  '@context': 'https://schema.org',
  '@type': 'SoftwareApplication',
  name: 'DocsGenTray',
  applicationCategory: 'BusinessApplication',
  operatingSystem: 'Windows',
  offers: {
    '@type': 'Offer',
    priceCurrency: 'RUB',
    price: '1990',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='ru'>
      <body>
        <Nav />
        {children}
        <script type='application/ld+json' dangerouslySetInnerHTML={{ __html: JSON.stringify(orgSchema) }} />
      </body>
    </html>
  );
}
