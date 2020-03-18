# ScrapyTutorial
This was created from a YouTube video series:
https://www.youtube.com/watch?v=OlAouS669bc

	Basic steps
  
  1) Create new project
	2) Add virtual environment (settings -> install "Scrapy")
	

	3) Go to terminal and enter "scrapy startproject quotetutorial"
	
	
	
	
Scaping to a database:

	1) Configure the pipeline.py file:
	class QuotetutorialPipeline(object):
	        def __init__(self):
	                self.create_connection()
	                self.create_table()
	
	
	        def create_connection(self):
	                self.conn = sqlite3.connect('myquotes.db')
	                self.curr = self.conn.cursor()
	
	        def create_table(self):
	                self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
	                self.curr.execute("""create table quotes_tb (
	title text,
	author text,
	tag text)
	""")
	
	        def process_item(self, item, spider):
	                self.store_db(item)
	#
	#         print("Pipeline : " +  item ['title'][0])
	                return item
	#
	        def store_db(self, item):
	                self.curr.execute("""insert into quotes_tb values (?,?,?)""",(
	
	                        item['title'][0],
	                        item['author'][0],
	                        item['tag'][0]))
	
	                self.conn.commit()
	
	2) Enable the pipeline to be used in the config file:
	ITEM_PIPELINES = {
	      'quotetutorial.pipelines.QuotetutorialPipeline': 300,
	}
	
  3) Add the class to the items.py file:
	import scrapy
	
	
	class QuotetutorialItem(scrapy.Item):
	        # define the fields for your item here like:
	        title = scrapy.Field()
	        author = scrapy.Field()
	        tag = scrapy.Field()
	
	4) Create the spider to call the functions to scrape & store the data items -> pipeline -> database
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
	                        yield items5) Run the crawler
	
	Database file is created with table containing the scraped data:
	
	  The file can be opened here:
	https://sqliteonline.com/
	
