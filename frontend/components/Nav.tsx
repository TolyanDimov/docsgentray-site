import Link from 'next/link';

export function Nav() {
  return (
    <nav className='space-x-4 py-4'>
      <Link href='/'>Главная</Link>
      <Link href='/pricing'>Тарифы</Link>
      <Link href='/docs'>Документация</Link>
      <Link href='/blog'>Блог</Link>
      <Link href='/faq'>FAQ</Link>
      <Link href='/contacts'>Контакты</Link>
      <Link href='/register'>Регистрация</Link>
      <Link href='/cabinet'>Личный кабинет</Link>
      <Link href='/admin'>Админ</Link>
    </nav>
  );
}
