# Jenkins

Jenkins is a software that allows **continous integration**. It will be installed on a server where the central build takes place. Essentially
it takes the changed source code from a developer and trigger a build and run any tests if required. The output will then be available in the
Jenkins dashboard. Automatic notifcations can also be sent back to the developer.

## What is Continuous Integration?

Continuous integration is a development practice that requires developers to integrate code into a shared repository at regular intervals. This
concept was meant to remove the problem of finding later occurence of issues in the build lifecycle. Continuous integration requires the developers to have frequent builds. The common practice is that whenver a code commit occurs, a build should be triggered.
