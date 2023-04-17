# Reliability Analysis

## Structure Functions

<p align="center" id = "parallel-components">Figure.1 Parallel Components </p>  

![image](https://user-images.githubusercontent.com/83746881/232553371-3faa9b5e-1897-4e57-b9b4-b330e940a24a.png)  

- In parallel-components structure, there's only need one successful component in each step
- The steps are in series, so in order to succeed, all the steps need to be successful  

<p align="center" id = "parallel-system">Figure.2 Parallel Systems </p>  

![image](https://user-images.githubusercontent.com/83746881/232553406-0396f057-47ec-4f04-aad5-bc807b7533ff.png)  

- In parallel-system structure, the systems are independent and parallel
- To secceed, at least one system works 

It can be proved that if all the corresponding components in the two diagrams are identical, the success probability in [Parallel Components (Figure.1)](#parallel-components) is greater than [Parallel Systems (Figure.2)](#parallel-system).  

In [the simplified model of DSA analysis](dsa-analysis.md#simplified-model), successful synchronization needs all the chains to get the successful submission, but for a single chain, the successful submission can be made by any synchronizer. In addition there's no need for. So the model is related to the [Figure.1](#parallel-components).  
