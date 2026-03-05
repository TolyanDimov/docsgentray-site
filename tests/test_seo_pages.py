from pathlib import Path


def test_seo_generation_count():
    content = Path('frontend/lib/seo-pages.ts').read_text(encoding='utf-8')
    assert 'occupations' in content
    assert 'intents' in content
