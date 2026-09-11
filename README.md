# AI Commerce Mind

Production-grade AI-first e-commerce platform built with **Python, FastAPI, PostgreSQL/pgvector, Redis, RAG, MCP, and AI Agents**.

The project is designed as a serious portfolio system for demonstrating senior-level backend engineering, modern AI architecture, retrieval systems, agentic workflows, observability, security, cloud infrastructure, and scalable service design.

---

## Vision

AI Commerce Mind is not just another e-commerce CRUD application.

The goal is to build a production-grade commerce platform where AI is a first-class architectural layer.

The system combines:

- traditional e-commerce backend capabilities;
- semantic product discovery;
- hybrid search;
- Retrieval-Augmented Generation;
- AI shopping assistants;
- catalog intelligence;
- support agents;
- MCP integrations;
- human approval workflows;
- AI evaluations;
- production observability;
- scalable cloud infrastructure.

The project starts as a **modular monolith** and evolves gradually toward a more distributed architecture only when there is a clear technical reason to do so.

---

# Core Use Cases

## Customer Search

A customer can ask:

> Show me black waterproof winter sneakers under €120 with good reviews.

The system will combine:

- structured PostgreSQL filters;
- keyword/full-text search;
- pgvector semantic search;
- metadata filtering;
- reranking;
- LLM-based recommendation generation.

---

## AI Shopping Assistant

A customer can ask:

> I have a €150 budget and need shoes for winter running.

The assistant can use tools such as:

```text
search_products
get_product
get_product_variants
check_inventory
get_reviews
compare_products
```

The result should contain real products from the catalog instead of hallucinated recommendations.

---

## Product Knowledge RAG

Customers can ask questions such as:

> Is this jacket waterproof?

or:

> Can I wash this product at 60°C?

The answer can be generated from:

- product manuals;
- technical specifications;
- FAQs;
- manufacturer documentation;
- descriptions;
- customer reviews.

Answers should contain source references.

---

## AI Catalog Assistant

A merchant can ask:

> Find products with missing attributes.

or:

> Find potentially duplicated products.

or:

> Show products with a high number of views but poor conversion.

The AI agent can analyze catalog data and suggest improvements.

---

## Product Enrichment

Raw imported product data can be enhanced with AI.

Example:

```text
Raw supplier product
        ↓
LLM enrichment
        ↓
Structured title
Description
Attributes
SEO metadata
Category suggestion
        ↓
Human approval
        ↓
Catalog update
```

AI-generated mutations should not be applied blindly.

Destructive or sensitive operations should require explicit approval.

---

# Architecture

Initial architecture:

```text
                        ┌─────────────────┐
                        │     Clients     │
                        │ Web / Mobile /  │
                        │ External APIs   │
                        └────────┬────────┘
                                 │
                                 ▼
                       ┌──────────────────┐
                       │     FastAPI      │
                       │    REST API      │
                       └────────┬─────────┘
                                │
          ┌─────────────────────┼──────────────────────┐
          │                     │                      │
          ▼                     ▼                      ▼
 ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
 │    Commerce    │    │   AI Layer     │    │   Background   │
 │    Modules     │    │                │    │     Workers     │
 └───────┬────────┘    └───────┬────────┘    └───────┬────────┘
         │                     │                      │
         │                     │                      │
         ▼                     ▼                      ▼
 ┌────────────────┐    ┌────────────────┐    ┌────────────────┐
 │   PostgreSQL   │    │     LLMs       │    │     Redis      │
 │   + pgvector   │    │ RAG / Agents   │    │ Queue / Cache  │
 └────────────────┘    └────────────────┘    └────────────────┘
```

The project begins as a **modular monolith**.

Microservices will not be introduced simply for architectural fashion.

Services will be extracted only when a component has clear requirements around:

- scaling;
- deployment independence;
- throughput;
- fault isolation;
- technology specialization.

---

# Technology Stack

## Backend

- Python 3.13+
- FastAPI
- Pydantic v2
- SQLAlchemy 2
- Alembic
- asyncpg
- psycopg

## Database

- PostgreSQL
- pgvector

## Caching / Messaging

- Redis

## AI

- LLM APIs
- Embeddings
- Retrieval-Augmented Generation
- Hybrid Search
- Reranking
- AI Agents
- Tool Calling
- MCP
- Evaluation pipelines

## Development

- uv
- Ruff
- Pyright
- pytest
- pytest-asyncio
- httpx
- pre-commit

## Infrastructure

- Docker
- Docker Compose
- GitHub Actions

Later:

- Go
- AWS
- Kubernetes
- Terraform
- OpenTelemetry
- Prometheus
- Grafana

---

# Repository Structure

```text
ai-commerce-mind/
│
├── src/
│   └── ai_commerce_mind/
│       │
│       ├── main.py
│       │
│       ├── api/
│       │
│       ├── core/
│       │
│       ├── db/
│       │
│       ├── modules/
│       │   ├── identity/
│       │   ├── organization/
│       │   ├── catalog/
│       │   ├── pricing/
│       │   ├── inventory/
│       │   ├── cart/
│       │   ├── orders/
│       │   ├── payments/
│       │   ├── shipping/
│       │   ├── promotions/
│       │   ├── reviews/
│       │   └── customers/
│       │
│       ├── ai/
│       │   ├── embeddings/
│       │   ├── search/
│       │   ├── rag/
│       │   ├── agents/
│       │   ├── tools/
│       │   ├── mcp/
│       │   └── evaluation/
│       │
│       ├── integrations/
│       │
│       └── workers/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── alembic/
│
├── docs/
│   ├── architecture/
│   └── adr/
│
├── docker/
│
├── .github/
│   └── workflows/
│
├── .env.example
├── .gitignore
├── Dockerfile
├── compose.yaml
├── alembic.ini
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Engineering Principles

The project follows several important engineering principles.

## Modular Monolith First

Domain modules should have clear boundaries.

Example:

```text
Catalog
Pricing
Inventory
Orders
Customers
AI
```

Cross-module coupling should be minimized.

---

## Async I/O

External I/O should use async APIs whenever appropriate.

Examples:

- PostgreSQL;
- Redis;
- HTTP APIs;
- LLM providers;
- MCP services.

---

## Strong Typing

The project uses:

- Python type annotations;
- Pyright strict mode;
- Pydantic validation;
- typed SQLAlchemy models;
- typed service interfaces.

---

## API Versioning

Public APIs should be versioned from the beginning.

Example:

```text
/api/v1/products
/api/v1/orders
/api/v1/search
```

---

## Multi-Tenancy

The platform should support multiple organizations and stores.

Typical hierarchy:

```text
Organization
    ↓
Store
    ↓
Users / Products / Orders
```

Tenant isolation is treated as a fundamental architecture concern.

---

## Human Approval for Sensitive AI Actions

AI agents should not autonomously perform dangerous operations.

Examples requiring approval:

```text
refund_order
delete_product
publish_price_change
bulk_update_products
cancel_order
```

Read-only operations can typically execute automatically.

---

# Domain Model

Core commerce entities include:

```text
Organization
Store
User
Membership
Role

Customer
CustomerAddress

Category
Brand
Product
ProductVariant
Attribute
AttributeValue

Price
Promotion
Coupon

Warehouse
Inventory
StockMovement

Cart
CartItem

Order
OrderItem

Payment
Refund

Shipment
Return

Review
Wishlist
```

AI-related entities may include:

```text
Conversation
Message

Embedding

SearchQuery
RetrievalRun
GenerationRun

Agent
AgentRun
AgentStep

ToolExecution

Prompt
PromptVersion

Evaluation
EvaluationRun
```

---

# Search Architecture

Search will evolve through several stages.

## Stage 1

Structured database filtering.

```text
category
brand
price
availability
attributes
```

## Stage 2

PostgreSQL full-text search.

## Stage 3

Vector search using pgvector.

## Stage 4

Hybrid search.

```text
keyword score
+
vector similarity
+
business ranking
```

## Stage 5

Reranking.

Final pipeline:

```text
User Query
    ↓
Query Understanding
    ↓
Structured Filters
    ↓
Full-Text Search
    ↓
Vector Search
    ↓
Candidate Merge
    ↓
Reranker
    ↓
Final Products
```

---

# RAG Architecture

Product knowledge ingestion:

```text
Document
    ↓
Extract
    ↓
Normalize
    ↓
Chunk
    ↓
Embed
    ↓
pgvector
```

Question answering:

```text
Question
    ↓
Query Understanding
    ↓
Retriever
    ↓
Top-K chunks
    ↓
Reranker
    ↓
Context Builder
    ↓
LLM
    ↓
Answer + Sources
```

Possible knowledge sources:

- product manuals;
- technical specifications;
- brand documents;
- FAQs;
- return policies;
- warranty documents;
- customer reviews.

---

# Agents

The first agents should have narrow responsibilities.

## Shopping Agent

Tools:

```text
search_products
get_product
get_product_variants
get_reviews
check_inventory
compare_products
```

---

## Catalog Agent

Tools:

```text
find_products
find_duplicates
find_missing_attributes
suggest_category
update_product
```

Mutating tools should support approval workflows.

---

## Support Agent

Tools:

```text
get_customer
get_order
get_order_items
get_shipment
get_tracking
get_return_policy
```

Potential protected tools:

```text
cancel_order
refund_order
create_return
```

---

# MCP

AI Commerce Mind will support both MCP server and MCP client capabilities.

## MCP Server

The platform can expose tools such as:

```text
commerce.search_products
commerce.get_product
commerce.check_inventory
commerce.get_order
commerce.get_customer
commerce.search_knowledge
```

External AI clients can interact with the commerce platform through a standardized tool interface.

---

## MCP Client

AI Commerce Mind agents may consume external MCP servers.

Potential integrations:

```text
ERP
CRM
Customer Support
Shipping
Analytics
GitHub
Internal Knowledge Systems
```

---

# Evaluation

AI features must be measurable.

## Retrieval Metrics

Examples:

```text
Recall@K
MRR
Precision@K
Context Relevance
```

## Generation Metrics

Examples:

```text
Faithfulness
Answer Relevance
Groundedness
Citation Correctness
```

## Operational Metrics

```text
LLM latency
retrieval latency
token usage
cost
tool failures
agent steps
agent completion rate
```

---

# Observability

Every production request should eventually be traceable.

Useful identifiers:

```text
request_id
trace_id
organization_id
store_id
user_id
conversation_id
agent_run_id
```

Observability stack planned later:

```text
OpenTelemetry
Prometheus
Grafana
Structured JSON Logs
```

---

# Security

Security areas include:

- JWT authentication;
- refresh tokens;
- password hashing;
- role-based access control;
- tenant isolation;
- rate limiting;
- secrets management;
- audit logs;
- request validation;
- tool permissions;
- agent iteration limits;
- agent cost limits;
- human approvals.

---

# Development Roadmap

The roadmap is intentionally large.

The objective is not to implement everything immediately.

Each module should represent a meaningful engineering milestone.

---

## Phase 1 — Foundation

### ACM-001 — Architecture & ADRs

Define:

- modular monolith architecture;
- module boundaries;
- dependency rules;
- database strategy;
- AI abstraction strategy;
- background processing strategy.

---

### ACM-002 — Repository Bootstrap

Setup:

- uv;
- Python;
- FastAPI;
- Ruff;
- Pyright;
- pytest;
- GitHub Actions;
- Docker.

---

### ACM-003 — Application Core

Implement:

- application factory;
- configuration;
- environments;
- exception handling;
- structured application lifecycle.

---

### ACM-004 — PostgreSQL Foundation

Implement:

- SQLAlchemy async engine;
- sessions;
- transaction patterns;
- database configuration.

---

### ACM-005 — Alembic Migration System

Implement:

- async migrations;
- migration conventions;
- initial schema migration.

---

### ACM-006 — Shared Database Models

Introduce:

- UUID identifiers;
- timestamps;
- reusable base models;
- optimistic concurrency support.

---

### ACM-007 — Redis Infrastructure

Introduce:

- Redis client;
- connection lifecycle;
- cache primitives;
- distributed locking foundations.

---

### ACM-008 — Background Job System

Implement:

- queues;
- workers;
- retries;
- dead-letter behavior;
- idempotency.

---

## Phase 2 — Identity & Multi-Tenancy

### ACM-009 — User

Implement user domain model.

---

### ACM-010 — Authentication

Implement:

- registration;
- login;
- access tokens;
- refresh tokens;
- logout.

---

### ACM-011 — Organization

Introduce multi-tenant organization model.

---

### ACM-012 — Store

Allow an organization to own multiple stores.

---

### ACM-013 — Membership & Roles

Roles:

```text
OWNER
ADMIN
MEMBER
VIEWER
```

---

### ACM-014 — Tenant Isolation

Ensure every tenant-owned resource is properly scoped.

---

## Phase 3 — Catalog

### ACM-015 — Category

Hierarchical product categories.

---

### ACM-016 — Brand

Brand/manufacturer management.

---

### ACM-017 — Product

Core product aggregate.

---

### ACM-018 — Product Variant

Support:

```text
size
color
material
SKU
barcode
```

---

### ACM-019 — Attribute

Dynamic product attributes.

---

### ACM-020 — Attribute Value

Product attribute values and filtering metadata.

---

### ACM-021 — Product Media

Images, videos and product assets.

---

### ACM-022 — Catalog REST API

CRUD and public catalog endpoints.

---

## Phase 4 — Pricing & Inventory

### ACM-023 — Price

Support:

- currencies;
- base price;
- sale price;
- validity periods.

---

### ACM-024 — Promotion

Promotional rules.

---

### ACM-025 — Coupon

Coupon codes and constraints.

---

### ACM-026 — Warehouse

Warehouse management.

---

### ACM-027 — Inventory

Stock by product variant and warehouse.

---

### ACM-028 — Stock Movement

Track:

```text
purchase
sale
return
adjustment
reservation
release
```

---

## Phase 5 — Search

### ACM-029 — Product Filtering

Structured filters.

---

### ACM-030 — PostgreSQL Full-Text Search

Keyword-based product search.

---

### ACM-031 — pgvector

Enable vector extension and vector indexes.

---

### ACM-032 — Product Embeddings

Generate embeddings from product content.

---

### ACM-033 — Semantic Product Search

Search products by semantic meaning.

---

### ACM-034 — Hybrid Search

Combine structured, lexical, and vector search.

---

### ACM-035 — Search Reranking

Improve result quality through reranking.

---

## Phase 6 — Commerce

### ACM-036 — Customer

Customer profile management.

---

### ACM-037 — Cart

Shopping cart and cart items.

---

### ACM-038 — Order

Order creation and order lifecycle.

---

### ACM-039 — Payment

Payment abstraction and transaction lifecycle.

---

### ACM-040 — Shipping

Shipment and tracking model.

---

### ACM-041 — Returns & Refunds

Return and refund workflows.

---

### ACM-042 — Reviews

Product reviews and ratings.

---

### ACM-043 — Wishlist

Customer wishlist.

---

## Phase 7 — AI

### ACM-044 — Product Knowledge Ingestion

Build ingestion pipeline for:

- manuals;
- specifications;
- FAQs;
- policies;
- product documents.

---

### ACM-045 — Product Knowledge RAG

Answer product questions with retrieved context and citations.

---

### ACM-046 — AI Shopping Assistant

Build first customer-facing agent.

---

### ACM-047 — Catalog Agent

AI tooling for catalog quality and enrichment.

---

### ACM-048 — Support Agent

Agent for orders, shipping and support questions.

---

### ACM-049 — Human Approval Workflows

Introduce approval checkpoints for sensitive agent actions.

---

### ACM-050 — MCP Server

Expose commerce tools through MCP.

---

### ACM-051 — MCP Client

Consume third-party MCP services.

---

## Phase 8 — AI Quality & Production

### ACM-052 — AI Evaluations

Introduce automated retrieval and generation evaluation.

---

### ACM-053 — Prompt Management

Versioned prompts and prompt metadata.

---

### ACM-054 — Agent Observability

Trace:

```text
agent runs
agent steps
tools
latency
tokens
cost
```

---

### ACM-055 — Guardrails

Implement:

- input validation;
- tool allowlists;
- output constraints;
- iteration limits;
- cost limits.

---

## Phase 9 — Production Engineering

### ACM-056 — Audit Logging

Track security-sensitive operations.

---

### ACM-057 — Rate Limiting

API and AI endpoint rate limits.

---

### ACM-058 — OpenTelemetry

Distributed tracing foundations.

---

### ACM-059 — Metrics

Prometheus-compatible application metrics.

---

### ACM-060 — Production Logging

Structured JSON logging and correlation IDs.

---

## Phase 10 — Scaling

### ACM-061 — Go Service

Extract a high-throughput component to Go.

Potential candidates:

```text
ingestion
events
API gateway
search aggregation
```

---

### ACM-062 — Event Architecture

Introduce events where justified.

Potential events:

```text
ProductCreated
ProductUpdated
OrderCreated
StockChanged
DocumentUploaded
EmbeddingRequested
```

---

### ACM-063 — AWS Infrastructure

Target architecture may include:

```text
ALB
ECS / EKS
RDS PostgreSQL
ElastiCache Redis
S3
Secrets Manager
CloudWatch
```

---

### ACM-064 — Terraform

Infrastructure as Code.

---

### ACM-065 — Kubernetes

Deploy:

```text
FastAPI API
workers
Go services
Redis integrations
jobs
```

---

### ACM-066 — Kubernetes Autoscaling

Introduce:

- HPA;
- resource limits;
- health probes;
- graceful shutdown.

---

### ACM-067 — Production Deployment

Build full production deployment pipeline.

---

# Target Learning Outcomes

This project is intended to demonstrate practical competence in:

## Python

- async/await;
- typing;
- protocols;
- context managers;
- generators;
- dependency injection;
- packaging;
- testing.

## Backend Engineering

- REST APIs;
- PostgreSQL;
- transactions;
- concurrency;
- Redis;
- queues;
- caching;
- distributed systems.

## AI Engineering

- embeddings;
- vector databases;
- semantic search;
- hybrid search;
- reranking;
- RAG;
- tool calling;
- agents;
- MCP;
- evaluation;
- guardrails.

## Production Engineering

- CI/CD;
- observability;
- Docker;
- AWS;
- Kubernetes;
- Terraform;
- Go services.

---

# Initial Vertical Slice

The first commerce slice will be intentionally small:

```text
Organization
    ↓
Store
    ↓
Category
    ↓
Product
    ↓
ProductVariant
    ↓
Price
```

Immediately after this slice, the project will add:

```text
Product
    ↓
Embedding
    ↓
pgvector
    ↓
Semantic Search
```

This ensures AI functionality appears early instead of spending months implementing traditional CRUD before introducing the core AI capabilities.

---

# Development Workflow

Development branch:

```text
develop
```

Stable branch:

```text
main
```

Typical workflow:

```text
feature branch
    ↓
pull request
    ↓
develop
    ↓
release
    ↓
main
```

Example:

```bash
git checkout develop
git pull

git checkout -b feature/acm-004-database-foundation
```

After implementation:

```bash
uv run ruff format .
uv run ruff check .
uv run pyright
uv run pytest
```

Then:

```bash
git add .
git commit -m "feat(database): add async database foundation"
git push -u origin feature/acm-004-database-foundation
```

---

# Local Development

Install dependencies:

```bash
uv sync
```

Run application:

```bash
uv run uvicorn ai_commerce_mind.main:app --reload
```

Run Docker environment:

```bash
docker compose up --build
```

Run tests:

```bash
uv run pytest
```

Run Ruff:

```bash
uv run ruff check .
```

Format code:

```bash
uv run ruff format .
```

Run type checking:

```bash
uv run pyright
```

---

# API

Development API:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

OpenAPI:

```text
http://localhost:8000/openapi.json
```

Health:

```text
GET /api/v1/health
```

---

# Project Status

Current phase:

```text
ACM-002 — Repository Bootstrap
```

Next milestones:

```text
ACM-003 Application Core
ACM-004 PostgreSQL Foundation
ACM-005 Alembic
ACM-006 Shared Database Models
ACM-007 Redis Infrastructure
```

---

# License

License will be selected later.

---

# Author

Built as a production-grade backend and AI engineering portfolio project.
