from collections import namedtuple
from datetime import datetime


# @dataclass
# class DataIngestionArrtifact:
#     feature_store_file_path : str
#     metadata_file_path : str
#     download_dir: str

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
                                   ["feature_store_file_path", "metadata_file_path", "download_dir"])