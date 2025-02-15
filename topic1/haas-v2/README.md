# HAAS v2

This challenge is not based on real world applications directly, but is instead intended to get you familiar with the idea that HTTP is a text based protocol. It involves two applications, one allowing you to send requests to the other. Instead of your web browser creating the text for the requests, you will instead be writing the HTTP requests yourself.

To run locally, use `docker compose up --build` to start the application. Use CTRL-C to stop the application.
When the application is running, access http://localhost:8000 in your web browser.
If you want to modify the source code, stop the app with CTRL-C, and start it again to rebuild (that's what the `--build` part of the command does).

Note: You may need to use `docker-compose` instead of `docker compose` depending on how you installed compose.