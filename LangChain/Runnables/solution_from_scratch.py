import random
from abc import ABC, abstractmethod


class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass


class DummyLLM(Runnable):

    def __init__(self):
        print('LLM created')

    def predict(self, prompt):
        res_list = [
            'delhi is cap of india',
            'IPL is cricket league',
            'AI is Artificial Intelligence'
        ]

        return {'response': random.choice(res_list)}

    def invoke(self, prompt):
        res_list = [
            'delhi is cap of india',
            'IPL is cricket league',
            'AI is Artificial Intelligence'
        ]

        return {'response': random.choice(res_list)}


class DummyPromptTemplate(Runnable):

    def __init__(self, template, input_var):
        self.template = template
        self.input_var = input_var

    def format(self, input_dict):
        return self.template.format(**input_dict)

    def invoke(self, input_dict):
        return self.template.format(**input_dict)


class DummyStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']


class Connector(Runnable):

    def __init__(self, run_list):
        self.run_list = run_list

    def invoke(self, input_data):
        for run in self.run_list:
            input_data = run.invoke(input_data)

        return input_data


temp = DummyPromptTemplate(
    template='poem for {topic}',
    input_var=['topic']
)

llm = DummyLLM()

parser = DummyStrOutputParser()

# chain = Connector([temp, llm, parser])

# ans = chain.invoke({'topic': 'india'})

# print(ans)

temp1 = DummyPromptTemplate(
    template='joke about {topic}',
    input_var=['topic']
)

temp2 = DummyPromptTemplate(
    template='explanation for {response}',
    input_var=['response']
)

chain1 = Connector([temp1, llm])
chain2 = Connector([temp2, llm, parser])

chain = Connector([chain1, chain2])

ans = chain.invoke({'topic': 'india'})

print(ans)
