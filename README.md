# LexiScan Auto

Automated Legal Entity Extraction System using OCR and Named Entity Recognition (NER).

## Project Overview
LexiScan Auto is designed to extract key legal entities such as Party Names,
Dates, Monetary Amounts, Jurisdiction, and Agreement Types from unstructured
legal PDF documents.

Named Entity Definitions (NER Schema)

| Entity | Description | Example |
|------|------------|--------|
| PARTY | Legal parties in the contract | Microsoft, Infosys Ltd |
| DATE | Important contract dates | 12 January 2024 |
| AGREEMENT_TYPE | Type of agreement | NDA, SLA |
| AMOUNT | Monetary values | $50,000 |
| JURISDICTION | Governing law | India, California |
| TERM | Contract duration | 5 years |

BIO Tagging Scheme

The BIO (Beginning–Inside–Outside) tagging scheme is used for Named Entity
Recognition to represent entity spans at the token level.

### BIO Tag Definitions
- **B-ENTITY**: Beginning of an entity
- **I-ENTITY**: Inside an entity
- **O**: Outside any entity

### Example

Sentence:
This Agreement is between Microsoft Corporation and Infosys Ltd

BIO Format:
This O  
Agreement B-AGREEMENT_TYPE  
is O  
between O  
Microsoft B-PARTY  
Corporation I-PARTY  
and O  
Infosys B-PARTY  
Ltd I-PARTY
