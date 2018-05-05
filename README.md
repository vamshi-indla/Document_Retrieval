# Document_Retrieval

Proof of concept to retrieve documents belonging to a domain.

Steps:
1. Convert PDFs to Text (doc_to_text.py)
  1.1 Preprocess the data
2. Index the documents using inverse-index
3. Query the search terms
  3.1 Keyword search
  3.2 Semantic search
 4. Ranking the results


```bash
git clone https://github.com/vamshi-indla/Document_Retrieval.git
cd Document_Retrieval
./env_setup.sh
```

### [Content](#content)

* [Setup Instructions](#setup-instructions)
* [SSE Model Training](#sse-model-training)
    * [Basic Idea](#basic-idea)
    * [Training Data](#training-data)
    * [Train Model](#train-model)
    * [SSE Visualization](#sse-visualization)
* [Index Generating](#index-generating)
* [Command Line Demo](#command-line-demo)
* [Setup WebService](#setup-webservice)
* [Call WebService to get results](#call-webservice-to-get-results)
* [Build Your Own NLP task services with your data](#build-your-own-nlp-task-services-with-your-data)
    * [Text Classification](#text-classification)
    * [Search Relevance Ranking](#search-relevance-ranking)
    * [Cross-Lingual Information Retrieval](#cross-lingual-information-retrieval)
    * [Question Answering](#question-answering)
* [References](#references)

---


* **rawdata-ranking**: 

  This search ranking sample data contains nearly 1 million product titles and 84K search queries about Clothes, Shoes and Accessariese in eCommerce domain. The source sequence data is user search query, and the target sequence data is a list of relevant listing titles corresponding to the given query. The unziped DataSet.tar.gz contains three text files named as TrainPairs, EvalPairs and targetIDs. The targetIDs file contains nearly 1 million listing titles and listing_ID, seperated by tab. The format of TrainPair/EvalPair is source_sequence(search query) and list of relevant listing ids. 
  
  An example line in targetIDs file:
  ```
  air jordan xii 12 white/dynamic pink size 4y 7y valentine's day gs pre order	Item#876583
  ```

  An example line in TrainPair file:
  ```
  air jordan 12 gs dynamic pink	Item#876583|Item#439598|Item#563089|Item#709305|Item#460164|Item#45300|Item#791751|Item#523586|Item#275794|Item#516742|Item#444557|Item#700634|Item#860517|Item#775042|Item#731907|Item#852612|Item#877692|Item#453434|Item#582210|Item#200407|Item#196434
  ```
## References
https://github.com/eBay/Sequence-Semantic-Embedding
