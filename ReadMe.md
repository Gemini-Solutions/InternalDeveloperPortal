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

|          | GetPort<img src="https://github.com/Gemini-Solutions/InternalDeveloperPortal/blob/main/resources/port.png" alt="GetPort Image" width="50" height="50"> | Backstage(OSS) | OpsLevel | Cortex |
| -------- | -------- | -------- | -------- | -------- |
| [Cataloging](#cataloging)     | Support any kind of cataloging with blue print | Predefined set of catalogs k8s, service etc | Pre defined catalog | Pre defined catalog |
| [Opinionated](#opinionated) | No | Yes | Yes | Yes |
| [workflow automation](#workflow-automation) | Getport supports any kinds of workflows and integration with blue prints and actions | Yes, by customizing | webhooks and actions | Yes |
| [Scaffolder](#scaffolder) | Predefined and easy to create new one | Available | Yes | Yes |
| [Auto Discovery](#auto-discovery) | Yes | No | No | No |
| [OSS](#oss) | Port's ocean is an Opensource | Most widely accespted IDP as OS | No | No |
| [RBAC](#rbac) | Yes | Yes, paid | Flat model but actions can be restricted only with team owners | Yes |
| [SCIM Integration](#scim-integration) | Yes | Yes | Very wide integration | Yes |
| [Scorecards](#scorecards) | Yes | Not so mature | Yes | Yes |
| [Tech Docs](#tech-docs) | Yes | Yes | Yes | Yes |
| [Audit Logs](#audit-logs) | Yes | No | Yes | Yes
| [Extensibility](#extensibility) | Easiest to define custom module with port | need strong type script experience and lot of coding | cant be customized | Cant be customized |
| [Ephemeral Environments](#ephemeral-environments)| Yes | No | No | No |
| [Incident Management](#incident-management) | Yes | Yes | No | No |
| [Action Webhooks](#action-webhooks) | Yes | Yes | Yes | Yes |
| [Security](#security) | Yes SOC2| No | Yes | Yes | 
| [Real Time Sync](#real-time-sync) | Yes | No | Yes | Yes | 
| [Gitops](#gitops) | Yes | No | Yes | Yes|
| (Git Management)(#git-management) | Yes | Yes | Yes | Yes
| [Pricing](#pricing) | 240USD per user per year | Free | NA | NA |







































#### Cataloging
It is the way as to how can you terraform your own IDP or how easy it is to customize the objects/entities in an IDP. Different firms have different use cases which cant be categorized into already existing catalog/objects, hence getPort stands out with only one of its kind as it supports any kinds. It has the model of Being your Own data.

#### Scaffolder
The ease of building and maintainning software templates. All support creating new ones .

#### workflow automation
Creation of multistep workflow to manage the lifecycle of our applications.

#### Opinionated
Do providers have some sort of enforcement of strucutres as to how we should proceed with our IDP, all other than Port has some sort of predefined schema. This is both a pro and con of port. 

#### Auto Discovery
The ability to automatically detect data and nourish on the UI

#### OSS
opensource community support, backstage by far has been leading in OSS but it maynot be the perfect as it takes too much effort to even standup a test instance of backstage and everything is just plugin and 
catalog in backstage. Following that Port has ocean community to support the opensource initiatives.

#### SCIM Integration 
System for Cross-domain Identity Management, is an open standard that allows for the automation of user provisioning.

#### Scorecards
They provide an insight into how mature our service is with the company's defined standards

#### Tech docs 
The ability to support feature rich documenation, search capabilities, audits etc

#### Extensibility
Ease of extending the Functionality of an IDP by adding support of new plugins.

#### RBAC
roles based access control for our actions and events and visibility.

#### Audit Logs
Changes in the IDP itself, who changed what.

#### Incident Management
On call support, with ticket creation escalation and resolution

#### Ephemeral environments
Ease to test and create mock environement to support POCs and some test cases

#### Security
If the IDP itself is secure and following standards

#### Real Time Sync
How is data reflected into IDP if a change happens

#### Gitops
Inherent support for gitops model

#### Action Webhooks 
How can we make events trigger to and from IDP

#### Pricing
what is the license cost of per user.

## User Enagement : What's and Hows
The tool is a success if it not only saves developer's time to market but also has the least learning curve and it's a pull factor rather being pushed from org, this can be achieved if
* The UI is appealing and has amazing UX and aesthetic design : Port does justify this once the blueprint and entities are setup
* Focussed delivery : Not overwhelming users with yet another tool and hacving to manage more yamls and configuration. Show them what they really care about.
* Control : Is it too much restricted? can they for once create the resources without creating too many tickets and still be in compliance with org standards
* Adaptation and innovation : Adding new features and integration to support all sort of requests .


## Conclusion
Backstage has undoubtebly the most widely accepted IDP and contributed by open source community, but it is too much hassle to manage the backstage and having to do so many customizations. Getport extends the
functionailty of backstage by following bringing your own data model, where it lets user define the whole structure of an IDP according to their standards and it simply nourishes them. We can also establish the
relationship between different entities thus saving lot of time and auto discovery is enabled by default with this feature.

## Roadmap to deployment
Either we can go do our POC with getports preview environment without having to go over the official procurement
or we can still keep up the backstage POC, start with getport's procurement and then use it's migration guide to move off of backstage in one go.

## Impact in case of Failure
IDP is just a portal to all the other tools and service to accelerate delivery, if it goes down it might impact the time to market as before IDP era but BAU would still be there without leading to an actual business loss.

## Vendor Lockin
Though we'd be choosing one vendor but we must ensure all our guardrails, scaffolder and blueprint are code first and we have a state managed. 



