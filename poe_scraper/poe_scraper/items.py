```python
import scrapy

class PoeItem(scrapy.Item):
    # define the fields for your item here like:
    conversation = scrapy.Field()
    date = scrapy.Field()
    user = scrapy.Field()
```