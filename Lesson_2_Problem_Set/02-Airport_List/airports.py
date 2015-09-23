#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "html.parser")
        FullAirportList = soup.find(id="AirportList")
        options = FullAirportList.find_all("option")
        for option in options:
            if option["value"] != "AllMajors" \
                    and option["value"] != "AllOthers" \
                    and option["value"] != "All":
                data.append(option["value"])

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()