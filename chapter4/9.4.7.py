import igraph
import numpy as np


def find_max_dependency(projects):
    start_project = projects[0]
    max_dependents = len(projects[0].blocking_projects)
    for project in projects[1:]:
        if len(project.blocking_projects) > max_dependents:
            start_project = project
            max_dependents = len(project.blocking_projects)
    return start_project


class Project:
    def __init__(self, value):
        self.value = value
        self.blocking_projects = []
        self.visited = False
        self.done = False

    def add_project(self, vertex):
        self.blocking_projects.append(vertex)


def create_graph(adj_matrix, num_vertices):
    projects = []
    for vertex in range(num_vertices):
        projects.append(Project(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adj_matrix[row][column] == 1:
                projects[row].add_project(projects[column])
    return projects


def do_project(project):
    if project.visited:
        print(f"Project {project.value} has unresolvable dependencies")
        exit()
    project.visited = True
    for blocking_project in project.blocking_projects:
        if not blocking_project.done:
            do_project(blocking_project )
    project.done = True
    print(f"Done project {project.value}")    

    


num_projects = 3
labels = list(map(str, range(num_projects)))

# Create dependency pairs
adj_matrix = np.random.randint(0, 2, (num_projects, num_projects))
# Make sure project is not dependent on itself
np.fill_diagonal(adj_matrix, 0)

print(adj_matrix)

# Create graph of connected projects, where the fanout of a particular project is
# the number of projects it depends on.
projects = create_graph(adj_matrix, num_projects)


start_project = find_max_dependency(projects)
do_project(start_project)

# Do projects which do not block other projects
for project in projects:
    if not project.done:
        print(f"Done project {project.value}")    

# g = igraph.Graph.Adjacency((adj_matrix > 0).tolist())
# g.vs["label"] = labels
# igraph.plot(g, labels=True)
