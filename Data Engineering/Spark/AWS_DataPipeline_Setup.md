The purpose of this document is to provide a detailed guide as to how to set up an automate data pipeline using AWS Data Pipeline to perform MapReduce jobs on data stored on AWS S3 buckets

### When Is This Necessary?
The need for an automated pipeline that provisions multiple nodes to perform a job is often needed when writing a data job that performs processing on large data sets to get some form of transformation from it and send it back to some form of storage (Ex. Amazon S3 Bucket). The distributed computing power ensures that the job finishes in a reasonable amount of time.

### What Is AWS Data Pipeline?
AWS Data Pipeline is a feature provided by Amazon on its' web service platform to allow the scheduled performance of MapReduce jobs using their Elastic Map Reduce clusters (EMR). EMR is in itself simply Amazon node instances with whatever MapReduce framework you need installed on it (Ex. Spark). The benefit of using this feature is that the node clusters used to perform

MapReduce jobs are only turned on for the duration of the job and then are automatically turned off when the job is complete. This saves NVIDIA fees that would be paid if the cluster is constantly kept turned on - even when it's not servicing any particular job.

## Step 1. Preparing Your Job Script To Be Used

1. Log on to the AWS account we use and click Services on the top bar. From there select the S3 Storage feature and create a bucket for ETL Job scripts
2. Upload your MapReduce script to this bucket

## Step 2. Setting Up A Data Pipeline

- Click on Services on the top bar of the AWS platform and select the Data Pipeline feature.
- Select "Create new pipeline"
- Give your pipeline a Name and Description
- Choose "Build using a template" from the form and select the "Elastic MapReduce (EMR) Templates" 
- Select a Core Node Instance Type that suits the requirements of your job. You can see a list of node types AWS offers at  https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-emr-supported-instance-types.html
- The type of node you choose really depends on what you need for your job (Ex. Memory Optimized, Storage Optimized, Computer Optimized).

Ensure you add the command you would perform to run your job on the EMR Step. This includes the parameters you want to pass in terms of the many Map Reduce configurations you can have (Ex. Executor Memory, Number of Executors). An example command is seen below. The command-runner.jar is used to run the script (the directory of where this is is automatically known by AWS so you just need to add it to the command like below). The parameters must be comma separated.

```
command-runner.jar,spark-submit,s3://gfn-etl-jobs/sparkjob.py,--deploy-mode,cluster,--master,yarn,--executor-memory,20G,--driver-memory,20G,--num-executors,14,--executor-cores,5
```

- IMPORTANT: Make sure to set the EMR Release Label to emr-5.15.0 or higher. The version that is default runs MapReduce frameworks as much older version that do not have a lot of the features you might be using
- Set the Core Node Instance Count to an appropriate number of nodes - this really depends on how large of a set of data you are processing and what type of core node instance you have added.
- Set the Master Node Instance Type to an appropriate node as in step 4 a.

- Under the Schedule section you may configure the pipeline to run on a specific schedule.
- Under the Pipeline Configuration enable Logging and set the S3 location to "s3://gfn-etl-jobs/logs/"
- Under the Security/Access section you want to have a IAM role that gives you control over the AWS Data Pipeline and EC2 Applications. (Ex. I used DataPipelineDefaultRole and DataPipelineDefaultResourceRole)

## Step 3. Setting Up A Data Pipeline

1. On the bottom of the page select Edit In Architect
2. Select the Resources tab and "Add an Optional Field" - here you want to add "Applications". Under this, you want to include the frameworks you would like to use. The Data Pipeline automatically installs Hive and Pig by default but if you want to use for example, Spark, you need to add it under this form.
3. Still under the Resources tab locate the "Terminate After" tab and configure the time here depending on how long you expect your job to take. Otherwise the pipeline may terminate before your job is fully finished.
4. On the top tab select Save and then Activate to start up your pipeline

## Step 4. Pipeline Analysis and Maintenance

Now the pipeline is set up you can view the pipeline on the Data Pipeline dashboard. You can select it to view more of its' execution details. You can visit the EMR feature under Services to see the nodes spin up to run your job when the pipeline is running.

If an error occurs you can visit the logs on the data pipeline which will indicate to you any issues that may have impeded the data processing.

### Common Reasons for Failure:

- You did not provide enough memory - this can be fixed by increasing the parameters passed in Step 2. 4) b. for the EMR Step.
- You allocated enough memory as a parameter, but the type of node you added doesn't have enough memory to provide that much - this can be fixed by upgrading the node type
- You forgot to add the framework you need in Step 3. 2)  to perform your job (Ex. Spark)
