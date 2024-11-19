#!/usr/bin/env python
import sys
import warnings

from criadordeartigos.crew import Criadordeartigos

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    inputs = {
        'topic': 'Criar soluções tecnologicas inovadoras para reduzir o impacto ambiental no setor logístico, com ênfase em redução de emissões de CO2 e energias renováveis.'
    }
    Criadordeartigos().crew().kickoff(inputs=inputs)


def train():
    inputs = {
        "topic": "Criar soluções tecnologicas inovadoras para reduzir o impacto ambiental no setor logístico, com ênfase em redução de emissões de CO2 e energias renováveis."
    }
    try:
        Criadordeartigos().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    try:
        Criadordeartigos().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    inputs = {
        "topic": "Criar soluções tecnologicas inovadoras para reduzir o impacto ambiental no setor logístico, com ênfase em redução de emissões de CO2 e energias renováveis."
    }
    try:
        Criadordeartigos().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
