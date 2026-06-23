from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()
model1 = ChatGroq(model="llama-3.1-8b-instant")
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 1st prompt: detailed report
prompt1 = PromptTemplate(
    template='Write a short and simple notes on \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short Q/A from \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge provided notes and quiz into single document \n notes -> {notes}, quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merged_chain = prompt3 | model2 | parser

chain = parallel_chain | merged_chain

text = """How Natural Language Processing Works
1. Text or Speech Input
Receiving text data: The system takes written language like sentences or documents which is called text acquisition.
Receiving voice input: When the input is audio, it is first converted into text using Speech Recognition.
2. Pre-processing
The text is cleaned and prepared. It can include:

Removing punctuation or noise: Cleaning unwanted characters or symbols from text is done using text normalization.
Splitting into words: Breaking sentences into smaller units so they can be processed easily.
Converting to lowercase: Changing all words into the same case for uniform processing is known as case folding.
Removing common words: Eliminating frequent words like is, the, and to focus on meaningful terms.
Reducing words to base form: Converting words like running to run to reduce computational power.
3. Language Analysis
The system studies structure and meaning:

Grammar detection: Identifying nouns, verbs, and other parts of speech in a sentence is done.
Word relationships: Finding how words connect to each other in a sentence.
Context understanding: Determining the actual meaning of a word based on surrounding text.
Finding names and places: Detecting entities like person names, locations, or dates.
Sentiment detection: Identifying whether text expresses positive, negative or neutral emotion.
4. Text Representation and Embedding Techniques
Since machines process numbers, this stage converts text into numerical vectors.

Text representation: In this step, text is converted into numbers using statistical features or vector representations so machines can process it.
Traditional representations: Earlier methods represent text using word counts and importance scores.
Word embeddings: Modern methods represent words as dense vectors capturing similarity and meaning.
Contextual embeddings: Advanced models generate word meanings based on the surrounding sentence."""


result = chain.invoke({'text': text})

print(result)

chain.get_graph().print_ascii()