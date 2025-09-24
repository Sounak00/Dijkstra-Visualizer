from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import heapq

app = Flask(__name__)
CORS(app)

# Parse input like: A,B,2\nA,D,7\n...
def parse_graph(text):
    nodes = set()
    adj = {}
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        # accept commas and optional spaces
        parts = [p.strip() for p in line.split(',')]
        if len(parts) != 3:
            continue
        a, b, w = parts
        try:
            w = int(w)
        except ValueError:
            continue
        nodes.add(a)
        nodes.add(b)
        adj.setdefault(a, {})[b] = w
        adj.setdefault(b, {})[a] = w
    # Create sorted node list for matrix ordering
    node_list = sorted(nodes)
    return node_list, adj

# Dijkstra
def dijkstra(adj, source):
    dist = {n: float('inf') for n in adj}
    parent = {n: None for n in adj}
    dist[source] = 0
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/parse', methods=['POST'])
def api_parse():
    data = request.get_json() or {}
    text = data.get('text', '')
    node_list, adj = parse_graph(text)
    # build adjacency matrix with -1 as no edge
    matrix = []
    for i in node_list:
        row = []
        for j in node_list:
            if j in adj.get(i, {}):
                row.append(adj[i][j])
            else:
                row.append(-1)
        matrix.append(row)
    return jsonify({
        'nodes': node_list,
        'matrix': matrix
    })

@app.route('/api/shortest', methods=['POST'])
def api_shortest():
    data = request.get_json() or {}
    text = data.get('text', '')
    source = data.get('source')
    destination = data.get('destination')
    node_list, adj = parse_graph(text)
    if not node_list:
        return jsonify({'error': 'No graph data parsed'}), 400
    if source not in adj or destination not in adj:
        return jsonify({'error': 'Source or destination node not found'}), 400
    dist, parent = dijkstra(adj, source)
    if dist[destination] == float('inf'):
        return jsonify({'path': None, 'distance': None})
    # reconstruct path
    path = []
    cur = destination
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return jsonify({'path': path, 'distance': dist[destination]})

if __name__ == '__main__':
    app.run(debug=True)