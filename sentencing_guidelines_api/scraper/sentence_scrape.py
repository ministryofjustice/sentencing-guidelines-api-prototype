import requests
from bs4 import BeautifulSoup
import pprint

class OffenceScraper:
    def __init__(self):
        self.offences = {}
        self.base_url = "https://www.sentencingcouncil.org.uk/"

    def get_offences(self):
        response = requests.get(self.base_url+"/offences/")
        soup = BeautifulSoup(response.content, "html.parser")
        list_of_offences = soup.find("ul", {"class": "offences-filter-list"}).findAll("a")
        for loop_count, offence in enumerate(list_of_offences):
            offence_name = offence.string.strip()
            self.offences[offence_name] = {"path": offence.get('href')}
            response = requests.get(self.base_url + offence.get('href'))
            local_soup = BeautifulSoup(response.content, "html.parser")
            try:
                self.offences[offence_name]["act"] = self.get_act(local_soup);
            except AttributeError:
                self.offences[offence_name]["act"] = ""
            try:
                self.offences[offence_name]["effective_data"] = self.get_effective_date(local_soup).replace("\t", "")
            except AttributeError:
                self.offences[offence_name]["effective_data"] = ""
            print(loop_count, offence_name)
            # if loop_count > 50:
            #     break

    def get_act(self, soup):
        return soup.find("div", {"class": "offence-act"}).string.strip()

    def get_effective_date(self, soup):
        return soup.find("div", {"class": "offence-effective-date"}).contents[2]

    def export_date(self):
        with open("offence_dates.txt", "w") as outfile:
            for k, v in self.offences.items():
                outfile.write(k + ' => ' + str(v["effective_data"]) + "\n")


offence_scraper = OffenceScraper()
offence_scraper.get_offences()
pprint.pprint(offence_scraper.offences)

offence_scraper.export_date()

#for k, v in offence_scraper.offences.items():
#    print(v["effective_data"], type(v["effective_data"]))

# def get_offence():
#     response = requests.get("https://www.sentencingcouncil.org.uk/offences/magistrates-court/item/abstracting-electricity/")
#     soup = BeautifulSoup(response.content, "html.parser")
#     return soup.find("div", {"class": "offence-act"}).string.strip()

#
# def get_offences():
#     response = requests.get("https://www.sentencingcouncil.org.uk/offences/")
#     soup = BeautifulSoup(response.content, "html.parser")
#     list_of_offences = soup.find("ul", {"class": "offences-filter-list"}).findAll("a")
#     offences = {}
#     for offence in list_of_offences:
#         offences[offence.string.strip()]= {"path": offence.get('href')}
#
#     return offences

# pprint.pprint(get_offences())



