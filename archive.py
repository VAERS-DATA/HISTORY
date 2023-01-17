#!/usr/bin/env python

import os
import sys

from vaers_downloader import download

from datetime import date

download.downloadVAERSdata([date.today().year], os.getcwd())
