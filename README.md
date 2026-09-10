# genpark-schnorr-threshold-multisig-musig2-skill

[![GenPark Skill](https://img.shields.io/badge/GenPark-Skill-blue.svg)](https://github.com/alphaparkinc/genpark-schnorr-threshold-multisig-musig2-skill)
[![Agentic AI](https://img.shields.io/badge/Agentic-AI-orange.svg)](https://github.com/alphaparkinc/genpark-schnorr-threshold-multisig-musig2-skill)
[![Zero Pip Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library-green.svg)](https://github.com/alphaparkinc/genpark-schnorr-threshold-multisig-musig2-skill)

MuSig2 multi-signature and threshold Schnorr aggregation protocol for compact collective authorization proofs.

## Architecture
```mermaid
graph TD
    A[Client / Signer Node] --> B[genpark-schnorr-threshold-multisig-musig2-skill]
    B --> C[Cryptographic Engine / State Machine]
    C --> D[Encrypted / Blinded / Verified Output]
```

## Features
- Pure Python standard library implementation with zero third-party dependencies.
- Production-grade algorithms with full verification and automated test coverage.
- Standalone client, MCP protocol server, and execution examples.

## Quickstart
```bash
python example_usage.py
```
