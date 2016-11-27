import warc

# path_dis="/user/bbkruit/CC-MAIN-20160924173739-00000-ip-10-143-35-109.ec2.internal.warc.gz"
#
# f=warc.open("/Users/xyang/Downloads/CommonCrawl-sample.warc","rb")

# record = f.read_record()
# while record is not None:
#   record = f.read_record()
#   pass

# print record
# print record.header
# print record.payload
import warc
from itertools import islice

N = 10
warc_file = warc.open('/Users/xyang/Downloads/CommonCrawl-sample.warc')
for record in islice(warc_file, N):
    print record
# for record in f:
#     print record['WARC-Target-URI'], record['Content-Length']