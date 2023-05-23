# Financial Modelling using Quantum Computing

This repsoitory holds code examples supporting the chapters of the book.

### Python environment

Make sure you create a local environment and install listed requirements before running the code.
```
pip install -r requirements.txt
```

Also, additional connectivity to DWave, IBM and cloud providers (Azure, AWS) will require accounts in those services to fully reproduce existing bits of code.

### Data retrieval

Data shown under the data folder is the one used by all the examples. It was obtained using Binance's API and the script named _retrive_data.py_ using the following command
```
python retrieve_data.py --day "2022-11-04"
```

That command looks back for 30 days and retrieves data from 5 assets by default. More information on how to use this functionality can be obtained by the command
```
python retrieve_data.py --help
```

## Chapter 4: Derivatives Valuation

Derivative pricing is one of those canonical examples in finance modelling. It tries to set the price for an option at a time $t$ in the future. We will explore how to create those predictions by using both classical and quantum computing resources.

## Chaper 5: Portfolio Optimization

Portfolio optimization another of those examples where a subset from all the available STOCKs should be selected so that the selection meets budget and risk willingness constraints while maximizing the expected revenue from the asset selection.

## Chapter 6: Credit Risk Analytics

This chapter performs a risk analysis in UK househoolds using classical and quantum Machine Learning models to develop models for risk analysis and assess the financial stability for a given case. This chapter explores several techniques such as SVM and NN so a working knowledge on those will help the reader catch up when the Quantum version is presented.

## Chapter 7: On Cloud connectivity and resource estimation

This chapter revolves around how to connect to major Cloud providers and their Quantum Computing offering. It is important that there exists a resource estimation before sending the circuits to the cloud hosted resource given these can be rather expensive devices to use.

## Chapter 8: On Simulators and emulators

It is important we understand the fundamental differences between the two and the role noise plays when emulating our circuits in a realstic setup. Restrictions given by the physical chip need to be taken into consideration when transpiling the theoretical circuit.

## Chapter 9: On handling noise

In this chapter we covered some interesting facts regarding current NISQ devices. On e needs to be aware of the complications that will be faced when working on actual devices and how to deal with their _imperfections_. It is just a brief reference on some of the problems and pottential techniques to aliviate those.
