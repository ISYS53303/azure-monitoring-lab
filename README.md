# Azure Monitoring Lab

This repository contains code for an in-class lab that simulates monitoring an Azure Function under load. It demonstrates handling multiple incoming requests and performing background work.

`student-client`: This directory holds the code for a client application that sends requests to the Azure Function. You can use this client to simulate workload and test the function's scalability.

`server`: This directory contains the Azure Function code ("backend") responsible for processing requests. The function calculates a Fibonacci sequence to represent "work" being performed.

This repository provides a valuable learning tool for understanding Azure Function behavior under concurrent requests.
