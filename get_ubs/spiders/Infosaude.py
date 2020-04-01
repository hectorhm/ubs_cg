# -*- coding: utf-8 -*-
import scrapy


class InfosaudeSpider(scrapy.Spider):
    name = 'Infosaude'
    allowed_paths = ['http://infosaude.com.br']
    start_urls = ['http://infosaude.com.br/cities/4278/']

    def parse(self, response):
        divs = response.xpath("/html/body/div/div/div/div/div")
        for div in divs:
        	url = div.xpath('.//h2/a/@href').extract_first()
        	formed_url = "https://www.infosaude.com.br" + url
        	

        	yield scrapy.Request(url= formed_url, callback=self.parse_detail)

        	

    def parse_detail(self,response):
    	nome = response.xpath('/html/body/div/div/div[2]/h1/text()').extract_first()

    	div_endereco = response.xpath('/html/body/div/div/div[2]/div[2]/div[2]')
    	telefone = div_endereco.xpath('.//p[1]/a/text()').extract_first()
    	id_cnes = div_endereco.xpath('.//p[2]/span/text()').extract_first()
    	rua = div_endereco.xpath('.//p[3]/span/text()').extract_first()
    	cidade = div_endereco.xpath('.//p[4]/span/a/text()').extract_first()

    	div_informacao = response.xpath('/html/body/div/div/div[2]/div[3]/div[2]')
    	srefa = div_informacao.xpath('.//p[1]/span/text()').extract_first() #Situação em relação a estrutura física e ambiência
    	sradi = div_informacao.xpath('.//p[2]/span/text()').extract_first() #Situação em relação a adaptações para deficientes e idosos
    	sre = div_informacao.xpath('.//p[3]/span/text()').extract_first() #Situação em relação aos equipamentos
    	srm = div_informacao.xpath('.//p[4]/span/text()').extract_first() #ituação em relação aos Mediacamentos

    	yield {
        		'nome': nome,
        		'telefone': telefone,
        		'rua': rua,
        		'cidade': cidade,
        		'id_cnes':id_cnes,
        		'srefa': srefa,
        		'sradi': sradi,
        		'sre': sre,
        		'srm': srm, 
        	}


