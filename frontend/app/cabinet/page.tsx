export default function CabinetPage() {
  return (
    <main>
      <h1>Личный кабинет</h1>
      <p>Здесь отображаются:</p>
      <ul>
        <li>email, телефон, telegram</li>
        <li>license key</li>
        <li>срок действия лицензии</li>
        <li>тариф</li>
        <li>fingerprint устройства</li>
        <li>статус (active/expired/blocked/inactive)</li>
      </ul>
      <p>Источник данных: endpoint <code>/me</code> backend API.</p>
    </main>
  );
}
