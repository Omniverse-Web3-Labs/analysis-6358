## Calculate the probability of continous failure 

If the probability of failure of device A is exponentially distributed, then the probability that it will fail in a given time interval of length $t$ is given by:

$$P(\text{A fails in }t \text{ units of time}) = 1 - e^{-\lambda t}$$

where $\lambda$ is the failure rate parameter of the exponential distribution. Note that the failure rate parameter is equal to the inverse of the mean time between failures (MTBF).

To solve for the probability that A will fail continuously for a fixed period of time $T$, we need to calculate the probability that A fails in each of $n$ non-overlapping time intervals of length $t$. We can assume that the time intervals are small enough so that the probability of multiple failures within a single interval is negligible.

If the time intervals are all of length $t$, then the probability that A fails in each of the $n$ intervals is:

$$P(\text{A fails in each of }n\text{ intervals}) = [1 - e^{-\lambda t}]^n$$

If we let $n = \frac{T}{t}$, then the probability that A fails continuously for the fixed period of time $T$ is:

$$P(\text{A fails continuously for time }T) = [1 - e^{-\lambda t}]^{\frac{T}{t}}$$

This formula can be used to calculate the probability of continuous failure for any fixed period of time $T$, given the failure rate parameter $\lambda$ of the exponential distribution.

## Detales about the $\lambda$

The failure rate parameter $\lambda$ in an exponential distribution is determined by the mean time between failures (MTBF) of the device. The MTBF represents the average time between failures for a device, and is usually measured in hours or some other unit of time.

The relationship between the failure rate parameter $\lambda$ and the MTBF is given by:

$$\lambda = \frac{1}{\text{MTBF}}$$

Thus, if the MTBF of a device is known, the failure rate parameter can be calculated. Similarly, if the failure rate parameter is known, the MTBF can be calculated as:

$$\text{MTBF} = \frac{1}{\lambda}$$

The failure rate parameter $\lambda$ is a key parameter in determining the probability of failure for a device, and is commonly used in reliability analysis and modeling of systems.

## Double-Spend Attack Analisys

- $T_{w}$: the waiting time for every omniverse transaction
- $t_{r}$: the recovery time for the failure of a submission to the `ERC-6358` smart contracts on one blockchain
- $N_{c}$: the number of blockchains one `ERC-6358` token is deployed  
- $N_{s}$: the number of off-chain synchronizers working for the `ERC-6358` token  
- We suppose the attacking user can successfully submit omniverse transactions **with probability `1.0`**, although at the same point, it is with a very low probability that the attacker succeeds but all the synchronizers cannot.  

### Continous failure of synchronizers for $T_{w}$  

- One synchronizer for one chain

$$P_{one-sync-one-chain}=[1 - e^{-\lambda t_{r}}]^{\frac{T_{w}}{t_{r}}}$$

- One synchronizer for $N_{c}$ chains  

$$P_{one-sync-N-chains}=[1 - (e^{-\lambda t_{r}})^{N_{c}}]^{\frac{T_{w}}{t_{r}}}$$

- $N_{s}$ synchronizers for $N_{c}$ chains. This is the probability that the synchronization of a transaction has failed, which can be considered as the probability of a successful double-spend attack under the suppose mentioned above.  

$$P_{Successful-DSA}=P_{sync-fail}=([1 - (e^{-\lambda t_{r}})^{N_{c}}]^{\frac{T_{w}}{t_{r}}})^{N_{s}}$$

### Results

- *The precision of the time is `1` minute.*
- *DSA stands for double-spend attack.*

| $MTBF$ | $T_{w}$ | $t_{r}$ | $N_{c}$ | $N_{s}$ | $P_{Successful-DSA}$ | Successful DSA times per year |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| 120 | 5 | 2 | 20 | 5 | $1.43\times 10^{-7}$ | 0.075 |
| 120 | 10 | 2 | 100 | 15 | $1.52\times 10^{-7}$ | 0.08 |
| 120 | 5 | 2 | 100 | 25 | $2.08\times 10^{-6}$ | 1.09 |
