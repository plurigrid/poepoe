```python
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from .items import PoeItem

class PoeSpider(CrawlSpider):
    name = 'poe'
    allowed_domains = ['poe.com']
    start_urls = ['http://www.poe.com/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.page_next',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        item = PoeItem()
        item['url'] = response.url
        item['title'] = response.css('h1::text').get()
        item['content'] = response.css('.content::text').getall()
        yield item
```