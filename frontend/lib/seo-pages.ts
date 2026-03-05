export type SeoPage = { slug: string; title: string; description: string; h1: string; body: string };

const occupations = ['lawyers','accountants','hr','sales','procurement','construction','medical','education','finance','manufacturing','logistics','real-estate','consulting','insurance','banking','government','retail','it','legal','auditors'];
const intents = ['document-generator-from-excel','excel-contract-generator','automatic-document-generation','template-automation','pdf-export','mail-merge','offline-document-generator','contract-builder','invoice-builder','report-generator','word-template-engine'];

export const seoPages: SeoPage[] = occupations.flatMap((occ) =>
  intents.map((intent) => {
    const slug = `${intent}-for-${occ}`;
    return {
      slug,
      title: `${intent.replaceAll('-', ' ')} для ${occ} | DocsGenTray`,
      description: `DocsGenTray автоматизирует ${intent.replaceAll('-', ' ')} для ${occ}. Оффлайн, безопасно, с PDF экспортом.`,
      h1: `Генерация документов (${intent}) для ${occ}`,
      body: `Ускорьте работу команды ${occ}. Используйте шаблоны Word/Excel и данные из Excel для массовой генерации документов.`
    };
  })
);
