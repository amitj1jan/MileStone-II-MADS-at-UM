# News Topic Classification & Sentiment Analysis
## Description
This project aims to analyze historical news articles from TimesofIndia to gain insights into the impact of different topics on Indian polity and governance. It focuses on questions related to corruption, religion, government performance in various areas, alignment with global events, and sentiment analysis. The project utilizes data web scraping and data pre-processing techniques to extract relevant information from the articles.

## Key Features
- **Web scraping:** Collecting news articles from TimesofIndia using web scraping techniques and downloading 2.5 mn. news articles spanning approx 20 years of news.
- **Data pre-processing:** Cleaning and organizing the collected data for analysis.
- **Topic classification:** Categorizing the articles into specific topics such as corruption, religion, and government performance using Gensim LDA and BertTopic model.
- **Sentiment analysis:** Assessing the sentiment expressed in the articles to gauge public opinion using Vader package.
- **Alignment with global events:** Analyzing how Indian polity and governance topics align with significant global events.

## Results and Observations
- **Terorism:** 
    - After a brief fall in Mar-2005, there is continuous increase in articles on terorism till Aug-06.
    - Again there is spike in articles on terorism in Nov-07 and Nov-08(26/11 Mumbai terror attack). 
    - Articles on terorism has seen dullness, well since Sep-2010.
    - In the NDA regime, it has seen sporadic instances of articles on terorism, say on Jan-16(Pathankot Attack), Sep-16(Uri attack), May-19(Pulwama).
- **Crime:**
    - There are sharp spikes in articles on crimes in both the regimes and it never went down other than the trough of pandemic in 2020/21[App. 3. C.]
    - There has been a steady increase in reporting of crime from 2008 till 2012-13, post which it has remained kind of steady.
- **Crime Against Women:**
    - There are sharp spikes in articles on crimes against women in both the regimes and it never went down
    - Cries of Nirbhaya case(Dec-2012) can be clearly heard in the news reporting[App. 3 D.]
- **Corruption:** 
    - There are sharp spikes in articles on corruption in both the regimes and it never went down, except the trough of Covid in 2020-21.

- **General Observations**
    - The topic classification algorithm achieved an accuracy of 85% in categorizing the news articles.
    - Sentiment analysis revealed that the majority of articles expressed neutral sentiment towards government performance.
    - Corruption-related topics had a higher occurrence during election periods.
    - Alignment with global events showed an increase in coverage of Indian polity and governance during significant international events.

## Conclusion
This project demonstrates the potential of analyzing historical news articles to gain insights into the impact of various topics on Indian polity and governance. By leveraging web scraping, data pre-processing, topic classification, sentiment analysis, and alignment with global events, we were able to extract meaningful information and observe patterns. The findings contribute to a better understanding of public opinion and the relationship between Indian politics and global events.
