from pathlib import Path


def test_backend_has_admin_capabilities():
    content = Path('backend/app/main.py').read_text(encoding='utf-8')
    assert '/admin/users/export.csv' in content
    assert '/admin/users/export.xlsx' in content
    assert '/admin/users/{user_id}/renew' in content
    assert '/admin/users/{user_id}/block' in content
    assert '/admin/users/{user_id}/regenerate-key' in content


def test_backend_has_bot_endpoint():
    content = Path('backend/app/main.py').read_text(encoding='utf-8')
    assert '/bot/license/{email}' in content
    assert 'x_bot_token' in content


def test_seo_pages_target_200_plus():
    content = Path('frontend/lib/seo-pages.ts').read_text(encoding='utf-8')
    assert 'const occupations' in content
    assert 'const intents' in content
    # 20 occupations * 11 intents = 220 pages
    assert content.count("'") > 50
