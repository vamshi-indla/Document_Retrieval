# Document_Retrieval

Proof of concept to retrieve documents belonging to a domain.




### [Content](#content)

* [Setup Instructions](#setup-instructions)
* [Traditional Method for Document Retrieval](## Traditional Method for Document Retrieval)
    * [Approach](### Approach)
    * [Disadvantages](### Disadvantages)
*  [Semantic Search](## Semantic Search)
    * [Approach](###Approach)
    * [Expanding the Query](###  Expanding the Query
    * [Advantages of semantic search over traditional keyword search](### Advantages of semantic search over traditional keyword search)
*  [Usecases](## Usecases)
*  [Further Reading](## Further Reading)
*  [References](## References)

---
## Setup Instructions

 Just issue below command to download the repo and install dependencies such as tensorflow.
```bash
git clone https://github.com/vamshi-indla/Document_Retrieval.git
cd Document_Retrieval
./env_setup.sh
```
## Traditional Method for Document Retrieval
Searching is done in four stages in classical search engines:

Document indexing: Simply index documents :)
Term weighting: Importance of the terms used within the document are calculated with the help of term frequency.
Similarity coefficients: Documents and queries are represented by vectors of term weight.
Retrieval: Retrieval is done by cosine similarity.

### Approach
1. Convert PDFs to Text (doc_to_text.py)
  1.1 Preprocess the data
2. Index the documents using inverse-index
3. Query the search terms
  3.1 Keyword search
  3.2 Collabrative filtering approach
  3.2 Semantic search
 4. Ranking the results

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


## Semantic Search
 
### Approach
1. Preprocessing data
2. Finding Synonyms, Polysemy , Hypernymy and Hyponymy
3. Creating topics
4. Create Domain specific Word Embeddings OR Use Transfer Learning
   - Word2vec (2013) and SVD?
   - CBOW
   - Skip Gram with negative Sampling
   - Glove (2014)
   - SVD , similar to PCA
5. Preprocess Query
6. Expand the Query
7. Find the nearest document to Query
    - Cosine 
    - Wordmoverdistance
    - Euclidean Distances
 

###  Expanding the Query
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

### Advantages of semantic search over traditional keyword search
Tradional keyword search will not be able to understand the difference between: USA Players in Catalan basket team Vs Catalan Palyers in USA teams. Such cases are not a problem for semantic search.

## Further Reading
 
The next release of InvertedIndex will contain support for proximity searching, which is the ability to search for keywords "near" each other in the indexed document. For instance, a search for the words "Python" and "rules" would return a document containing,
Everybody knows that Python rules!
but not a document containing,
Python! Everybody knows that rules!

t-SNE 300D to 2D for visualiztion
Transfer Learning and Word Embedding.
 - Address Bias in Word Embedding(2016)
Word2vec (2013) and SVD?
- CBOW
- Skip Gram with negative Sampling
Glove (2014)
SVD , similar to PCA
Attention Model(2014)

## Usecases
1 Analogies
2 Predicting next word, using sequence modeling
3 Fill up the blanks :)
4 Sentiment Analysis
    - Word Embeddings is best, when small train labeled examples
    - Use average or Sum of all the embeddings and that can work. However it fails for Sarcarm examples. Ex: lacking good taste.
    - Use RNNs or LSTM in that scenario
5  Machine Translation and Captioning an image
    - Greedy Search
    - Beam Search 
6 Speech Recognition
    
## References
https://github.com/eBay/Sequence-Semantic-Embedding
https://spoddutur.github.io/my-notes/semantic-search-2.html
https://opensourceconnections.com/blog/2013/08/25/semantic-search-with-solr-and-python-numpy/ (collabarative filtering search)
