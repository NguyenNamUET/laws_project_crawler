from my_crawler.crawler_helper.url_helper import load_url


def get_url_from_page__vbpl(sitemap_url):
    sitemap_content = load_url(sitemap_url, return_content=True)
    doc_urls = []
    for doc_soup in sitemap_content.find_all("div", attrs={"class": "item"}):
        doc_url = "http://vbpl.vn/" + doc_soup.p.a["href"]
        doc_urls.append(doc_url)

    return doc_urls


def get_url_from_sitemap__thuvienphapluat(sitemap_content):
    return [url.text for url in sitemap_content.find_all("loc")]


def get_all_sitemaps_url(base_sitemap_url):
    base_sitemap_soup = load_url(base_sitemap_url, return_content=True)

    return get_url_from_sitemap__thuvienphapluat(base_sitemap_soup)


def get_all_document_url(sitemap_url):
    sitemap_soup = load_url(sitemap_url, return_content=True)

    return get_url_from_sitemap__thuvienphapluat(sitemap_soup)

