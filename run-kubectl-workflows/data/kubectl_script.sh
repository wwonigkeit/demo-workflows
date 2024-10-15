#!/bin/bash

for i in {1..10}; do
    kubectl get nodes --kubeconfig=$KUBECONFIG > version.txt

    VERSION=$(cat version.txt)

    echo $VERSION