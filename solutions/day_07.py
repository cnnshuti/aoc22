from aoclib import input_parsers
from typing import List
from collections import defaultdict
class Node():
    def __init__(self, parent, children, name, depth, size):
        self.parent = parent
        self.children = children
        self.name = name
        self.depth = depth
        self.size = size
    def __str__(self):
        return f'{self.parent.name if self.parent else None}, {len(self.children)}, {self.name}, {self.depth}, {self.size}'

def commands_to_fstree(input_lines):
    nodes_list = []
    seen_node_names = set()
    nodes_by_depth = defaultdict(list)
    current_node = None
    current_depth = 0
    for line in input_lines:
        elements = line.split(' ')
        if elements[0] == '$':
            if elements[1] == 'cd':
                node_name = elements[2]
                if node_name == '..':
                    current_depth -= 1
                    current_node = current_node.parent
                else:
                    new_node = Node(current_node, [], node_name, current_depth, 0)
                    nodes_by_depth[current_depth].append(new_node)
                    current_depth += 1
                    nodes_list.append(new_node)
                    seen_node_names.add(new_node.name)
                    if current_node is not None:
                        current_node.children.append(new_node)
                    current_node = new_node
            elif elements[1] == 'ls':
                # Do nothing, we'll add children to
                pass
            else:
                raise ValueError(f'Unknown command {elements}')
        else:
            if elements[0] != 'dir':
                new_node = Node(current_node, [], elements[1], current_depth, int(elements[0]))
                current_node.children.append(new_node)
                nodes_by_depth[current_depth].append(new_node)
                nodes_list.append(new_node)
                seen_node_names.add(new_node.name)
    return nodes_list, nodes_by_depth

def compute_directory_sizes(nodes_list, nodes_by_depth):
    if nodes_by_depth[0][0].size > 0:
        return
    for depth in range(max(nodes_by_depth), -1, -1):
        for node in nodes_by_depth[depth]:
            if node.parent is not None:
                node.parent.size += node.size

def solve_part_one(input_file):
    nodes_list, nodes_by_depth = commands_to_fstree(input_parsers.get_input_lines(input_file))
    compute_directory_sizes(nodes_list, nodes_by_depth)
    sum_sizes = 0
    for node in nodes_list:
        if (len(node.children) > 0) & (node.size <= 100_000): # the node is a directory
            # print(node)
            sum_sizes += node.size
    return sum_sizes


def solve_part_two(input_file):
    total_disc_space = 70000000
    min_unused = 30000000
    nodes_list, nodes_by_depth = commands_to_fstree(input_parsers.get_input_lines(input_file))
    compute_directory_sizes(nodes_list, nodes_by_depth)
    curr_unused_space = total_disc_space - nodes_by_depth[0][0].size
    candidate_for_deletion = nodes_by_depth[0][0]
    for node in nodes_list:
        if ((node.size < (min_unused - curr_unused_space))  # directory is too small
            or (len(node.children) == 0)): # it's not a directory
            continue
        if node.size < candidate_for_deletion.size:
            candidate_for_deletion = node
    return candidate_for_deletion


if __name__ == "__main__":
    input_files = [
        input_parsers.INPUTS_DIR / file for file in ["07_test_input", "07_input"]
    ]
    for file in input_files:
        print(f"\t{file.name:=^20}")
        print(f"\t{solve_part_one(file)}")
        print(f"\t{solve_part_two(file)}")
