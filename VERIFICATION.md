​🛡️ TrustFlow-Agent: Physical Integrity & Telemetry Verification Guide
​This guide provides instructions to replicate the TrustFlow-Agent hardware-level logic interception and granular telemetry generation.

​🚀 Step-by-Step Verification Process
​1. Execute the Core Audit Script
​Run the following command in your terminal:
​python trustflow_agent.py

2. Analyze the Granular Telemetry (JSON Output)
​After interception, the Agent automatically generates a JSON report. This data provides the "Evidence" needed for downstream semantic layers.

​📈 Execution Evidence & Validation
​Below is the actual execution log verified in a Termux environment. Your output should match the JSON structure shown here:
​<p align="center">
<img src="assets/trustflow_verification.png" alt="TrustFlow Telemetry Verification" width="600">
</p>

​Architect's Note:
This verification proves that TrustFlow-Agent successfully bridges the gap between "Physical Interception" and "Semantic Understanding."
