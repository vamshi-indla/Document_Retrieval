# Document_Retrieval

Proof of concept to retrieve documents belonging to a domain.

Steps:
1. Convert PDFs to Text (doc_to_text.py)
  1.1 Preprocess the data
2. Index the documents using inverse-index
3. Query the search terms
  3.1 Keyword search
  3.2 Collabrative filtering approach
  3.2 Semantic search
 4. Ranking the results



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
## Setup Instructions

The code of SSE toolkit support both python2 and python3. Just issue below command to download the repo and install dependencies such as tensorflow.
```bash
git clone https://github.com/vamshi-indla/Document_Retrieval.git
cd Document_Retrieval
./env_setup.sh
```
## Traditional Method for Document Retrieval:
Searching is done in four stages in classical search engines:

Document indexing: Simply index documents :)
Term weighting: Importance of the terms used within the document are calculated with the help of term frequency.
Similarity coefficients: Documents and queries are represented by vectors of term weight.
Retrieval: Retrieval is done by cosine similarity.

### Disadvantages
Term mismatch is the most concerning problem for effective information retrieval. In that, there are multiple kinds of problems namely:

1. Vocabulary problem:
The words on which the documents are indexed (vs) the words in user query are not same
2. Synonymy:
Same words different meanings (Ex: “apple” as company [vs] fruit)
Synonymy may result in a failure to retrieve relevant documents
Decreases Recall
3. Polysemy:
Different words with same meaning (Ex: “television” and “tv”)
Polysemy may cause retrieval of erroneous or irrelevant documents
Decreases Precision of retrieval.
4. Hypernymy and Hyponymy:



## Expanding the Query
1. User inputs query in natural language.
2. Use tools like StanfordParser to identify the noun phrases and other grammar in the query.
3. Related synonym sets of various words in the query are also obtained from Ontology and Word Net API.
4. Add these words to the original query and form the new query.
5. The queries formed will be more refined and are sent to Search API which fetches the results related to the user query. Following diagram depicts the same: image

### Example run
Step 1 - User Query: name of football clubs in EEFA.
Step 2 - Parsed words for this user query using Stanford Parser: 

Step 3 - Word Net and Ontology Synonym words: list, soccer
Step4 - Expanded Query: Name or list the football Soccer clubs in EEFA

### Advantages of semantic search over traditional keyword search:
Tradional keyword search will not be able to understand the difference between: USA Players in Catalan basket team Vs Catalan Palyers in USA teams. Such cases are not a problem for semantic search.

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
 ## Future
 
The next release of InvertedIndex will contain support for proximity searching, which is the ability to search for keywords "near" each other in the indexed document. For instance, a search for the words "Python" and "rules" would return a document containing,
Everybody knows that Python rules!
but not a document containing,
Python! Everybody knows that rules!

t-SNE 300D to 2D for visualiztion
Transfer Learning and Word Embedding.
Word2vec (2013) and SVD?
- CBOW
- Skip Gram with negative Sampling
Glove (2014)

Usecases:
> Analogies
> Predicting next word, using sequence modeling
> Fill up the blanks :)
> Sentiment Analysis

Similarities
> Cosine 
> Wordmoverdistance
> Euclidean Distances

## References
https://github.com/eBay/Sequence-Semantic-Embedding
https://spoddutur.github.io/my-notes/semantic-search-2.html
https://opensourceconnections.com/blog/2013/08/25/semantic-search-with-solr-and-python-numpy/ (collabarative filtering search)
