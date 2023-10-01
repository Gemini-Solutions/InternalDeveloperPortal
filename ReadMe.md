## What is an IDP
An internal developer portal is one stop solution designed to support and facilitate collaboration and development within an organization's teams working closely for delivery. It does so by abstracting away all
the nitty girities of the complete tech stack, giving visibility to what is actually needed to be effecient serving different personas. The developer portal must have an aesthetic UI and a great UX to keep the
customers engaging with minimal to no learning curve.

## How does it work & how it is different from CICD tools like Jenkins, Argo, K8s dashboard, Service Now etc?
IDP is not the replacement to any of these tools rather, it will act as a portal to all these tools, rendering information from these golden source of truth into what exactly is needed by the team in
rather more comprehensive manner. These tools are focussed on different domains and tech specs, like Jenkins primarily focuses on Jobs stage and pipelines, argo CD in tandem with K8s helps achieve gitops , 
K8s dashboard is insight into my cluster and service now acting as catalog for my apps within the org, IDP would simply source the data from these tools and nourish it on the UI by establishing the relationship
between the IDPs so the developer doesnt have to necesarily go to all these different tools.

## Problem Statement
Since advent of k8s and its wide adoption the devops is moving at a fast pace to keep up with industry standards which makes it painful for a developer to keep up with the constant change and learning
new technology and at times keeping up with the current one. The developers really need to focus on business delivery and with all these tools it becomes rather difficult and time consuming to deliver.
We want to bring in all the teams working under one umbrella, following the data model defined thus making it easy for everyone to adopt.

### Persona
The different entites in an organization and the problems they have

#### Developer
* How to get started with my first project. Do I have a getting started guide or a scaffolder that does the job for me and i focus on business logic
* I am already having my service deployed, now I want to move to cloud
* new joiner, how can i get started in the firm
* I want some resources , ephemeral ones, to whom to reach, it is very time consuming
* so many tools to check job status, deployment status and current version canaries etc.


#### Devops/Platform/Infra
* There are so many tickets again to create these resources
* Orphaned test env again?
* Overall visibility into system
* automated service maturity notification for users.
* onboard new technology

#### Team Lead
* Which application needs my attention the most
* Can I reduce the cost of this service. Can this be optimized

#### Dept Lead
* How to enforce guardrails for my org
* Are we inline with Firms goals and delivery
* I need a code freeze, how can i do that across all org

## Service now serves the similar purpose, can we use it?
Service now indeed is a great cataloging software for org's tech stack, incident management workflows and audits. We are not trying to replace Service now but using service now as golden source of truth
to nourish the data into IDP and bind that with other tools which do not have integration with service now yet. The IDP is more developer facing catering to the needs for changing environement.


## What all options do I have for an IDP and which one should we choose from
Spotify had similar issues as the magnitude of their microservices and infra grew and tackeled with this home grown tool called backstage, they opensourced it for communities acceptance and support. Then comes more
elegant soltion enhancing the capabilities of backstage for different industries and purposes. Below is the table that does the comparison of some of the best IDPs in the market.
We are leaving servicenow in this comparison as its not either or solution, but service now will pair with IDP. 

|          | GetPort | Backstage | OpsLevel | Cortex |
| -------- | -------- | -------- | -------- | -------- |
| Cataloging | Support any kind of cataloging with blue print | Predefined set of catalogs | | Row 1, Col 5 |
| Row 2, Col 1 | Row 2, Col 2 | Row 2, Col 3 | Row 2, Col 4 | Row 2, Col 5 |
| Row 3, Col 1 | Row 3, Col 2 | Row 3, Col 3 | Row 3, Col 4 | Row 3, Col 5 |
| Row 4, Col 1 | Row 4, Col 2 | Row 4, Col 3 | Row 4, Col 4 | Row 4, Col 5 |
| Row 5, Col 1 | Row 5, Col 2 | Row 5, Col 3 | Row 5, Col 4 | Row 5, Col 5 |
| Row 6, Col 1 | Row 6, Col 2 | Row 6, Col 3 | Row 6, Col 4 | Row 6, Col 5 |
| Row 7, Col 1 | Row 7, Col 2 | Row 7, Col 3 | Row 7, Col 4 | Row 7, Col 5 |
| Row 8, Col 1 | Row 8, Col 2 | Row 8, Col 3 | Row 8, Col 4 | Row 8, Col 5 |
| Row 9, Col 1 | Row 9, Col 2 | Row 9, Col 3 | Row 9, Col 4 | Row 9, Col 5 |
| Row 10, Col 1 | Row 10, Col 2 | Row 10, Col 3 | Row 10, Col 4 | Row 10, Col 5 |
| Row 11, Col 1 | Row 11, Col 2 | Row 11, Col 3 | Row 11, Col 4 | Row 11, Col 5 |
| Row 12, Col 1 | Row 12, Col 2 | Row 12, Col 3 | Row 12, Col 4 | Row 12, Col 5 |
| Row 13, Col 1 | Row 13, Col 2 | Row 13, Col 3 | Row 13, Col 4 | Row 13, Col 5 |
| Row 14, Col 1 | Row 14, Col 2 | Row 14, Col 3 | Row 14, Col 4 | Row 14, Col 5 |
| Row 15, Col 1 | Row 15, Col 2 | Row 15, Col 3 | Row 15, Col 4 | Row 15, Col 5 |



