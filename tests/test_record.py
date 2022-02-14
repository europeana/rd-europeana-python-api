from pyeuropeana.apis.record import Record
from pyeuropeana.utils.edm_utils import process_CHO_record

if __name__ == "__main__":

    record_api = Record('api2demo')

    resp = record_api('/9200579/tw7v83p4')
    simple_resp = process_CHO_record(resp)
    image_url = simple_resp['image_url']
    print(image_url)

