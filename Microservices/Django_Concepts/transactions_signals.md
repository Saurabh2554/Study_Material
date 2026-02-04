# What is Transactions ?
 ANS: Any Database operations such as Select, Update will be termed as a database Transaction. In DBMS term we try to implement that any database operation should follow ACID Property. 

# What is ACID Property ?
 ANS: ACID stands for Atomicity, Consistency, Isolation, Durability. It helps operations to happen in a proper and discrepency free manner.
    #Atomicity: It states that each database operation be it single or collection of one or more should be considered as a single unit. Either all database operation will be executed or none. 
    For ex: on order creation, we generally have to perform three operations, 1. Decrease pdt qty, 2. Create_order, 3.Process_payment. So Atomicity states that either all will happen or none.

    #Consistency: It states that state of the database must remain in a valid state before and after a transaction. If a transaction deducts money from one account but doesn't add it to another (in a transfer), it violates consistency.

    For ex: If there is a money transfer operation from person A to person B, then consistency means total balance before and after transaction should remain same, which means if money is deducted from A's account then it must be added to B's account, in this way if total money(combined account) before transaction is 700 then after that it will be 700 too.

    #Isolation: Isolation ensures that transactions run independently without affecting each other. Changes made by one transaction are not visible to others until they are committed. It prevents issues like reading uncommitted data which can be rolled back later.

    #Durability: Durability ensures that once a transaction is committed, its changes are permanently saved, even if the system fails. The data is stored in non-volatile memory, so the database can recover to its last committed state without losing data.

    Example: After successfully transferring money from Account A to Account B, the changes are stored on disk. Even if there is a crash immediately after the commit, the transfer details will still be intact when the system recovers, ensuring durability.

# How can we implement transaction behaviour in Django ?
 ANS: There are two ways in which we can implement the same, by using @transaction.atomic decorator at the view level or by using transaction.atomic() context manager.
      decorator pattern is generally used for entire view and context manager is generally used to make a particular code block to be handled as transaction.
      By default django considers each db operation to be a transaction, because of the default configuration AUTOCOMMIT: True while configuring DB in settings.py .
      Reverting it will require you to explicitely define transaction in case if you want any particular DB operation to be atomic.

# How will you handle the case when you have multiple co-related DB operation and you want either all should happen or none ?
 ANS: In order to implement this scenario we have two options: 
      1. Either make entire method handling this operation to behave as transaction.
      2. We can use the concept of nested transaction block.

      Consider a situation when you do not want failure occurred by any inner transaction block, also reverse the db changes made by other outer operations neither it should stop the execution. In that case we can use transaction.atomic() making a nested transaction wrapped in try-Except block. if we do not use try-except the error caused by inner db-operation will lead to rollback for the oter db ops too.
      When we use nested transaction, db creates a savepoint at that block to revert or to step back at that step if needed.


      consider a situation when you have multiple db-operations to handle and each one must either be committed or no one should be, So in that case we can use Durable=True when declaring an outer transaction block.

# What are Data Errors and Integrity Errors in Django Transactions?
 ANS: Data errors and integrity errors are common issues that can occur during transactions. Data errors include situations where incorrect or unexpected data is encountered, while integrity errors involve violations of database constraints. Handling these errors is essential for maintaining a reliable database system.

# When would you use transaction.on_commit()?
 ANS: transaction.on_commit(func) is used to register a callback function that will be executed only after the current transaction successfully commits to the database.  This is useful for actions that depend on the transaction's success but are not part of the core database logic, such as: 
    1. Sending email notifications.
    2. Invalidating a cache.
    3. Enqueuing background tasks (e.g., using Celery).     

# What is the ATOMIC_REQUESTS setting in Django?
 ANS: Setting ATOMIC_REQUESTS = True in your database configuration in settings.py enables a mode where Django automatically wraps every view function in an atomic() block. This simplifies transaction management for simple CRUD views but requires careful handling for more complex scenarios or streaming responses. 


# What are signals in Django ?
 ANS: Signals are a way for different parts of application to communicate with each other in a loosly coupled manner. A signal is essentially a message sent by one part of the application (the sender) to another part (the receiver) to notify it of some event that has occurred. Signals in django follow publisher-subscriber pattern for communication. The publisher (sender) sends out a signal, and one or more subscribers (receivers) listen for that signal and respond accordingly.

# What does it mean by "Django signals are synchronous in nature" ?
 ANS: In django , saying Signals are synchronous, simply means that when a signal is sent, all it's connected receiver are executed immediately one after the another, the order in which they are registered, in the same thread, before the original operation continues.

# How can we make signals behave non-blocking ?
 Ans: Conceptually we can make signals non-blocking by using celery to perform the task which we will be performing inside he receiver, but even in this case signals are sync, only the job it was doing will behave in async manner.when a receiver enqueues a Celery task using .delay(), it does not wait for task execution; only the task dispatch is synchronous. 
For-ex:  @receiver(post_save, sender=User)
        def send_email(sender, instance, **kwargs):
            send_email_task.delay(instance.id)

here the receiver will not wait for celery task to be finished, it returns immediatly, email will be sent in non-blocking manner.

# When and when not to go for signals ?
 ANS: Use signal when the action you want to perform is a side effect, it is not the core business logic, or even if it fails it wont break the main flow. for ex: sending mail, update caching, audit logs, metrics/monitoring stuffs. 
 Do not use signals when you are performing operation which is a code business logic, suppose after order save you want to call process_payment or update the inventory etc.



