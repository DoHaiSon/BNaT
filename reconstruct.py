import pandas as pd 
import numpy as np

col_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
                "land", "wrong_fragment", "urgent", "count", "srv_count", "serror_rate",
                "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate", 
                "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
                "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
                "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate", 
                "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]

file_name = r'C:\Users\SON\Desktop\BNaT\Merged_dataset\w3.csv'

raw = pd.read_csv(file_name, header=None, names = col_names) 
raw = raw.drop(columns=["land", "wrong_fragment",  "urgent", "rerror_rate",  "srv_rerror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate"])

reorder = raw[["duration", "protocol_type", "service",	"src_bytes", "dst_bytes", "flag", "count", "srv_count", "serror_rate", "same_srv_rate", "diff_srv_rate", "srv_serror_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", "dst_host_serror_rate", "dst_host_srv_diff_host_rate", "dst_host_srv_serror_rate", "label"]]

print(reorder)

reorder.to_csv(file_name, index = False, header=None)    