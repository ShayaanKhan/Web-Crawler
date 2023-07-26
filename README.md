# Web-Crawler
Its a webcrawler for finding any and all emails present on a website.
The user can set the starting page of a defined domain for the crawler to begin and it traverses all links within the domain.

PRE REQUISITES:
1. Have scrapy installed.
2. Have pandas installed (for optional duplicate remover)
3. Have re installed.
4. Have the latest version of python installed.

The crawler can be used through the command prompt or a terminal of an IDE such as VScode. The following steps provided below are for vscode:
1. Once the repository has been cloned onto the system, open the folder in vs code.
2. Open the terminal and navigate to the corrcet subfolder ( cd .\mailcrawl\mailcrawl\spiders)
3. Now you can run the spider from the terminal using th following command: scrapy runspider main_crawler.py -o output.csv
4. The results are saved in a cvs file within the spiders folder.

OPTIONAL:
Since there can be duplicated emails, a separate python file has been created to delete the duplicate emails. 
Simply run the emailAntidupe.py file, it will create a new csv file names output1.csv and delete the previous output.csv within the spiders folder.
However, for this to work, the file containing the duplicate entries must be named "output.csv". 
If it is not, you can either rename the file or edit the file path in the emailAntidupe.py file.

Key information.
The crawler respects robots.txt of any webpage.
The crawler does not use a proxy.
These settings can be changed. (View scrapy documentation for details steps)

Thanks for reading :)
