## laws_project_crawler

#### Version
Status: Development

Start date: 03/02/2020

#Crawler
#### How to run
1/ Manual Mode
```sh
    $ python3 crawl_data.py -m manual
```
Prompt for inputs as:
1. Crawl check with latest version
2. Crawl check with latest version having largest transform data
3. Crawl check custom version (**user need to input path to transform folder**)
4. Crawl without checking

After running option 1,2 or 3, a prompt specifies merging with that version (choosing Y/N)

2/ Auto mode
```sh
    $ python3 crawl_data.py -m auto
```
Auto mode will auto check for latest version and merge with that version
###Ouput 
Root directory: **.../vnu_law/crawler/<thuvienphapluat.vn/vbpl.vn>/<YYYYMMDD_HHMMSS>**

Sub directories include:

* Directory stores sitemap content: _sitemaps_
* Directory store document errors after crawling: _errors_
* Directory stores urls of law documents: _urls/urls.lines_
* Directory stores law documents with JSON schema: _transform_
* Log folder contains information of crawler: _crawl.done.txt_

#Importer
###How to run
```shell script
    $ pyhon3 import_data.py -m <mode> -p <path_to_data/transform>
```
Manual mode prompt will be displayed as
1. Import to Postgresql
2. Import to Elasticsearch
3. Import to both (Postgresql then Elasticsearch)

Auto mode will perform options 3 of manual mode


#Crawler and Importer working together
```shell script
    $ pyhon3 crawl_then_import.py
```
performs auto crawler then auto import

##Note:
If auto crawler finds no change in thuvienphapluat.vn and vbpl.vn, it will sleep for 2 days. Switching to manual is recommended 