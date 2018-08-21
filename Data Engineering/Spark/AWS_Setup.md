The purpose of this document is to provide a detailed guide as to how to set up an automate data pipeline using AWS Data Pipeline to perform MapReduce jobs on data stored on AWS S3 buckets

### When Is This Necessary?
The need for an automated pipeline that provisions multiple nodes to perform a job is often needed when writing a data job that performs processing on large data sets to get some form of transformation from it and send it back to some form of storage (Ex. Amazon S3 Bucket). The distributed computing power ensures that the job finishes in a reasonable amount of time.

### What Is AWS Data Pipeline?
AWS Data Pipeline is a feature provided by Amazon on its' web service platform to allow the scheduled performance of MapReduce jobs using their Elastic Map Reduce clusters (EMR). EMR is in itself simply Amazon node instances with whatever MapReduce framework you need installed on it (Ex. Spark). The benefit of using this feature is that the node clusters used to perform

MapReduce jobs are only turned on for the duration of the job and then are automatically turned off when the job is complete. This saves NVIDIA fees that would be paid if the cluster is constantly kept turned on - even when it's not servicing any particular job.
