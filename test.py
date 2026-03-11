from collections import deque
import click
from mygeotab import API, dates
import asyncio
import datetime
import pytz
import logging
import psycopg2
import pprint
import re
# import nest_asyncio
# nest_asyncio.apply()

exceptionIds=deque()

api = API(database='intcesetti', username='mt@cesetti.com.ar', password='Mt.cesetti7023', server='my.geotab.com')
api.authenticate()
logging.basicConfig(filename='ROUTELog.log', format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')


# mySearch = {"fromDate": "2025-11-17T15:45:00.000-03:00",  "deviceSearch": {"id": 'b2AF'}}

# mySearch = {"fromDate": "2025-08-01T00:00:00.000-03:00", 'ruleSearch': {'id': 'aS-6G-1AZWUazLcsp_NBTUw'}}
myPropSelDevice={'fields':['id','activeFrom','activeTo','devicePlanBillingInfo','deviceType','licensePlate','name','serialNumber'], 'isIncluded':True}

        mySearch={}
        ret = api.get(
                'Device',
                search=mySearch,
                resultsLimit = None,
                property_selector=myPropSelDevice
            )




def getRoutes():











