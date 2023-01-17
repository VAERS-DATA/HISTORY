#!/usr/bin/env python

import os
import sys

from vaers_downloader import download

from datetime import date

download.downloadVAERSdata([i for i in range(2019, date.today().year)], os.getcwd())
