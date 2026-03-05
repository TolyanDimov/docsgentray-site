const columns = ['ID', 'Email', 'Телефон', 'Telegram', 'Device fingerprint', 'License key', 'Тариф', 'Дата активации', 'Дата окончания', 'Статус', 'Дата регистрации'];

export default function AdminPage() {
  return (
    <main>
      <h1>Админ-панель</h1>
      <p>Управление пользователями и лицензиями: поиск, фильтры, пагинация, экспорт CSV/Excel.</p>
      <p>
        API endpoints: <code>/admin/users</code>, <code>/admin/users/export.csv</code>, <code>/admin/users/export.xlsx</code>
      </p>
      <table>
        <thead>
          <tr>{columns.map((column) => <th key={column}>{column}</th>)}</tr>
        </thead>
      </table>
    </main>
  );
}
