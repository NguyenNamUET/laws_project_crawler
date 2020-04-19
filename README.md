## laws_project_crawler

#### Version
Status: Development

Start date: 03/02/2020

#Crawler
#### How to run
```sh
    $ python3 crawl_thuvienphapluat.py   
```

###Ouput 
Root directory: **.../vnu_law/crawler/thuvienphapluat.vn/<YYYYMMDD_HHMMSS>**

Sub directories include:

* Directory stores sitemap content: _sitemaps_
* Directory store document errors after crawling: _errors_
* Directory stores urls of law documents: _urls/urls.lines_
* Directory stores law documents with JSON schema: _transform_
* Log folder contains information of crawler: _crawl.done.txt_

#Importer
###How to run
```shell script
    $ pyhon3 import_data_thuvienphapluat.py <path to Directory stores law documents with JSON schema>
```
For example:
```shell script
    $pyhon3 import_data_thuvienphapluat.py /vnu_law/my_crawler/thuvienphapluat.vn/<YYYYMMDD_HHMMSS>/transform
```