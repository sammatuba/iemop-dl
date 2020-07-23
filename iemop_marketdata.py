MARKET_DATA = {
    # Market Projections
    "DAPMP" : ("DAPMP", "MarketProjection", "DAPMP", "HOURLY", "iemop_data_DAP", "DAP"),
    "HAPMP" : ("HAPMP", "MarketProjection", "HAPMP", "HOURLY", "iemop_data_HAP", "HAP"),
    "WAPMP" : ("WAPMP", "MarketProjection", "WAPMP", "HOURLY", "iemop_data_WAP", "WAP"),
    # Real-time Dispatch: 
    "RTD" : ("RTD", "RealTimeDispatch", "RTD", "HOURLY", "iemop_data_RTD", "RTD"),
    # Constraint Violation
    "DAPCV" : ("DAPCV", "ConstraintViolation", "DAP", "HOURLY", "iemop_data_DAPCV", "DAPCV"),
    "HAPCV" : ("HAPCV", "ConstraintViolation", "HAP", "HOURLY", "iemop_data_HAPCV", "HAPCV"),
    "RTDCV" : ("RTDCV", "ConstraintViolation", "RTD", "HOURLY", "iemop_data_RTDCV", "RTDCV"),
    "WAPCV" : ("WAPCV", "ConstraintViolation", "WAP", "HOURLY", "iemop_data_WAPCV", "WAPCV"),
    # GWAP: http://www.iemop.ph/csv/iemop_data_GWAP/GWAP_202007170000.zip
    "GWAP" : ("GWAP", "GWAP", "GWAP", "HOURLY", "iemop_data_GWAP", "GWAP"),
    # LWAP: http://www.iemop.ph/csv/iemop_data_LWAP/LWAP_202007170000.zip
    "LWAP" : ("LWAP", "LWAP", "LWAP", "HOURLY", "iemop_data_LWAP", "LWAP"),
    # HVDC Limit
    "DAPHL" : ("DAPHL", "HVDCLimit", "DAP", "DAILY", "iemop_data_DAPHL", "DAPHL"),
    "HAPHL" : ("HAPHL", "HVDCLimit", "HAP", "DAILY", "iemop_data_HAPHL", "HAPHL"),
    "RTDHL" : ("RTDHL", "HVDCLimit", "RTD", "DAILY", "iemop_data_RTDHL", "RTDHL"),
    "WAPHL" : ("WAPHL", "HVDCLimit", "WAP", "DAILY", "iemop_data_DAPHL", "DAPHL"),
    # HVDC Schedule
    "DAPHS" : ("DAPHS", "HVDCSchedule", "DAP", "DAILY", "iemop_data_DAPHS", "DAPHS"),
    "HAPHS" : ("HAPHS", "HVDCSchedule", "HAP", "DAILY", "iemop_data_HAPHS", "HAPHS"),
    "RTDHS" : ("RTDHS", "HVDCSchedule", "RTD", "DAILY", "iemop_data_RTDHS", "RTDHS"),
    "WAPHS" : ("WAPHS", "HVDCSchedule", "WAP", "DAILY", "iemop_data_DAPHS", "DAPHS"),
    # Market Bids and Offers Reserve - RTDOR: http://www.iemop.ph/csv/iemop_data_RTDOR/RTDOR_202005260000.zip
    "RTDOR" : ("RTDOR", "MarketBids_OffersReserve", "RTDOR", "HOURLY", "iemop_data_RTDOR", "RTDOR" ),
    # Market Bids and Offers Nomination - RTDNE: http://www.iemop.ph/csv/iemop_data_RTDNE/RTDNE_202005260000.zip
    "RTDNE" : ("RTDNE", "MarketBids_OffersReserve", "RTDNE", "HOURLY", "iemop_data_RTDNE", "RTDNE" ),
    # Market Bids and Offers Energy - RTDOE: http://www.iemop.ph/csv/iemop_data_RTDOE/RTDOE_202005260000.zip
    "RTDOE" : ("RTDOE", "MarketBids_OffersReserve", "RTDOE", "HOURLY", "iemop_data_RTDOR", "RTDOE" ),
    # Marginal Plant
    "MP" : ("MP", "MarginalPlant", "MP", "HOURLY", "iemop_data_MP", "MP"),
    # MPI Advisories: http://www.iemop.ph/csv/iemop_data_MPI_ADVISORIES/MPI_ADVISORIES_202007170000.zip
    "MPI_ADVISORIES" : ("MPIA", "MPI_ADVISORIES", "MPIA", "HOURLY", "iemop_data_MPI_ADVISORIES", "MPI_ADVISORIES"),
    # Outage Schedule
    "DAPOS" : ("DAPOS", "OutageSchedule", "DAP", "HOURLY", "iemop_data_DAPOS", "DAPOS"),
    "HAPOS" : ("HAPOS", "OutageSchedule", "HAP", "HOURLY", "iemop_data_HAPOS", "HAPOS"),
    "RTDOS" : ("RTDOS", "OutageSchedule", "RTD", "HOURLY", "iemop_data_RTDOS", "RTDOS"),
    "WAPOS" : ("WAPOS", "OutageSchedule", "WAP", "HOURLY", "iemop_data_WAPOS", "WAPOS"),
    # Post-Market Run Calculations: "http://www.iemop.ph/csv/iemop_data_DIPCER/DIPCER_202007170000.zip"
    "PMRC" : ("PMRC", "PostMarketRunCalculations", "PMRC", "HOURLY", "iemop_data_DIPCER", "DIPCER"),
    # Regional Summary
    "DAPREG" : ("DAPREG", "RegionalSummary", "DAP", "DAILY", "iemop_data_DAPREG", "DAPREG"),
    "HAPREG" : ("HAPREG", "RegionalSummary", "HAP", "DAILY", "iemop_data_HAPREG", "HAPREG"),
    "RTDREG" : ("RTDREG", "RegionalSummary", "RTD", "DAILY", "iemop_data_RTDREG", "RTDREG"),
    "WAPREG" : ("WAPREG", "RegionalSummary", "WAP", "DAILY", "iemop_data_WAPREG", "WAPREG"),
    # Security Limit
    "DAPSL" : ("DAPSL", "SecurityLimit", "DAP", "DAILY", "iemop_data_DAPSL", "DAPSL"),
    "HAPSL" : ("HAPSL", "SecurityLimit", "HAP", "DAILY", "iemop_data_HAPSL", "HAPSL"),
    "RTDSL" : ("RTDSL", "SecurityLimit", "RTD", "DAILY", "iemop_data_RTDSL", "RTDSL"),
    "WAPSL" : ("WAPSL", "SecurityLimit", "WAP", "DAILY", "iemop_data_WAPSL", "WAPSL")
}
VALID_SHORTNAMES = MARKET_DATA.keys()

DT_FORMAT = {
    1 : "%Y%m%d%H%M",
    2 : "%Y%m%d%H",
    3 : "%Y%m%d",
    4 : "%Y%m",
}

class ReportFrequency():
    def __new__(self, report_frequency: str):
        if report_frequency.upper() == "HOURLY":
            return "H"
        elif report_frequency.upper() == "DAILY":
            return "D"
        else:
            raise Exception("Invalid input.")

class MarketData():
    BASE_URL = "http://www.iemop.ph/csv/"
    FILE_FORMAT = ".zip"
    PRECISION = 5 #minutes

    def __init__(self, shortname: str, cat: str, subcat: str, frequency: str, subdir: str, prefix: str):
        self.NAME = shortname
        self.SHORTNAME = shortname
        self.CATEGORY = cat
        self.SUBCATEGORY = subcat
        self.FREQUENCYLONG = frequency
        self.FREQUENCY = ReportFrequency(frequency)
        self.SUBDIR = subdir
        self.PREFIX = prefix

    def generate_url(self, dt):
        endpoint = f"{self.BASE_URL}{self.SUBDIR}"
        filename = f"{self.PREFIX}_{dt}{self.FILE_FORMAT}"
        return f"{endpoint}/{filename}"

def constructor(name: str):
    if name in VALID_SHORTNAMES:
        return MarketData(*MARKET_DATA.get(name))