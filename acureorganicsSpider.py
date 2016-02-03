import scrapy

class AcureorganicsSpider(scrapy.Spider):
    name = 'AcureorganicsSpider'
    allowed_domains = ["www.acureorganics.com"]
    start_urls = ['http://www.acureorganics.com/Acure-Organics-Facial-Products-s/28.htm','http://www.acureorganics.com/category-s/172.htm','http://www.acureorganics.com/category-s/169.htm',
'http://www.acureorganics.com/Acure-Organics-Facial-Cleansers-s/88.htm',
'http://www.acureorganics.com/Acure-Organics-Facial-Toners-s/87.htm',
'http://www.acureorganics.com/Acure-Organics-Facial-Moisturizers-s/85.htm',
'http://www.acureorganics.com/category-s/152.htm',
'http://www.acureorganics.com/Acure-Organics-Facial-Treatments-s/82.htm',
'http://www.acureorganics.com/category-s/168.htm',
'http://www.acureorganics.com/category-s/156.htm',
'http://www.acureorganics.com/category-s/157.htm',
'http://www.acureorganics.com/category-s/153.htm',
'http://www.acureorganics.com/category-s/145.htm',
'http://www.acureorganics.com/category-s/151.htm',
'http://www.acureorganics.com/Acure-Organics-Body-Lotions-and-Creams-s/78.htm',
'http://www.acureorganics.com/Acure-Organics-Lip-Products-s/26.htm',
'http://www.acureorganics.com/Acure-Organics-Hair-Care-Products-s/140.htm?searching=Y&sort=2&cat=140&show=120&page=1',
'http://www.acureorganics.com/category-s/170.htm',]
    def parse(self, response):
        for href in response.css('a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
	try:
        	yield {'Product': response.css('.colors_productname::text').extract()[0],'PRICE': response.css('.colors_productprice::text').extract()[0],}
	except:
		pass
