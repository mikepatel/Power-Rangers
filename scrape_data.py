"""


"""
################################################################################
# Imports
import os
import re
import pandas
import urllib.request
import requests
from bs4 import BeautifulSoup

################################################################################
# Main
if __name__ == "__main__":
    html = """
    <ul aria-describedby="asst2200">
    <li><span class="itemnum">2200</span> <a href="/toys/pictures/bandai/02200_5.jpg" class="item" aria-expanded="false" role="button">Billy Blue Ranger</a> <ul class="toyutility noprint" tabindex="-1" hidden=""><li class="picbtn"><a class="picbtn-btn" data-lightbox="Billy Blue Ranger (2200)" href="/toys/pictures/bandai/02200_5.jpg" role="button"><span>View</span> <span>Photo</span><span class="srtext"> (2200)</span></a></li><li class="UPCbtn"><a class="upcbtn-btn" data-lightbox="2200 Billy Blue Ranger" data-title="0 45557 02200 6" href="/toys/upcs/bandai/04555702200.png" role="button"><span>View</span> <span>UPC</span><span class="srtext"> (2200)</span></a></li><li class="amzbtn"><a rel="external nofollow sponsored" class="external-link" href="https://www.amazon.com/gp/product/B003J8R7KG/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B003J8R7KG&amp;linkCode=as2&amp;tag=grnrncom-20"><span>Buy</span> <span>Item</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="ebay"><a rel="external nofollow sponsored" class="external-link" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?&amp;campid=5338165879&amp;customid=link&amp;mpre=https://www.ebay.com/sch/i.html?_nkw=045557022006&amp;_rdc=1"><span>Browse</span> <span>eBay</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="last" aria-hidden="true"><button class="close-btn" type="button"><img src="/images/svg/close-btn.svg" alt="Close"></button></li></ul><span class="wavedate">[Fall 1993]</span></li><li><span class="itemnum">2200</span> <a href="/toys/pictures/bandai/02200_3.jpg" class="item" aria-expanded="false" role="button">Zach Black Ranger</a> <ul class="toyutility noprint" tabindex="-1" hidden=""><li class="picbtn"><a class="picbtn-btn" data-lightbox="Zach Black Ranger (2200)" href="/toys/pictures/bandai/02200_3.jpg" role="button"><span>View</span> <span>Photo</span><span class="srtext"> (2200)</span></a></li><li class="UPCbtn"><a class="upcbtn-btn" data-lightbox="2200 Zach Black Ranger" data-title="0 45557 02200 6" href="/toys/upcs/bandai/04555702200.png" role="button"><span>View</span> <span>UPC</span><span class="srtext"> (2200)</span></a></li><li class="amzbtn"><a rel="external nofollow sponsored" class="external-link" href="https://www.amazon.com/gp/product/B002BZKJC6/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B002BZKJC6&amp;linkCode=as2&amp;tag=grnrncom-20"><span>Buy</span> <span>Item</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="ebay"><a rel="external nofollow sponsored" class="external-link" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?&amp;campid=5338165879&amp;customid=link&amp;mpre=https://www.ebay.com/sch/i.html?_nkw=045557022006&amp;_rdc=1"><span>Browse</span> <span>eBay</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="last" aria-hidden="true"><button class="close-btn" type="button"><img src="/images/svg/close-btn.svg" alt="Close"></button></li></ul><span class="wavedate">[Fall 1993]</span></li><li><span class="itemnum">2200</span> <a href="/toys/pictures/bandai/02200_4.jpg" class="item" aria-expanded="false" role="button">Trini Yellow Ranger</a> <ul class="toyutility noprint" tabindex="-1" hidden=""><li class="picbtn"><a class="picbtn-btn" data-lightbox="Trini Yellow Ranger (2200)" href="/toys/pictures/bandai/02200_4.jpg" role="button"><span>View</span> <span>Photo</span><span class="srtext"> (2200)</span></a></li><li class="UPCbtn"><a class="upcbtn-btn" data-lightbox="2200 Trini Yellow Ranger" data-title="0 45557 02200 6" href="/toys/upcs/bandai/04555702200.png" role="button"><span>View</span> <span>UPC</span><span class="srtext"> (2200)</span></a></li><li class="amzbtn"><a rel="external nofollow sponsored" class="external-link" href="https://www.amazon.com/gp/product/B002DE1032/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B002DE1032&amp;linkCode=as2&amp;tag=grnrncom-20"><span>Buy</span> <span>Item</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="ebay"><a rel="external nofollow sponsored" class="external-link" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?&amp;campid=5338165879&amp;customid=link&amp;mpre=https://www.ebay.com/sch/i.html?_nkw=045557022006&amp;_rdc=1"><span>Browse</span> <span>eBay</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="last" aria-hidden="true"><button class="close-btn" type="button"><img src="/images/svg/close-btn.svg" alt="Close"></button></li></ul><span class="wavedate">[Fall 1993]</span></li><li><span class="itemnum">2200</span> <a href="/toys/pictures/bandai/02200_2.jpg" class="item" aria-expanded="false" role="button">Kimberly Pink Ranger</a> <ul class="toyutility noprint" tabindex="-1" hidden=""><li class="picbtn"><a class="picbtn-btn" data-lightbox="Kimberly Pink Ranger (2200)" href="/toys/pictures/bandai/02200_2.jpg" role="button"><span>View</span> <span>Photo</span><span class="srtext"> (2200)</span></a></li><li class="UPCbtn"><a class="upcbtn-btn" data-lightbox="2200 Kimberly Pink Ranger" data-title="0 45557 02200 6" href="/toys/upcs/bandai/04555702200.png" role="button"><span>View</span> <span>UPC</span><span class="srtext"> (2200)</span></a></li><li class="amzbtn"><a rel="external nofollow sponsored" class="external-link" href="https://www.amazon.com/gp/product/B001DXT5PO/ref=as_li_ss_tl?ie=UTF8&amp;camp=1789&amp;creative=390957&amp;creativeASIN=B001DXT5PO&amp;linkCode=as2&amp;tag=grnrncom-20"><span>Buy</span> <span>Item</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="ebay"><a rel="external nofollow sponsored" class="external-link" href="https://rover.ebay.com/rover/1/711-53200-19255-0/1?&amp;campid=5338165879&amp;customid=link&amp;mpre=https://www.ebay.com/sch/i.html?_nkw=045557022006&amp;_rdc=1"><span>Browse</span> <span>eBay</span><span class="srtext hcm-nobg-srtext"> (off-site link)</span></a></li><li class="last" aria-hidden="true"><button class="close-btn" type="button"><img src="/images/svg/close-btn.svg" alt="Close"></button></li></ul><span class="wavedate">[Fall 1993]</span></li>
    </ul>
    
    <ul aria-describedby="asst2201">
    
    </ul>

    """

    html = requests.get("https://www.grnrngr.com/toys/power-rangers/mighty-morphin")

    soup = BeautifulSoup(html.text, "html.parser")

    itemnums = []
    names = []
    dates = []

    # toylistings div
    toylistings = soup.find("div", {"class": "toylistings"})

    # All ul under toylistings
    uls = toylistings.find_all("ul", recursive=False)
    for ul in uls:
        try:
            lis = ul.find_all("li", recursive=False)

            for li in lis:
                # item number
                itemnum = li.find("span", {"class": "itemnum"}).text.strip()
                itemnums.append(itemnum)

                # name
                name = li.find("a").text.strip()
                names.append(name)

                # date
                date = li.find("span", {"class": "wavedate"}).text.strip()
                date = re.sub("\[|\]", "", date)
                dates.append(date)

        except AttributeError as e:
            date = li.find("span", {"class": "wavedate"})
            if date is None:
                dates.append(None)
            continue

    #print(itemnums)
    #print(names)
    #print(dates)
