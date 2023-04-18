# Double-Spend Attack Analysis

Actually, with a zk-rollup layer for omnichians, the `double-spend attack` will finally be settled with certainty. This article presents a detailed analysis of the double-spent attacks without the zk-rollup layer for omnichians, and will prove that the probability of successful DSA is very low with a longer wait time or more synchronizers.  

To understand the analysis, we need some knowledge of [exponential distribution](#exponential-distribution) and [reliability](./reliability-analysis.md). You can ignore the analysis and directly jump to the [results](#results).  

## Simplified Model  

In this simplified model, we will use an [exponential distribution](#exponential-distribution) to describe the working process of the synchronizers. And use another **exponential distribution** to describe the time of successful submission of a smart contract call transaction.  

### Parameters

- `MTBF` is the mean time between failures of the synchronizers, which determines the [$\lambda$](#details-about-the-mtbf) of the **exponential distribution**
- $t_{o}$ is the mean time of a successful submission of a smart contract call transaction when the synchronizer is working. In the simplified model, other factors can be considered as a black box and all of them are finally reflected in the $t_{o}$. For example, if a submission is not confirmed after a short time, the synchronizer will re-submit it again immediately, and this time will be included in the $t_{o}$. The $t_{o}$ determines the $\lambda$ of an **exponential distribution** too  
- $T_{w}$: the waiting time for every omniverse transaction. This time needs to be longer that the operation time of calling a smart contract on the slowest chain.  
- $N_{c}$: the number of blockchains one `ERC-6358` token is deployed  
- $N_{s}$: the number of off-chain synchronizers working for the `ERC-6358` token  

### Principle

*Note that we suppose the attacking user can successfully submit omniverse transactions **with probability `1.0`**, although at the same point, it is with a very low probability that the attacker succeeds but all the synchronizers cannot.*  

- To calculate the probability of a successful submission to one chain by one synchronizer within the $T_{w}$, we need to calculate the probability of successfully submitting the transaction within $T_{w}$, and the synchronizer needs to work more than the submission time at the same time.  

    $$P_{s-1-1}=\int_{0}^{T_{w}}[\int_{t}^{+\infty}{\lambda_{1}e^{-\lambda_{1}x}}dx]\lambda_{2}e^{-\lambda_{2}t}dt=\frac{\lambda_{2}}{\lambda_{1}+\lambda_{2}}(1-e^{-(\lambda_{1}+\lambda_{2})T_{w}})$$

    where $\lambda_{1}=\frac{1}{MTBF}$ and $\lambda_{2}=\frac{1}{t_{o}}$  

- According to the [reliability analysis](./reliability-analysis.md), we need to calculate the probability of the successful submission to one chain with $N_{s}$ synchronizers first:  

    $$P_{s-1-n}=1-(1-P_{s-1-1})^{N_{s}}$$

- and then for $N_{c}$ chains. As submitting to one chain fails then the synchronization fails, the successful synchronization can be calculated as 
 
    $$P_{s-n-n}=(P_{s-1-n})^{N_{c}}$$  

- So the probability of a successful double-spend attacks (DSA) is:  

    $$P_{s-dsa}=1-P_{s-n-n}$$  

### Results

- *The precision of the time is `1` minute.*
- *DSA stands for double-spend attack.*
- The meaning of the [parameters](#parameters) can be found above.

| $MTBF$ | $T_{w}$ | $t_{o}$ | $N_{c}$ | $N_{s}$ | $P_{Successful-DSA}$ | Successful DSA times per year |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 120 | 5 | 5 | 100 | 25 | $2.88\times 10^{-9}$ | 0.002 |
| 120 | 10 | 5 | 100 | 25 | $1.18\times 10^{-18}$ | $6.19\times 10^{-13}$|
| 120 | 10 | 5 | 100 | 10 |  0.00000107 | 0.56|
| 120 | 10 | 10 | 100 | 25 | $5.74\times 10^{-9}$ | 0.003 |
| 120 | 5 | 3 | 30 | 10 | 0.000003 | 1.709 |

## Appendix

### Exponential Distribution

Recall that The probability density function (PDF) of the exponential distribution is given by:  

$$f(x) = \left\\{  \begin{array}{rcl} 
\lambda e^{-\lambda x}, x\geq 0\\ 
0, x\leq 0
\end{array} \hspace{1em} (\lambda>0) \right . $$  

and the cumulative distribution function (CDF) of the exponential distribution can be calculated by:  

$$P(X < t\mid\lambda)=\int_{0}^{t}{\lambda e^{-\lambda t}}dx=1-e^{-\lambda t}$$  

and  

$$P(X > t\mid\lambda)=\int_{t}^{+\infty}{\lambda e^{-\lambda t}}dx=e^{-\lambda t}$$  

The mean and variance of the exponential distribution are given by:

$$Mean = \frac{1}{\lambda}$$  

$$Variance =\frac{1}{\lambda ^ {2}}$$  

#### Calculate the probability of continous failure  

***Note that the calculation of the continous failure probability is not used in the simplified model, but sometimes it's useful.***  

If the probability of failure of device A is exponentially distributed, then the probability that it will fail in a given time interval of length $t$ is given by:

$$P(\text{A fails in }t \text{ units of time}) = 1 - e^{-\lambda t}$$

where $\lambda$ is the failure rate parameter of the exponential distribution. Note that the failure rate parameter is equal to the inverse of the mean time between failures (MTBF).

To solve for the probability that A will fail continuously for a fixed period of time $T$, we need to calculate the probability that A fails in each of $n$ non-overlapping time intervals of length $t$. We can assume that the time intervals are small enough so that the probability of multiple failures within a single interval is negligible.

If the time intervals are all of length $t$, then the probability that A fails in each of the $n$ intervals is:

$$P(\text{A fails in each of }n\text{ intervals}) = [1 - e^{-\lambda t}]^n$$

If we let $n = \frac{T}{t}$, then the probability that A fails continuously for the fixed period of time $T$ is:

$$P(\text{A fails continuously for time }T) = [1 - e^{-\lambda t}]^{\frac{T}{t}}$$

This formula can be used to calculate the probability of continuous failure for any fixed period of time $T$, given the failure rate parameter $\lambda$ of the exponential distribution.

#### Details about the `MTBF`

The failure rate parameter $\lambda$ in an exponential distribution is determined by the mean time between failures (MTBF) of the device. The MTBF represents the average time between failures for a device, and is usually measured in hours or some other unit of time.

The relationship between the failure rate parameter $\lambda$ and the MTBF is given by:

$$\lambda = \frac{1}{\text{MTBF}}$$

Thus, if the MTBF of a device is known, the failure rate parameter can be calculated. Similarly, if the failure rate parameter is known, the MTBF can be calculated as:

$$\text{MTBF} = \frac{1}{\lambda}$$

The failure rate parameter $\lambda$ is a key parameter in determining the probability of failure for a device, and is commonly used in reliability analysis and modeling of systems.
