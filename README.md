# Simple RAG
This project is focused on developing an advanced chatbot using large language models (LLMs) with sophisticated indexing techniques to improve the quality of responses. The project covers various stages from data crawling, indexing, to evaluation, and aims to optimize the chatbot's ability to handle queries effectively.

## Table of Contents
1. [Quest 1: LLM Integration](#quest-1)
    - [Config](#config)
    - [Generate API URL with API key to call Gemini model](#generate-api-url-with-api-key-to-call-gemini-model)
    - [Prompt](#prompt)
    - [Translation Request](#translation-request)
2. [Chatbot Development](#chatbot-development)
    - [Data Access and Indexing](#data-access-and-indexing)
        - [Crawl Data](#crawl-data)
        - [Insert chunks of text](#insert-chunks-of-text)
        - [Create collection, add Docs function](#create-collection-add-docs-function)
        - [BM25 (Best Matching 25)](#bm25-best-matching-25)
        - [Hybrid Search](#hybrid-search)
        - [Maximal Marginal Relevance (MMR)](#maximal-marginal-relevance-mmr)
        - [Indexing Based on Chunksize](#indexing-based-on-chunksize)
        - [Topic-Based Indexing](#topic-based-indexing)
    - [Chatbot Development](#chatbot-development)
        - [Generate Question - Ground truth for Evaluation](#generate-question-ground-truth-for-evaluation)
        - [Collect answer from Chatbot](#collect-answer-from-chatbot)
        - [Indexing by Topic](#indexing-by-topic)
        - [Indexing by Chunksize](#indexing-by-chunksize)
    - [Evaluation - Bert Score](#evaluation-bert-score)
        - [BERTScore](#bertscore)
        - [Eval Chunksize Verse](#eval-chunksize-verse)
        - [Eval Topic Verse](#eval-topic-verse)
3. [Conclusion](#conclusion)
    - [Comments on Indexing Results](#comments-on-indexing-results)
    - [Drawbacks of Topic-Based Indexing When Scaling Up](#drawbacks-of-topic-based-indexing-when-scaling-up)
    - [Indexing Based on Chunksize](#indexing-based-on-chunksize)

---

## Quest 1: LLM Integration

### Config
Setup and configuration details for integrating Large Language Models (LLMs) like Gemini.

### Generate API URL with API Key to Call Gemini Model
Generate a valid API URL using your API key to interact with the Gemini model for various NLP tasks.

### Prompt
Define the prompts that the LLM will use to generate responses based on user queries.

### Translation Request
Translate text using LLM capabilities to support multilingual chatbot functions.

---

## Chatbot Development

### Data Access and Indexing

#### Crawl Data
Crawl the necessary data for indexing and training purposes.

#### Insert Chunks of Text
Process and insert chunks of text into the system for indexing.

#### Create Collection, Add Docs Function
Create a collection for storing documents and the necessary functions for adding documents.

#### BM25 (Best Matching 25)
Implement BM25 to rank documents based on relevance using term frequency and inverse document frequency.

#### Hybrid Search
Utilize Hybrid Search, which combines dense and sparse retrieval methods, to optimize the search process.

#### Maximal Marginal Relevance (MMR)
Use MMR to diversify the search results and reduce redundancy in the retrieved documents.

#### Indexing Based on Chunksize
Index documents based on chunks of text, splitting large documents into smaller manageable pieces.

#### Topic-Based Indexing
Implement topic-based indexing to organize documents based on their content and improve retrieval relevance.

### Chatbot Development

#### Generate Question - Ground Truth for Evaluation
Generate questions to evaluate the chatbot’s performance, providing a reference for comparison.

#### Collect Answer from Chatbot
Collect answers from the chatbot based on the generated questions.

#### Indexing by Topic
Implement indexing by topic, where documents are grouped by subject matter for better query results.

#### Indexing by Chunksize
Index documents based on chunks of text for granular control over the retrieval process.

### Evaluation - Bert Score

#### BERTScore
Evaluate the chatbot's response quality using BERTScore, a metric that measures the semantic similarity between generated text and reference text.

#### Eval Chunksize Verse
Evaluate the performance of chunk-based indexing in comparison to other methods.

#### Eval Topic Verse
Evaluate the performance of topic-based indexing in the context of the chatbot.

---

## Conclusion

### Comments on Indexing Results
Provide insights on the performance of the different indexing techniques (topic-based and chunksize).

### Drawbacks of Topic-Based Indexing When Scaling Up
Discuss the potential limitations of topic-based indexing when dealing with larger datasets and scalability issues.

### Indexing Based on Chunksize
Analyze the benefits and drawbacks of indexing based on chunksize for document retrieval.

---

## Access the Product

To use the product, please visit the following link:

[Product on Render](https://prj-python-code.onrender.com/)

We have an error reporting page available. If you encounter any issues or bugs, feel free to report them, and we will get back to you with a solution. (Database: MongoDB)

You can provide feedback, and we will respond to your queries via your provided email.

Your feedback is valuable to us, and we strive to improve the product continuously.
