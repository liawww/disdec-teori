import time
from raft import RaftNode

node_ids = [1, 2, 3]
nodes = [RaftNode(nid, node_ids) for nid in node_ids]

print("Simulasi Raft Consensus Dimulai...")

# Jalankan simulasi selama beberapa detik sampai ada yang jadi LEADER
start_time = time.time()
while time.time() - start_time < 3.0:
    for node in nodes:
        node.tick()
    time.sleep(0.1)

print("\n--- Status Akhir Node ---")
for node in nodes:
    print(f"Node {node.id}: State = {node.state.name}, Term = {node.current_term}")
