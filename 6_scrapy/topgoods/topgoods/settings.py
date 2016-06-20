# -*- coding: utf-8 -*-

# Scrapy settings for topgoods project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'topgoods'

SPIDER_MODULES = ['topgoods.spiders']
NEWSPIDER_MODULE = 'topgoods.spiders'


LOG_FILE = "scrapy.log"