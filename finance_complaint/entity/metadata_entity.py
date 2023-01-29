
from finance_complaint.exception import FinanceException
import os, sys

from finance_complaint.utils import read_yaml_file, write_yaml_file
from collections import namedtuple
from finance_complaint.logger import logger
from finance_complaint.cloud_storage import SimpleStorageService
DataIngestionMetadataInfo = namedtuple("DataIngestionMetadataInfo", ["from_date", "to_date", "data_file_path"])


class DataIngestionMetadata:

    def __init__(self, metadata_file_path,):
        self.metadata_file_path = metadata_file_path
    
    '''checking if meta_data file is present then we are calling get_metadata() to check the information if not present 
        we will not call we start any start_date and end _date, if present based on that the from date is selected'''
    @property
    def is_metadata_file_present(self):
        return os.path.exists(self.metadata_file_path)

    def write_metadata_info(self, from_date: str, to_date: str, data_file_path: str):
        try:
            '''writing the information to meta_info.yaml file'''
            metadata_info = DataIngestionMetadataInfo(
                from_date=from_date,
                to_date=to_date,
                data_file_path=data_file_path
            )
            write_yaml_file(file_path=self.metadata_file_path, data=metadata_info._asdict())

        except Exception as e:
            raise FinanceException(e, sys)

    def get_metadata_info(self) -> DataIngestionMetadataInfo:
        try:
            '''reading the metadata information from the yaml file'''
            if not self.is_metadata_file_present:
                raise Exception("No metadata file available")
            metadata = read_yaml_file(self.metadata_file_path)
            metadata_info = DataIngestionMetadataInfo(**(metadata))
            logger.info(metadata)
            return metadata_info
        except Exception as e:
            raise FinanceException(e, sys)