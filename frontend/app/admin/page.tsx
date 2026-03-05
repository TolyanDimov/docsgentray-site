const columns = ['ID', 'Email', 'Телефон', 'Telegram', 'Device fingerprint', 'License key', 'Тариф', 'Дата активации', 'Дата окончания', 'Статус', 'Дата регистрации'];

export default function AdminPage() {
  return (
    <main>
      <h1>Админ-панель</h1>
      <p>Поддерживаются поиск, сортировка, фильтры, пагинация и экспорт CSV/Excel через backend API.</p>
      <table>
        <thead>
          <tr>{columns.map((column) => <th key={column}>{column}</th>)}</tr>
        </thead>
      </table>
    </main>
  );
}
