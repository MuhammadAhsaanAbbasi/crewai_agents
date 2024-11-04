#!/usr/bin/env python
import sys
from crewai_agents.crew import CrewaiAgentsCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    result = CrewaiAgentsCrew().crew().kickoff(inputs=inputs)
    return result


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        result = CrewaiAgentsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)
        return result

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        results = CrewaiAgentsCrew().crew().replay(task_id=sys.argv[1])
        return results

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

if __name__ == "__main__":
            if len(sys.argv) > 1 and sys.argv[1] == "train":
                response = train()
                print(response)
            elif len(sys.argv) > 1 and sys.argv[1] == "replay":
                response = replay()
                print(response)
            else:
                response = run()
                print(response)
