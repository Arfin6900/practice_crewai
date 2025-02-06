from crewai import BaseTool

class CustomTool(BaseTool):
    def use(self, input_data):
        # Implement your custom functionality here.
        return f"Processed data: {input_data}"
