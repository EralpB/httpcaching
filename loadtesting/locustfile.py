from locust import HttpUser, task

class HomepageUser(HttpUser):

    @task
    def homepage(self):
        self.client.get("/")
