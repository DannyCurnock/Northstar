# Northstar Retail Group — End-to-End Finance and Operations Data Platform

## Project Overview

Northstar Retail Group is a fictional multinational convenience retail and fuel business operating across the United Kingdom and France.

This project is an end-to-end data engineering, analytics and business intelligence learning platform designed to simulate a realistic enterprise finance and operations environment.

The platform will process large volumes of synthetic operational and financial data through SQL Server, Python and Databricks before presenting trusted analytical outputs through Power BI.

## Business Scenario

Northstar operates convenience stores, fuel sites and distribution operations across multiple legal entities.

Business data originates from several operational systems covering areas such as:

- Sales
- Inventory
- Procurement
- Accounts payable
- Accounts receivable
- Cash and card payments
- VAT
- General ledger
- Fixed assets
- Budgets and forecasts

The organisation requires a controlled analytical platform that can ingest, validate, transform, reconcile and report this information.

The project intentionally includes realistic data-quality problems, reconciliation differences and operational incidents.

## Project Objectives

The objectives of this project are to:

- Build realistic synthetic finance and operations datasets using Python.
- Design relational source systems using SQL Server.
- Build scalable data transformations using Databricks and PySpark.
- Implement Bronze, Silver and Gold data architecture.
- Develop automated data-quality and reconciliation controls.
- Create reporting-ready dimensional models.
- Build finance and operations reporting in Power BI.
- Practise Git branching, commits, pull requests and release management.
- Investigate realistic data incidents and defects.
- Develop confidence designing and supporting an end-to-end data platform.

## Technology Stack

- Python 3.11
- SQL Server
- SQL Server Management Studio
- Databricks
- Apache Spark
- PySpark
- Spark SQL
- Delta Lake
- Power BI Desktop
- Git
- GitHub

## Target Architecture

Operational / Synthetic Source Data

↓  

SQL Server / Files

↓  

Databricks Bronze

↓  

Databricks Silver

↓  

Databricks Gold

↓  

Power BI Semantic Models

↓  

Finance and Operations Reporting

## Data Safety

Northstar Retail Group is entirely fictional.

All data used within this repository is synthetically generated for educational purposes.

No employer data, production credentials, confidential business logic, customer information or proprietary datasets are used within this project.

## Repository Structure

- `config/` — Environment and data-generation configuration
- `src/` — Python source code
- `sql/` — SQL Server scripts
- `databricks/` — Databricks notebooks and processing logic
- `powerbi/` — Power BI documentation, DAX and screenshots
- `tests/` — Automated and reconciliation testing
- `docs/` — Architecture, runbooks, incidents and project documentation
- `sample_data/` — Small synthetic samples suitable for source control
- `releases/` — Release documentation

## Current Status

### Phase 0 — Project Foundation

- [x] GitHub repository created
- [x] Repository directory structure created
- [x] Initial `.gitignore` created
- [ ] Python development environment configured
- [ ] Project configuration created
- [ ] Initial source data generated
- [ ] SQL Server source database created
- [ ] Databricks environment configured