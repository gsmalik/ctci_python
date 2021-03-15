import igraph
import numpy as np


def find_max_dependency(projects):
    """
    Determines project with maximum number of blocking projects.

    Parameters
    ----------
    projects: ``list``
        A list of ``Project`` objects.

    Returns
    -------
    Project that is most blocked.

    Time Complexity
    ---------------
    O(N), where N is the number of projects.

    Space Complexity
    ----------------
    O(1).
    """
    # Iterate through list of projects to determine one that has most number of
    # blocking projects.
    start_project = projects[0]
    max_dependents = len(projects[0].blocking_projects)
    for project in projects[1:]:
        if len(project.blocking_projects) > max_dependents:
            start_project = project
            max_dependents = len(project.blocking_projects)
    return start_project


class Project:
    """
    Class to implement project.

    Parameters
    ----------
    value: ``int/str``
        The identifying value of the project.
    """

    def __init__(self, value):
        self.value = value
        self.blocking_projects = []
        self.visited = False
        self.done = False

    def add_project(self, vertex):
        """Adds blocking project"""
        self.blocking_projects.append(vertex)


def create_graph(adj_matrix, num_vertices):
    """Creates graph of dependent projects. Not part of asymptotic analysis"""
    projects = []
    for vertex in range(num_vertices):
        projects.append(Project(vertex))

    for row in range(num_vertices):
        for column in range(num_vertices):
            if adj_matrix[row][column] == 1:
                projects[row].add_project(projects[column])
    return projects


def do_project(project):
    """
    Function to do a project.

    Parameters
    ----------
    project: ``Project``
        The project object we want to do.

    Time Complexity
    ---------------
    O(F), where F is the total fanout cone of blocking projects.

    Space Complexity
    ----------------
    O(D), where D is the depth of the fanout cone of blocking projects.
    """
    # This means we tried doing this project in the stack before and it
    # recursively led us to this, implying an unresolvable dependency.
    if project.visited:
        print(f"Project {project.value} has unresolvable dependencies")
        exit()

    # Set project as visited and try doing the projects that block this project.
    project.visited = True
    for blocking_project in project.blocking_projects:
        if not blocking_project.done:
            do_project(blocking_project)

    # This project can be done since we did all other projects that were blocking
    # this project. Mark it so.
    project.done = True
    print(f"Done project {project.value}")


# Create project labels
num_projects = 3
labels = list(map(str, range(num_projects)))

# Create dependency pairs
adj_matrix = np.random.randint(0, 2, (num_projects, num_projects))
# Make sure project is not dependent on itself
np.fill_diagonal(adj_matrix, 0)

print(f"Project dependency:\n {adj_matrix}")

# Create graph of connected projects, where the fanout of a particular project is
# the number of projects it depends on.
projects = create_graph(adj_matrix, num_projects)

# Find your most constrained project
most_constrained_project = find_max_dependency(projects)

# Do projects, starting with most constrained. This does not mean that the most
# constrained project will be done first. We perform a DFS on this. So, that
# means we will start doing it in like "`A` depends on `B` which depends on `C`
# which depends on `D` which is not dependent on anything so lets do `D` and
# backtrack to `C`, `B` and finally most constrained `A`.
do_project(most_constrained_project)

# Do projects which do not block other projects and were not explored in the DFS
# above
for project in projects:
    if not project.done:
        print(f"Done project {project.value}")

g = igraph.Graph.Adjacency((adj_matrix > 0).tolist())
g.vs["label"] = labels
igraph.plot(g, labels=True)
