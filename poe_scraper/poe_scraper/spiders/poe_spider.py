```python
import scrapy
from scrapy_splash import SplashRequest
from poe_scraper.items import PoeItem

class PoeSpider(scrapy.Spider):
    name = 'poe_spider'
    start_urls = ['http://www.poe.com/conversations']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        for conversation in response.css('div.conversation'):
            item = PoeItem()
            item['title'] = conversation.css('h2.title::text').extract_first()
            item['content'] = conversation.css('div.content::text').extract()
            yield item

        next_page = response.css('a.next::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```
This code creates a Scrapy spider for scraping conversations from Poe.com. It uses Scrapy-Splash to handle the dynamic content and infinite scrolling. The parse method extracts the title and content of each conversation and stores them in a PoeItem object. If there is a next page, it follows the link and continues scraping.