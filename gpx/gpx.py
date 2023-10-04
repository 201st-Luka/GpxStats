import re

from .collections import InvalidFile


__all__ = (
    'GpxFile',
)


class GpxFile:
    def __init__(self, gpx_file_name: str):
        self.file_name: str = gpx_file_name
        self.__dict = {}
        with open(self.file_name, 'r') as gpx_file:
            file_content: str = gpx_file.read()

        self.__read_file_head(file_content)
        self.__read_trk_points(file_content)
        return

    @staticmethod
    def __find_in_str(file_content: str, start: str, end: str) -> str | None:
        start_index = file_content.find(start)
        end_index = file_content[start_index:].find(end) + start_index

        result = file_content[start_index + len(start): end_index]

        if result != file_content:
            return result
        return None

    def __gpx_part_to_dict(self, file_content: str, start: str, end: str) -> dict:
        pattern = r'(\w+)="([^"]+)"'
        matches = re.findall(pattern, self.__find_in_str(file_content, start, end))
        return dict(matches)

    @staticmethod
    def __get_point_list(file_content: str):
        pattern = r'lat="([-0-9.]+)" lon="([-0-9.]+)">\s+<ele>([-0-9.]+)</ele>\s+<time>([^<]+)</time>'
        pattern_hr = r'<ns3:TrackPointExtension>\s+<ns3:hr>([-0-9.]+)</ns3:hr>\s+</ns3:TrackPointExtension>'
        matches = re.findall(pattern, file_content)
        matches_hr = re.findall(pattern_hr, file_content)

        if len(matches_hr):
            return [
                {'lat': float(lat), 'lon': float(lon), 'ele': float(ele), 'time': time, 'hr': int(hr)}
                for (lat, lon, ele, time), hr in zip(matches, matches_hr)
        ]

        return [
            {'lat': float(lat), 'lon': float(lon), 'ele': float(ele), 'time': time}
            for lat, lon, ele, time in matches
        ]

    def __read_file_head(self, file_content: str):
        self.__dict['file'] = self.__gpx_part_to_dict(file_content, "<?xml", "?>")
        if self.__dict['file'] == {}:
            raise InvalidFile
        self.__dict['gpx'] = self.__gpx_part_to_dict(file_content, "<gpx", ">")
        self.__dict['metadata'] = self.__find_in_str(
            file_content, "<metadata>", "</metadata>"
        ). replace("\n", '').replace('  ', '')

    def __read_trk_points(self, file_content: str):
        self.__dict['trk'] = {}

        data = self.__find_in_str(file_content, "<trk>", "<trkseg>")

        if (name := self.__find_in_str(data, "<name>", "</name>")) is not None:
            self.__dict['trk']['name'] = name
        else:
            self.__dict['trk']['name'] = None
        if (type_ := self.__find_in_str(data, "<type>", "</type>")) is not None:
            self.__dict['trk']['name'] = type_
        else:
            self.__dict['trk']['name'] = None

        self.__dict['trk']['points'] = self.__get_point_list(file_content)

    def to_dict(self) -> dict:
        return self.__dict
