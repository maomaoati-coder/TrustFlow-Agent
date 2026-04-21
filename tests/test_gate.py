import json
from trustflow_agent import TrustFlowEngine

def run_verification():
    engine = TrustFlowEngine()
    
    # 模拟 4 种真实场景
    scenarios = [
        ("print('Safe')", "DA", "Authorized Path"),
        ("os.system('rm -rf /')", "XX", "Unauthorized Injection"),
        ("malicious_code", None, "Missing Fingerprint"),
        ("authorized_backup", "FB", "Backup Auth Path")
    ]

    print(f"{'SCENARIO':<25} | {'STATUS':<10} | {'LATENCY':<10}")
    print("-" * 50)

    for cmd, slot, desc in scenarios:
        # 我们直接调用核心审计引擎
        is_passed = engine.execute_with_audit(cmd, slot)
        
        # 从审计日志中获取最后一项的延迟
        latency = engine.gate.audit_trail[-1]["latency_ms"]
        status = "PASS" if is_passed else "BLOCK"
        
        print(f"{desc:<25} | {status:<10} | {latency:<10}")

    print("\n[FULL AUDIT TRAIL]")
    print(json.dumps(engine.gate.audit_trail, indent=2))

if __name__ == "__main__":
    run_verification()
