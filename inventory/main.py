from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

app = FastAPI()

redis = get_redis_connection(
    host="redis-19611.c300.eu-central-1-1.ec2.cloud.redislabs.com",
    port=19611,
    password="szpPPPJNLLyTEvVDHXtPYs48L9d2prhV",
    decode_responses=True,
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


@app.get("/products")
def all():

    return Product.all_pks()
