

## 📌 Version 1 — Event-Driven Architecture using Redis Pub/Sub

### 🎯 Objective

This version demonstrates the **fundamental concept of Event-Driven Architecture (EDA)** using a very simple producer → broker → consumer pipeline.
The main goal was to understand **asynchronous communication** and **decoupling** between components.

---

### 🏗️ Architecture Overview

| Component                  | Responsibility                                 |
| -------------------------- | ---------------------------------------------- |
| **Producer**               | Generates events and publishes them            |
| **Broker (Redis Pub/Sub)** | Transmits events asynchronously to subscribers |
| **Consumer**               | Listens and reacts to incoming events          |

The producer and consumer run as **independent processes**, removing any direct dependency between them.
Even if the consumer goes down, **the producer can continue working**.

---

### 🔄 Message Flow (Pub/Sub Model)

```
 Producer → Publishes event → Redis Channel → Consumer receives event in real time
```

Redis here acts as a **lightweight message broker**, enabling loose coupling following the Pub/Sub messaging pattern.

This architecture successfully demonstrates:

✔ Asynchronous communication
✔ Real-time event delivery
✔ Service decoupling (Producer doesn’t care about consumer availability)
✔ A minimal version of EDA

---

### ⚠️ Limitations in Version-1 (Why Move Forward?)

Although Redis Pub/Sub works well for learning, it has **major limitations** for production-level Event-Driven Architecture:

| Limitation                      | What Happens                               |
| ------------------------------- | ------------------------------------------ |
| ❌ No message persistence        | If consumer is offline → messages are lost |
| ❌ No event replay               | Consumers can’t reprocess older events     |
| ❌ No consumer groups            | Harder to scale horizontally               |
| ❌ No tracking of delivery state | No ACK/retry handling                      |

So, it works like a **“fire and forget”** pipeline — good for demos, not for reliable systems.

---

### 🚀 Why Redis Streams Next?

To move closer toward **real-world distributed event streaming**, next version will upgrade to **Redis Streams** — which provides:

| Feature                       | Benefit                         |
| ----------------------------- | ------------------------------- |
| Durability                    | Consumers can read events later |
| Replayable message log        | Debugging, audits, retries      |
| Consumer groups               | Horizontal scalability          |
| Better reliability guarantees | No message loss during downtime |

This will allow the system to evolve into a more robust **Kafka-like** event streaming architecture while still using Redis.

---

### 📌 Summary

> Version-1 serves as a foundational step — demonstrating Pub/Sub-based EDA.
> Next evolution: **Redis Streams for durability, scalability & reliability**.

---
