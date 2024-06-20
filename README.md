## Simple Application Based on Microservices

the following application adopts the **microservices architecture**, it was developed to learn how the latter works practically.

The idea here is to have two entities: **sender** and **receiver**. The receiver service initiates the connection to the sender either by asking him some limited set of questions:
- What time is it?
- Where am I?
  
and the sender would reply by providing the answer. Or by testing whether the sender service is up or not (a simple ping would do the job).

The project can be considered a good starter for those who want to learn more about microservices in practice, you might want to check this [article](https://medium.com/swlh/building-your-first-microservice-80c90af74d9b) too for further information.

