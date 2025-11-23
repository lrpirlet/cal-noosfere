info='''
<div>
 <br/>
 <a class="undertag" href="/tags/tag_content.asp?tag=1" title="">
  science-fiction
 </a>
 <a class="undertag" href="/tags/tag_content.asp?tag=139" title="">
  origine :  États-Unis
 </a>
</div>
'''

from bs4 import BeautifulSoup as BS

soup = BS(info, "html5lib" )

for br in soup.find_all('br'):
    hr = soup.new_tag('hr')
    br.replace_with(hr)

print(soup.prettify())
