from Station import Station
from Train import Train

trains = []
stations = []
tickits = []

stations.append(Station("New Jalpaiguri", "NJP", "Siliguri"))
stations.append(Station("Howrah", "HWR", "Kolkata"))
stations.append(Station("Delhi", "DLH", "Delhi"))
stations.append(Station("Mumbai", "MBY", "Mumbai"))
stations.append(Station("Tata Nagar", "TATA", "Jamshedpur"))
stations.append(Station("Guwahati", "GHW", "Assam"))
stations.append(Station("Kashmir", "KSM", "Kashmir"))
stations.append(Station("Manali", "MNL", "Himachal"))


def get_station_by_Shhort_name(short_name):
    return _gsbsn(short_name)


def _gsbsn(short_name) -> Station:
    for station in stations:
        if short_name == station.get_short_name():
            return station


trains.append(Train("12021", "Shatabdi Express", _gsbsn("HWR"), _gsbsn("NJP"), [], 100))
trains.append(Train("19001", "Rajdhani Express", _gsbsn("NJP"), _gsbsn("DLH"), ["NJP", "GHW", "MBY", "DLH"], 120))
trains.append(Train("13490", "Darjeeling mail", _gsbsn("MNL"), _gsbsn("HWR"), ["KSM", "GHW", "TATA", "HWR"], 80))
trains.append(Train("12345", "tista torsha", _gsbsn(""), _gsbsn(""), [], 80))


def search_trains_by_route(source, destination) -> [Train]:
    available_trains = []

    for train in trains:
        if source in train.get_route() and destination in train.get_route():
            available_trains.append(train)

    return available_trains
