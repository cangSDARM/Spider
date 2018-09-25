										Scrapy
Scrapy 爬虫框架
   +--------------+				   +---------+
   |Item Piperline|				   |Scheduler| ---------------------+
   +------|-------+				   +----|----+						|
		  ^								^							|
		data						 Requests						|
		  |								|							|
		  |								|							|
		  |							   else							|
		  |							  	|							|
		  +--------------------< if needed data get					|
										|							|
						   +------------|-----------+				|
						   |						---<'Requests'<-+
						   |		 Scrapy			----------->'Requests'>----------+
						   |					 	-----------<'Responses'<-----Downloader
						   |	  	 Engine			|
						   |						----------------+
						   +------------|-----------+				|
										^							|
								   Middlewares						|
										|							|
								   +-------+						|
								   |Spiders|------<'Responses'<-----+
								   +-------+