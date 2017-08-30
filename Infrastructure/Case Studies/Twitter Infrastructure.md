# Twitter Infrastructure

https://blog.twitter.com/engineering/en_us/topics/infrastructure/2017/the-infrastructure-behind-twitter-scale.html

- Started migration from third party hosting in early 2010 to internal infrastructure. They began iterating through
various network designs, hardware, and vendors.

- By late 2010, they finalized first network architecture, designed to scale and service issues encountered in the hosted
colo.

- They had **deep buffer ToRs (Top of the Rack)** to support bursty service traffic and **carrier grade core switches** with 
no oversubscription at that layer.

- Such a implementation supported them through high **TPS** hit during Caste in the Sky and World Cup 2014.

- A few years later, they were running a network with **POPs** on five continents and data centers with hundres of thousands
of servers. In early 2015, they were suffering due to changing service architecture and increased capacity needs, leading to
physical scalability limits in the data center when a full mesh topology would not support additional hardware needed to add
racks.

- Existing data center **IGP** began to behave unexpectedly due to increasing **route scale** and **topology complexity**
