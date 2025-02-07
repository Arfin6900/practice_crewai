from ..services.crew_service import CrewService

class CrewController:
    def __init__(self):
        self.crew_service = CrewService()
    
    def run_task(self):
        return self.crew_service.execute_task()
