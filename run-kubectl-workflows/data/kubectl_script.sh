#!/bin/bash

for i in {1..10}; do
    VERSION=$(kubectl get nodes --kubeconfig="$1" | grep -i ip | awk '{print $5}')
    echo "$i : $VERSION"
done
