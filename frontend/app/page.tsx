import Link from 'next/link';

export default function Home() {
  return (
    <main>
      <h1>DocsGenTray</h1>
      <p>Оффлайн программа для генерации документов из Excel + Word/Excel шаблонов с PDF экспортом.</p>
      <nav>
        <Link href='/pricing'>Тарифы</Link> | <Link href='/docs'>Документация</Link> | <Link href='/blog'>Блог</Link> | <Link href='/faq'>FAQ</Link> | <Link href='/contacts'>Контакты</Link>
      </nav>
    </main>
  );
}
