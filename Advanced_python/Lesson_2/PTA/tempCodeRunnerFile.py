import networkx as nx
import matplotlib.pyplot as plt

def example_function(x):
    if x > 0:
        y = x + 1
    else:
        y = x - 1
    return y

# Tạo đồ thị phụ thuộc chương trình (PDG)
pdg = nx.DiGraph()

# Thêm các nút và cạnh cho đồ thị
pdg.add_node("x > 0", type="control")
pdg.add_node("y = x + 1", type="data")
pdg.add_node("y = x - 1", type="data")
pdg.add_node("return y", type="data")

pdg.add_edge("x > 0", "y = x + 1", type="control")
pdg.add_edge("x > 0", "y = x - 1", type="control")
pdg.add_edge("y = x + 1", "return y", type="data")
pdg.add_edge("y = x - 1", "return y", type="data")

# Vẽ đồ thị PDG
pos = nx.spring_layout(pdg)  # Vị trí các nút trong đồ thị
edge_labels = nx.get_edge_attributes(pdg, 'type')

nx.draw(pdg, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold")
nx.draw_networkx_edge_labels(pdg, pos, edge_labels=edge_labels, font_color='red')

plt.title("Program Dependence Graph (PDG)")
plt.show()