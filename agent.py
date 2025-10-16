"""
test_agent_1 - Custom Lambda Agent
Description: this is the testing of the agent 1 ...

IMPORTANT: Only edit the code in the main() function below.
The Lambda handler will be automatically appended during deployment.
DO NOT add lambda_handler code here - it will be added automatically.
"""

def main(event_body):
    """Main function for test_agent_1"""
    return {
        "success": True,
        "message": "Hello from test_agent_1!",
        "data": event_body
    }
