import requests
from bs4 import BeautifulSoup
from dateparser.search import search_dates


import time
import requests
from bs4 import BeautifulSoup
from dateparser.search import search_dates


class OffenceScraper:
    def __init__(self):
        self.base_url = "https://www.sentencingcouncil.org.uk/"

    def get_offences(self, limit = 0):
        response = requests.get(self.base_url+"/offences/")
        soup = BeautifulSoup(response.content, "html.parser")
        list_of_offences = soup.find("ul", {"class": "offences-filter-list"}).findAll("a")
        for loop_count, offence in enumerate(list_of_offences):
            if limit > 0 and loop_count >= limit:
                break
            offence_name = offence.string.strip()
            offence_data = {
                "name": offence_name,
                "path": offence.get('href')
            }
            response = requests.get(self.base_url + offence.get('href'))
            local_soup = BeautifulSoup(response.content, "html.parser")
            try:
                offence_data["act"] = self.get_act(local_soup);
            except AttributeError:
                offence_data["act"] = ""
            try:
                offence_data["effective_date"] = self.get_effective_date(local_soup, offence.get('href'))
            except AttributeError:
                offence_data["effective_date"] = ""
            # print(loop_count, offence_name)
            offence_data["raw_date"] = self.get_raw_effective_date(local_soup)
            yield offence_data

    def get_act(self, soup):
        return soup.find("div", {"class": "offence-act"}).string.strip()

    def get_effective_date(self, soup, url):
        dates = search_dates(soup.findAll("div", {"class": ["offence-effective-date", "overarching-effective-date"]})[0].contents[2],  languages=['en'])
        if dates:
            for date in dates:
                return date[1]
        else:
            return None

    def get_raw_effective_date(self, soup):
        effective_date_area = soup.find("div", {"class": "offence-effective-date"})
        if effective_date_area:
            effective_date_text = effective_date_area.contents[2]
            # effective date can be line of text with the last 3 "words" holding d/m/y
            # so split the text on " " and keep just the final three elements
            date_elements = effective_date_text.split(" ")[-3:]
            # Also need to remove pesky tab characters
            effective_date = " ".join(date_elements).replace("\t", "")
        else:
            effective_date = ""
        return effective_date

    def export_date(self):
        with open("offence_dates.txt", "w") as outfile:
            for k, v in self.offences.items():
                outfile.write(k + ' => ' + str(v["effective_data"]) + "\n")


def list_to_csv_row(filename, mylist, separator="\t", show=True):
    with open(filename, "a") as outfile:
        line = separator.join(mylist)
        if show:
            print(line)
        outfile.write(line + "\n")

if __name__ == "__main__":

    # Scrape the data and write to tsv file
    # Also compare to ways of extracting effective date

    go = OffenceScraper()
    offences = go.get_offences()

    filename = time.strftime("scrape_data(%Y-%m-%d_%H.%M.%S).tsv")

    for count, offence in enumerate(offences):
        # Write column headings on 1st iteration, plus extra heading for date comparison
        if count == 0:
            list_to_csv_row(filename, list(offence.keys()) + ["Dates Match"])
        # See if dateparser effective date looks same as non-dateparser one
        # using strip("0") as presence/absence of leading zero probably good enough match
        try:
            reformatted_effective_date = offence["effective_date"].strftime("%d %B %Y")
        except AttributeError:
            reformatted_effective_date = ""

        match = str(reformatted_effective_date.strip("0") == offence["raw_date"].strip("0"))
        # Write offence data + date match outcome
        list_to_csv_row(filename, [str(v) for v in offence.values()] + [match])
        ##if count > 3: break
    print("Finished")

