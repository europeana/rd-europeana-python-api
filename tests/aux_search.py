import pyeuropeana.utils as utils
import pyeuropeana.apis as apis

if __name__ == "__main__":

    resp = apis.search(
        query = 'leonardo',
        rows = 150
    )

    df = utils.edm_utils.resp2df(resp)

    print(df)