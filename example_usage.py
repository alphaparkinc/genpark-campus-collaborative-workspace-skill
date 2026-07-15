from client import CampusCollaborativeWorkspaceClient
client = CampusCollaborativeWorkspaceClient()
print(client.dispatch_feedback("fix design layout", ["design_agent", "qa_agent"]))