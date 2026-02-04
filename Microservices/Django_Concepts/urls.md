# For idempotent APIs
 ANS: https://chatgpt.com/c/695c980b-1c84-8322-90d7-40e8e664a9e7

# Best Practices API Design
 ANS: https://medium.com/@techsuneel99/api-design-from-basics-to-best-practices-da47c63aaf70

  2. Implement asynchronous methods
    Sometimes a POST, PUT, PATCH, or DELETE method might require processing that takes time to complete. If you wait for completion before you send a response to the client, it might cause unacceptable latency. In this scenario, consider making the method asynchronous. An asynchronous method should return HTTP status code 202 (Accepted) to indicate that the request was accepted for processing but is incomplete.

    Expose an endpoint that returns the status of an asynchronous request so that the client can monitor the status by polling the status endpoint. Include the URI of the status endpoint in the Location header of the 202 response. For example:

    HTTP/1.1 202 Accepted
    Location: /api/status/12345

    If the client sends a GET request to this endpoint, the response should contain the current status of the request. Optionally, it can include an estimated time to completion or a link to cancel the operation.

    HTTP/1.1 200 OK
    Content-Type: application/json
    {
        "status":"In progress",
        "link": { "rel":"cancel", "method":"delete", "href":"/api/status/12345" }
    }