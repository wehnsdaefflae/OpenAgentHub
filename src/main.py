# Example usage
from src.business_logic.workflow import WorkflowEngine, WorkflowStep
from src.model_interface.provider import DummyCloudProvider
from src.runtime.local_runtime import LocalRuntime
from src.security.data_protection import DataProtector


def main():
    # Initialize components
    provider = DummyCloudProvider()
    workflow_engine = WorkflowEngine()
    data_protector = DataProtector()
    local_runtime = LocalRuntime()

    # Create a sample workflow
    workflow_steps = [
        WorkflowStep(
            name="process_data",
            action="analyze_text",
            parameters={"max_length": 1000}
        ),
        WorkflowStep(
            name="generate_response",
            action="generate",
            parameters={"temperature": 0.7}
        )
    ]

    workflow_name = workflow_engine.create_workflow("sample_workflow", workflow_steps)

    # Execute workflow with dummy data
    input_data = {"text": "Sample input for processing"}
    protected_data = data_protector.minimize_data(input_data)
    result = workflow_engine.execute_workflow(workflow_name, protected_data)

    print(f"Workflow execution result: {result}")


if __name__ == "__main__":
    main()