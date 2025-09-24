# Dijkstra Web Project

A small web app to **visualize graphs and compute shortest paths** using **Dijkstra's algorithm**.  
Users can input a graph, see its adjacency matrix, and find the shortest path between nodes.

---

## Demo

> A live demo can be deployed on [Render.com](https://sounakmondal-dijkstra-visualizer.onrender.com/)

## Features

- Parse CSV graph input (`A,B,2`) and display adjacency matrix.  
- Compute shortest path between two nodes using Dijkstra’s algorithm.  
- Interactive frontend with HTML, CSS, and JavaScript.  
- Flask backend with simple REST API endpoints.  

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **Deployment Ready:** Compatible with Render, Railway, or Heroku  

---

## Usage

1. Enter graph edges in the textarea (`A,B,2` per line).  
2. Click **Parse & Show Matrix** to view the adjacency matrix.  
3. Enter **Source** and **Destination** nodes, click **Find Shortest Path**.  
4. Path and distance appear below.

---

## Installation (Local)

```bash
git clone https://github.com/Sounak00/Dijkstra-Visualizer.git
cd Dijkstra-Web-Project
pip install -r requirements.txt
python app.py
