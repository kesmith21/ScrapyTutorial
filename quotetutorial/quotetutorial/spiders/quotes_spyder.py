import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    # from Tutorial #16
    def parse(self, response):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

    #from Tutorial 11
    # https://www.youtube.com/watch?v=cC9aFbViT_c&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=11
    # def parse(self, response):
    #     all_div_quotes = response.css('div.quote')
    #     title = all_div_quotes.css('span.text::text').extract()
    #     author = all_div_quotes.css('.author::text').extract()
    #     tag = all_div_quotes.css('.tag::text').extract()
    #     yield {
    #         'title': title,
    #         'author': author,
    #         'tag': tag
    #     }


    # from Tutorial #12
    # def parse(self, response):
    #     items = QuotetutorialItem()
    #
    #     for quotes in response.css('div.quote'):
    #             title = quotes.css('span.text::text').extract()
    #             author = quotes.css('.author::text').extract()
    #             tag = quotes.css('.tag::text').extract()
    #
    #             items['title'] = title
    #             items['author'] = author
    #             items['tag'] = tag
    #             yield items

                # 'title': quote.css('span.text::text').get(),
                # 'author': quote.css('small.author::text').get(),
                # 'tags': quote.css('div.tags a.tag::text').getall(),


    # from Tutorial #14
    # def parse(self, response):
    #     items = QuotetutorialItem()
    #
    #     all_div_quotes = response.css('div.quote')
    #
    #     for quotes in all_div_quotes:
    #         title = quotes.css('span.text::text').extract()
    #         author = quotes.css('.author::text').extract()
    #         tag = quotes.css('.tag::text').extract()
    #
    #         items['title'] = title
    #         items['author'] = author
    #         items['tag'] = tag
    #
    #         yield items

    # def parse(self, response):
    #         title = response.css('title::text').extract()
    #         author = response.css('.author::text').extract()
    #         # print(title)
    #         yield {'titletext': title, 'author': author}







