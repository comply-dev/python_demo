# pythondemo  

`pythondemo`

## Installing the Chart

```bash
helm install --namespace=pythondemo --name python-demo-1.0.0 .
```

Output is expected to resemble:

```bash
NAME:   pythondemo-1.0.0
LAST DEPLOYED: Tue Sep 18 16:11:42 2018
NAMESPACE: default
STATUS: DEPLOYED
```

## Delete Chart

```bash
helm delete pythondemo-1.0.0 --purge;
```

## List deployed Charts

```bash
helm list
```

or all

```bash
helm list -a
```

List kubernetes stuff

```bash
kubectl get all --namespace pythondemo
```
