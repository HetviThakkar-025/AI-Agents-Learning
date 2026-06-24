import random


class DummyLLM:

    def __init__(self):
        print('LLM created')

    def predict(self, prompt):

        res_list = [
            'delhi is cap of india',
            'IPL is cricket league',
            'AI is Artificial Intelligence'
        ]

        return {'response': random.choice(res_list)}


# llm = DummyLLM()

# ans = llm.predict('What is cap of india')

# print(ans)


class DummyPromptTemplate:

    def __init__(self, template, input_var):
        self.template = template
        self.input_var = input_var

    def format(self, input_dict):
        return self.template.format(**input_dict)


temp = DummyPromptTemplate(
    template='poem for {topic}',
    input_var=['topic']
)

# ans = temp.format({'topic': 'india'})

# print(ans)


class DummyChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final = self.prompt.format(input_dict)
        result = self.llm.predict(final)
        return result['response']


llm = DummyLLM()

chain = DummyChain(llm=llm, prompt=temp)

ans = chain.run({'topic': 'india'})

print(ans)
