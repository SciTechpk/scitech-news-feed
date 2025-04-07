import feedparser
from datetime import datetime

# List of RSS feeds
FEEDS = [
    "http://feeds.bbci.co.uk/news/rss.xml",
    "http://rss.cnn.com/rss/edition.rss",
    "http://feeds.reuters.com/reuters/topNews",
    "http://www.aljazeera.com/xml/rss/all.xml",
    "https://www.espn.com/espn/rss/news",
    "https://apnews.com/rss",
    "https://arynews.tv/en/feed/"
]

# Final Beautiful HTML Generator
def generate_html(news_items):
    html_content = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Latest News Feed</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            color: #0077cc;
        }}
        .news-item {{
            background-color: #fff;
            margin-bottom: 20px;
            padding: 15px 20px;
            border-left: 5px solid #0077cc;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-radius: 8px;
        }}
        .news-item h2 {{
            font-size: 20px;
            margin: 0 0 10px;
            color: #0077cc;
        }}
        .news-item p {{
            margin: 5px 0;
        }}
        .news-item time {{
            font-size: 12px;
            color: #888;
        }}
        a {{
            text-decoration: none;
            color: #0077cc;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Latest News (Updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')})</h1>
"""

    for item in news_items:
        html_content += f"""
    <div class=\"news-item\">
        <h2><a href=\"{item['link']}\" target=\"_blank\">{item['title']}</a></h2>
        <p>{item['summary']}</p>
        <time>{item['published']}</time>
    </div>
"""

    html_content += """
</body>
</html>
"""
    return html_content

# Fetch feed data
def fetch_news():
    items = []
    for url in FEEDS:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:3]:
                items.append({
                    "title": entry.get("title", "No Title"),
                    "link": entry.get("link", "#"),
                    "summary": entry.get("summary", ""),
                    "published": entry.get("published", "Unknown date")
                })
        except Exception as e:
            print(f"\u274c Failed to fetch from {url}: {e}")
    return items

# Generate and write HTML file
if __name__ == "__main__":
    news = fetch_news()
    html = generate_html(news)
    with open("news_latest.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("\u2705 Fully styled news_latest.html generated successfully!")