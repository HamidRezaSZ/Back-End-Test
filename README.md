# Your Task
Your task is to implement a RESTful API Server with Django. The server must be able to receieve an image, and classify it using a pretrained TensorFlow model. The choice of the model and the serving technique is up to you. You'll be evaluated on:

- How well the system can utilize the available resources at its disposal. E.g. GPUs, RAM, etc.
- How well the system can handle high load, e.g., dozens of requests at a time. The server is not expected to be able to answer such requests, but to queue them up and deliver the answer later. Note that the server doesn't have to (and shouldn't) block the request.

# Optional Features

- [ ] Authentication System: A simple token-based login/logout would do.
- [ ] Dashboard Panel for Authenticated Admin Users: Single-page simple stats report. 0 lines of CSS would do.
- [ ] Landing Page: Serving a static landing page.
- [ ] Dockerization.
