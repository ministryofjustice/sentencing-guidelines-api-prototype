# Sentencing guidelines API prototype

A prototype API for providing offences and sentencing guidelines.

## Description

Currently, the process of requesting legal aid involves solicitors and providers using e-form to input all the necessary data. Caseworkers process each request from the e-form form backend and they import each one of them into MAAT cross-referencing the information submitted with the [sentencing guidelines website](https://www.sentencingcouncil.org.uk/offences/). 

## Goal

Produce an API that would allow us to look up sentencing guidelines programmatically and allow caseworkers to easily navigate through them so they can find guidelines in a more efficient and cosistent manner.

## Problems:
- Guidelines are structured slightly differently.
- At the moment Case Workers process applications having lot of different pages opened in their browser (MAAT, Eform, the sentencing guidelines website)
