# Jenkins

Jenkins is a software that allows **continous integration**. It will be installed on a server where the central build takes place. Essentially
it takes the changed source code from a developer and trigger a build and run any tests if required. The output will then be available in the
Jenkins dashboard. Automatic notifcations can also be sent back to the developer.

## What is Continuous Integration?

Continuous integration is a development practice that requires developers to integrate code into a shared repository at regular intervals. This
concept was meant to remove the problem of finding later occurence of issues in the build lifecycle. Continuous integration requires the developers to have frequent builds. The common practice is that whenver a code commit occurs, a build should be triggered.

## Historical Use

Back in the day, there was a phase in the development team which was called the Integration Phase. During this phase, code changes made by
individual developers or small teams were brought together piecemeal and forged into a working product. This was difficult and tedious, and took months sometimes to integrate conflicting changes. It was very hard to anticipate the types of issues that would crop up, and even harder to fix them.

By using Continuous Integration, we have a tool that monitors the version control system for changes. Whenever a change is detected, this tool automatically compiles and tests your application. If something goes wrong, the tool immediately notifies the developers so that they can fix  the issue.

## Usage of Jenkins and CI

- Helps keep tabs on the health of code base, automatically monitoring code quality and code coverage metrics, and helping keep technical
debt down and maintenance costs low.
- Acts as a communication tool, publishing a clear picture of the current state of development efforts. It can simplify and accelerate delivery by helping you automate the deployment process, letting you deploy the latest version of your application either automatically or as a one-click process.

## So is Continuous Integration Always the Best?

A pure Continuous Deployment approach is not always appropriate for everyone. For example, many users would not appreciate new versions falling into their laps several times a week, and prefer a more predictable (and transparent) release cycle.
