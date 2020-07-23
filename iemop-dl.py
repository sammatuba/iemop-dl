from datetime import datetime
from dateutil.relativedelta import relativedelta
from requests import Session
from zipfile import ZipFile
from io import BytesIO#, TextIOWrapper
#from csv import writer, reader
from concurrent.futures import ThreadPoolExecutor 
from iemop_marketdata import MarketData, constructor, DT_FORMAT
from pandas import date_range
import typer

def validate_datetime(dt, report_frequency: str):
    """
    Valid Formats: 
        1: yyyyddmmHHMM
        2: yyyyddmmHH
        2: yyyymmdd
        3. yyyymm
    """
    if type(dt) == datetime:
        return dt

    try:
        # remove all non-numeric characters
        dt = dt.translate(str.maketrans('','',"/-:")) 
        if len(dt) == 12: 
            _dt = datetime.strptime(dt, DT_FORMAT.get(1))
            minute = _dt.minute
            if minute != 0:
                raise Exception("Invalid datetime, minute cannot be nonzero")
            if (_dt.hour != 0) and (report_frequency == "D"):
                raise Exception("Entered datetime not available per report frequency (daily)")
            return _dt, DT_FORMAT.get(1)
        elif len(dt) == 10:
            _dt = datetime.strptime(dt, DT_FORMAT.get(2))
            if (_dt.hour != 0) and (report_frequency == "D"):
                raise Exception("Entered datetime not available per report frequency (daily)")
            return _dt, DT_FORMAT.get(2)
        elif len(dt) == 8:
            _dt = datetime.strptime(dt, DT_FORMAT.get(3))
            return _dt, DT_FORMAT.get(3)
        elif len(dt) == 6:
            _dt = datetime.strptime(dt, DT_FORMAT.get(4))
            return _dt, DT_FORMAT.get(4)
        else:
            raise Exception("Invalid datetime")

    except ValueError:
        raise ValueError(f"Invalid datetime format.")

def generate_url_list(marketdata: MarketData, dt_from: datetime, dt_until: datetime):
    if dt_until >= dt_from:
        dt_range = [datetime.strftime(dt, "%Y%m%d%H%M") for dt in date_range(start=dt_from, end=dt_until, freq=marketdata.FREQUENCY)]
        return list(map(marketdata.generate_url, dt_range))
    else:
        raise Exception("dt_until can't be earlier than dt_from")

def download(url):
    with Session() as session:
        header = session.head(url)
        # get content type and check if a zip file
        content_type = header.headers.get('Content-Type')
        file_size = float(header.headers.get('Content-Length')) / 1e6
        if content_type != 'application/zip':
            raise Exception("Not a zip file")
        else:
            print(f"Downloading file ({file_size} MB)...", flush=True)
            response = session.get(url, stream=True)
            # read byte-file into memory
            bytefile = response.content
            return bytefile

def verify_zipfile(bytefile, mode='r'):
    # read byte-file into memory
    file = BytesIO(bytefile)
    zipfile = ZipFile(file, mode)
    # check if zip file is valid by verifying that all files inside are .csv
    if not all(filename.endswith('.csv') for filename in zipfile.namelist()):
        raise Exception("Invalid zip file contents")
    else:
        #print("File has been successfully verified")
        if mode == 'r':
            return zipfile
        else:
            return ZipFile(file, mode)

"""
def process_zipfile(zipfile):
    # create csv writer
    header_saved = False
    with open('out.csv', mode='w', newline='') as fout:
        csv_writer = writer(fout, dialect='excel')

        for csvfilename in zipfile.namelist():
            with zipfile.open(csvfilename) as file:
                csv_reader = reader(TextIOWrapper(file, 'utf-8'), dialect='excel')
                
                header = next(csv_reader)
                # save header
                if header_saved == False:
                    # ?verify_header
                    csv_writer.writerow(header)
                    header_saved = True
                
                for row in csv_reader:
                    if "EOF" in row:
                        continue
                    else:
                        csv_writer.writerow(row)
    print("File has been successfully processed.")
"""
def main(dataname: str, dt_from: str, dt_until: str = None):
    #url = "http://www.iemop.ph/csv/iemop_data_MP/MP_202007130000.zip"
    marketdata = constructor(name=dataname)
    _dt_from, _format = validate_datetime(dt_from, marketdata.FREQUENCY)
    # set to single datetime if dt_until is not provided
    if not dt_until:
        _dt_from, _format = validate_datetime(dt_from, marketdata.FREQUENCY)
        if _format in [DT_FORMAT.get(1), DT_FORMAT.get(2)]: # hour or minute
            _dt_until = _dt_from
        elif _format == DT_FORMAT.get(3): # day
            #dt_from = _dt_from + relativedelta(hours=1)
            _dt_until = _dt_from + relativedelta(days=1) - relativedelta(hours=1)
        elif _format == DT_FORMAT.get(4): # month
            #dt_from = _dt_from + relativedelta(hours=1)
            _dt_until = _dt_from + relativedelta(months=1) - relativedelta(hours=1)
    else:
        _dt_until,_ = validate_datetime(dt_until, marketdata.FREQUENCY)

    url_list = generate_url_list(marketdata, _dt_from, _dt_until)
    with ThreadPoolExecutor(max_workers=10) as executor:
        result = executor.map(download, url_list)
        main_zipfile = ZipFile('out.zip', mode='w')
        print(f"Requested data from {_dt_from} until {_dt_until} for a total of {len(url_list)} {marketdata.FREQUENCYLONG} reports.")
        for item in result:
            zipfile_to_append = verify_zipfile(item)
            for filename in zipfile_to_append.namelist():
                info = zipfile_to_append.getinfo(filename)
                main_zipfile.writestr(info, zipfile_to_append.read(filename))
        main_zipfile.close()
        print("Done.")

if __name__ == "__main__":
    typer.run(main)