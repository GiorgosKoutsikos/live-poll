# 📊 Live Audience Polling App

A real-time, interactive voting system built with **FastAPI**, native **WebSockets**, and **Vanilla JavaScript**.

---

## 📖 About This Project

This project was developed for **educational and learning purposes** to implement bi-directional client-server communication using WebSockets without third-party frontend frameworks, featuring real-time data aggregation and dynamic UI state synchronization.

---

## ✨ Features

- **Instant Bi-Directional Communication:** Full-duplex WebSocket connection (`/ws`) between client and server.
- **Real-Time Result Broadcasting:** When a vote is cast, updated aggregated results are pushed instantly to all connected clients.
- **Initial State Synchronization:** Clients immediately receive the current poll status upon establishing a connection.
- **Dynamic DOM Updates:** Poll results and progress bars automatically animate and calculate percentage shares in real time.
- **Graceful Lifecycle Management:** Tracks active connections and removes disconnected clients safely using `WebSocketDisconnect`.

---

## 🧠 What I Learned

- Establishing WebSocket endpoints and managing connection pools in FastAPI.
- Using `send_json()` and `receive_text()` for structured real-time network payloads.
- Native JavaScript WebSocket event handling (`onmessage`, `send`, payload parsing via `JSON.parse`).

---
