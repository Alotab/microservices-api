
# Restaurant Ordering App

This is a FastAPI microservices app for managing restaurant orders. The app is divided into several chapters, each focusing on a specific aspect of the whole resturant process.

## Chapter 1: Orders

This chapter provides endpoints for creating, retrieving, updating, and deleting orders. The following endpoints are available:

- `POST /orders`: Create a new order.
- `GET /order/{order_id}`: Retrieve an order by ID.
- `PUT /orders/{order_id}`: Update an existing order.
- `DELETE /orders/{order_id}`: Delete an order.

In addition to the endpoints, this chapter also defines the following schemas:

- `OrderItemSchema`: Represents an order in the system.
- `GetOrderSchema`: Used to list all available order.
- `OrderUpdate`: Used to update an existing order.

## Chapter 2: Kitchen API

This chapter provides endpoints for managing the production of orders in the kitchen. The following endpoints are available:

- `POST /kitchen/schedules`: Create a new production schedule.
- `GET /kitchen/schedules`: List all production schedules.
- `GET /kitchen/schedules/{schedule_id}`: Retrieve a production schedule by ID.
- `DELETE /kitchen/schedules/{schedule_id}`: Cancel a production schedule.

In addition to the endpoints, this chapter also defines the following schemas:

- `Schedule`: Represents a production schedule in the system.
- `OrderItemSchema`: Used to select the size of the food item - `small`,`midium`,`big`.
- `ScheduleCreate`: Used to create a new production schedule.
- `ScheduleStatusSchema`: Used to track the status of the order - `pending`,`progress`,`cancelled`, `finished`.

## Future Chapters

This is an ongoing project, and future chapters will be added as needed. Stay tuned for more updates!

I hope this helps! Let me know if you have any other questions.

