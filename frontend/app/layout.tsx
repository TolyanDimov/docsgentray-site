import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'DocsGenTray — генератор документов из Excel',
  description: 'Оффлайн генератор документов по шаблонам Excel/Word с экспортом PDF и системой лицензирования.',
  openGraph: {
    title: 'DocsGenTray',
    description: 'Генерация документов из Excel в один клик',
    type: 'website',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='ru'>
      <body>{children}</body>
    </html>
  );
}
