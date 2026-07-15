class CampusCollaborativeWorkspaceClient:
    def dispatch_feedback(self, human_feedback: str, active_agents: list[str]) -> dict:
        queue = [{"agent": agent, "task": f"Process feedback: {human_feedback}"} for agent in active_agents]
        return {"message_queue": queue}