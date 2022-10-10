# Binghamton University: CS428 2022 Fall

## Project-1: Web Server

### SUMMARY

[Provide a short description of your program's functionality, no more than a couple sentences]: #
Server provides access to the html file and handles incorrect requests with a 404 response.
Webserver 1 handles one request at a time; Webserver 2 uses a multithreaded approach to handle multiple requests.
 
### NOTES, KNOWN BUGS, AND/OR INCOMPLETE PARTS

[Add any notes you have here and/or any parts of the project you were not able to complete]: #

### REFERENCES

[List any outside resources used]: #
https://ruslanspivak.com/lsbaws-part1/
https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#student,isbn=0136681557
https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

### INSTRUCTIONS

[Provide clear and complete step-by-step instructions on how to run and test your project]: #
1. Take note of the **ip** of your device by going to your machine's command line / terminal and typing `ipconfig`.
2. Take note of the **port** used for the running instance of the web server by checking the source code for the line `serverPort = x` where x is the port.
3. *cd* into the directory with the web server.
4. Ensure that the html file you'd like to appear on the web server is in the same directory as the web server source code which start the web server.
5. Start the web server with `py webserver1.py`.
    - Test the single-threaded web server by putting `ip:port/filename.html` into the URL of the client's web browser. The html contents should be displayed.
    - Test the returned 404 status code by misspelling the *filename.html* in the URL.
6. Place a large PDF file into the same directory as the web server.
7. Start the web server with `py webserver2.py`.
    - Test the multi-threaded web server by putting `ip:port/filename.pdf` into the URL of 2 or more of client's web browsers. The PDF contrents should be displayed. This tests the multi-threadedness of the web server and the contents should be loaded for the 2+ web browser windows quicker than in a single-threaded web server.
    - Test the returned 404 status code by misspelling the *filename.pdf* in the URL.

### SUBMISSION

I have done this assignment completely on my own. I have not copied it, nor have I given my solution to anyone else. I understand that if I am involved in plagiarism or cheating I will have to sign an official form that I have cheated and that this form will be stored in my official university record. I also understand that I will receive a grade of "0" for the involved assignment and my grade will be reduced by one level (e.g., from "A" to "A-" or from "B+" to "B") for my first offense, and that I will receive a grade of "F" for the course for any additional offense of any kind.

By signing my name below and submitting the project, I confirm the above statement is true and that I have followed the course guidelines and policies.

Submission date: 10/10/2022

Team member 1 name: Josh Gordon

Team member 2 name: Tim Marder
