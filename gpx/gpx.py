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

        self.__parse_to_dict(file_content)
        return

    @staticmethod
    def __slice_content(file_content: str, start: str, end: str) -> dict:
        start_index = file_content.find(start)
        end_index = file_content[start_index:].find(end) + start_index

        items = file_content[start_index + len(start): end_index]

        pattern = r'(\w+)="([^"]+)"'
        matches = re.findall(pattern, items)
        return dict(matches)

    def __parse_to_dict(self, file_content: str):
        self.__dict['file'] = self.__slice_content(file_content, "<?xml", "?>")
        if self.__dict['file'] == {}:
            raise InvalidFile
        self.__dict['gpx'] = self.__slice_content(file_content, "<gpx", ">")

    def to_dict(self) -> dict:
        return self.__dict

