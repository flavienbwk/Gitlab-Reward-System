# API documentation

This API documentation relates to the API of the **Gitlab RS** system. This is **not** a Gitlab documentation.

## Authentication

Authentication is performed through the OAuth Gitlab API. The front-end nonetheless will perform user actions through the Gitlab RS back-end as the badges and statistics need to be registered in the Gitlab RS database.

Only the **OAuth token** is saved in the Gitlab RS back-end (`user.access_token`).
