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

- Existing data center **IGP** began to behave unexpectedly due to increasing **route scale** and **topology complexity**.
To address this, converted existing data centers to a **Clos** topology + **BGP** – a conversion which had to be done on a live network, yet, despite the complexity, was completed with minimal impact to services in a relatively short time span.

The network looked like this:

![alt tag](https://blog.twitter.com/content/dam/blog-twitter/engineering/en_us/infrastructure/2017/behind-twitter-scale/eng_infra_007.png.img.fullhd.medium.png)

## Highlights of New Network

- Smaller blast radius of a single device failure
- Horizontal bandwidth scaling capabilities
- Lower routing engine CPU overhead; far more efficient processing of route updates.
- Higher route capacity due to lower CPU overhead.
- More granular control of routing policy on a per device and link basis.
- No longer exposed to several known root causes of prior major incidents: increased protocol reconvergence times, route churn issues and unexpected issues with inherent OSPF complexities.
- Enables non-impacting rack migrations.

## Storage

Hundreds of millions of Tweets are sent every day. They are processed, stored, cached, served and analyzed.

With such massive content, we need a consequent infrastructure. Storage and messaging represents 45% of Twitter’s infrastructure footprint.

Following services were provided by their storage and messaging teams:

![alt tag](https://blog.twitter.com/content/dam/blog-twitter/engineering/en_us/infrastructure/2017/behind-twitter-scale/eng_infra_002.png.img.fullhd.medium.png)

### Challenges

**scale multi-tenancy**: Often customers have corner cases that would impact existing tenants and force us to build dedicated clusters. More dedicated clusters increases the operational workload to keep things running.

## Chronological Evolution

Twitter was built on MySQL and originally all data was stored on it. Went from a small database instance to a large one, and eventually many large database clusters. Manually moving data across MySQL instances requires a lot of time consuming hands on work, so in April 2010 they introduced Gizzard – a framework for creating **distributed datastores**.

Introduced FlockDB, a **graph storage solution** on top of Gizzard and MySQL, and in June 2010, Snowflake our **unique identifier service**. 2010 was also when we invested in Hadoop. Originally intended to store MySQL backups, it now is heavily used for analytics.

2010 - Added Cassandra as a storage solution, and while it didn’t fully replace MySQL due to it’s lack of an auto-increment feature, it did gain adoption as a metrics store.

- As traffic was growing exponentially, needed to grow the cluster, and, in April 2014 they built Manhattan: real-time, multi-tenant distributed database. Since then Manhattan has become one of their common storage layers and Cassandra has been deprecated.

### Lessons Learned

- Started protecting storage layers from abuse by sending a **back pressure signal** and enabling **query filtering**.

## Big Wins

- Code linting, style check hooks, documenting of best practices, and holding regular office hours.

With linting tooling (puppet-lint) they were able to conform to common community linting standards. Reduced our linting errors and warnings in our codebase by 10s of thousands of lines and touched more than 20% of the codebase.
