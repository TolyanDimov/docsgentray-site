import Link from 'next/link';

export default function Home() {
  return (
    <main>
      <h1>DocsGenTray</h1>
      <p>Оффлайн программа для генерации документов из Excel + Word/Excel шаблонов с PDF экспортом.</p>
      <ul>
        <li>Генерация документов из выделенных строк Excel</li>
        <li>Поддержка шаблонов Word/Excel и плейсхолдеров</li>
        <li>Опции PDF, печатей, штампов и подписей</li>
      </ul>
      <p>
        <Link href='/pricing'>Купить лицензию</Link>
      </p>
    </main>
  );
}
