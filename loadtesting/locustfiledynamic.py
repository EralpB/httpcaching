from locust import task
from locust.contrib.fasthttp import FastHttpUser


class HomepageUser(FastHttpUser):

    @task
    def homepage(self):
        self.client.get("/dynamic")
        self.client.post("/dynamic")
