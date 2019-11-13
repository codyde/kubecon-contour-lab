# Contour Demo for KubeCon Mini-Labs

This application was written to show building a set of Kubernetes services that can be stitched together with [Project Contour](https://projectcontour.io). The repo is designed to take a step by step approach to configuring Contour starting with a single HTTPProxy configuration, and moving through multiple configurations, includes, and weighting. It is being featured in the KubeCon 2019 VMware Mini-labs, and the Github repo for the steps can be found [here](https://github.com/codyde/kubecon-minilabs-contour)

## Relevant File Descriptions

* Contour-Route-* - Each of these is a step of configuring the Contour HTTPProxy
* Pods and Services - This will deploy all of the pods for the application against a Kubernetes environment
* Dark Mode Pods and Services - This will deploy the same application as above, but with the theme set to ClarityUI's dark mode

## Application Information

The application was written in Python Flask. There is a lot of room for optimizations in how the application was written and should not be considered a best practice guide for building a Flask application in Kubernetes.

## Deployment Instructions

* Clone down this repository
* Install Project Contour into your Kubernetes Cluster
* Replace relevant fqdn entries in Contour HTTPProxy configuration files
* Apply either the Pods and Services YAML or Dark Mode Pods and Services YAML
* Apply relevant Contour HTTPProxy configurations
