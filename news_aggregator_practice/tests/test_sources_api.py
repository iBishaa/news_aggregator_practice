from fastapi.testclient import TestClient
from backend.app import app
from config import STUDENT_ID

client = TestClient(app)

def test_get_empty_sources():
    res = client.get(f"/sources/{STUDENT_ID}")
    assert res.status_code == 200
    assert res.json() == {"sources": []}

def test_add_and_get_source():
    res1 = client.post(f"/sources/{STUDENT_ID}", json={"url": "<https://example.com/rss>"})
    assert res1.status_code == 200
    assert "<https://example.com/rss>" in res1.json()["sources"]
    res2 = client.get(f"/sources/{STUDENT_ID}")
    assert res2.json()["sources"] == ["<https://example.com/rss>"]
def test_fetch_custom_feed(monkeypatch):
    news_store.clear(); sources_store.clear()

    client.post(f"/sources/{STUDENT_ID}", json={"url": "http://test.com/rss"})

    class DummyFeed:
        entries = [{"title": "X", "link": "L", "published": "2025-04-28"}]

    monkeypatch.setattr(feedparser, "parse", lambda _: DummyFeed)

    r = client.post(f"/fetch/{STUDENT_ID}")
    assert r.json() == {"fetched": 1}
