# Real_Time_Stock_Price_Analysis

In today's data-driven financial markets, vast amounts of stock price information are generated 
continuously across global exchanges. Analyzing these high-frequency datasets efficiently presents 
significant computational challenges, particularly when extracting meaningful patterns and trends. 
Traditional analysis methods often prove inadequate for processing real-time market data at scale, 
creating a pressing need for distributed computing solutions. 
This project implements a robust big data pipeline for real-time stock price analysis using Hadoop's 
distributed ecosystem. Focusing on five major stocks (IBM, AAPL, GOOGL, MSFT, and AMZN), 
we demonstrate how Hadoop's MapReduce framework can effectively process and analyze time
series financial data. Our approach collects live market data through the Alpha Vantage API, stores 
it in the Hadoop Distributed File System (HDFS), and performs distributed computations to identify 
key metrics including daily price ranges, volatility patterns, and trend correlations. 
By leveraging Python for both data processing and interactive visualization, this solution bridges 
the gap between large-scale financial data processing and actionable market insights. The project 
showcases how modern big data technologies can transform financial analysis, enabling more 
informed investment decisions through scalable, real-time processing of market information. This 
approach not only addresses the limitations of traditional analytical tools but also provides a 
foundation for developing more sophisticated algorithmic trading strategies and risk assessment 
models. 
